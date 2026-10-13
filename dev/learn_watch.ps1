<#
  Watches design-library\ for dropped design images and DESIGN.md files and learns them with a background Claude run
  (design-library\LEARN.md). Started hidden at logon by "Design library watcher.vbs" in the Startup folder.

    learn_watch.ps1                  watch until logoff (one instance per user)
    learn_watch.ps1 -Once            learn whatever is waiting now, then exit
    learn_watch.ps1 -Lib <folder>    watch another copy of the library (tests); drops go in <library>\inspiration

  Log: <workspace>\_temp\learn\watch.log. Stop it: end the hidden powershell in Task Manager, or delete the
  Startup shortcut to stop it starting at logon.
#>
param([switch]$Once, [string]$Lib)
$ErrorActionPreference = 'Stop'

# Resolve the real pipeline folder (this script may be reached through the ~\.claude\skills\website junction).
$pipeline = (Get-Item $PSScriptRoot).Parent
if ($pipeline.LinkType) { $pipeline = Get-Item @($pipeline.Target)[0] }
$workspace = $pipeline.Parent.Parent.FullName
if (-not $Lib) { $Lib = Join-Path $pipeline.FullName 'design-library' }
$Lib = (Resolve-Path $Lib).Path
$prep = Join-Path $PSScriptRoot 'learn_prep.py'
$logDir = Join-Path $workspace '_temp\learn'
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$log = Join-Path $logDir 'watch.log'
function Log($msg) { Add-Content -Path $log -Value ('{0:yyyy-MM-dd HH:mm:ss}  {1}' -f (Get-Date), $msg) -Encoding UTF8 }

Add-Type -AssemblyName System.Windows.Forms, System.Drawing
# One tray icon for the watcher's lifetime; balloons show on it without blocking.
$icon = New-Object System.Windows.Forms.NotifyIcon
$icon.Icon = [System.Drawing.SystemIcons]::Information
$icon.Text = 'Design library watcher'
$icon.Visible = $true
function Notify($title, $text) {
  try { $icon.ShowBalloonTip(8000, $title, $text, 'Info') } catch { Log "notify failed: $_" }
}

$exts = '.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp'
# Drops land in inspiration\; learned images there are already lowercase-slug .webp files. A dropped .md
# (a DESIGN.md) is always new: learned ones are filed in inspiration\design-md\.
function Drops {
  Get-ChildItem -LiteralPath (Join-Path $Lib 'inspiration') -File |
    Where-Object { ($_.Extension.ToLower() -eq '.md') -or
      (($exts -contains $_.Extension.ToLower()) -and -not ($_.Name -cmatch '^[a-z0-9]+(-[a-z0-9]+)*\.webp$')) }
}
function Waiting { [int](& python $prep --check --lib $Lib 2>$null) }

function Learn {
  $names = (Drops | ForEach-Object Name) -join ', '
  if (-not $names) { $names = 'pending references' }
  Log "learning: $names"
  Notify 'Design library' "Learning $names..."
  # No double quotes in the prompt: Windows PowerShell 5.1 mangles them in native-command arguments.
  $prompt = "The design library folder is: $Lib -- Learn the dropped design references by following the file LEARN.md in that folder exactly, step by step."
  $started = Get-Date
  Push-Location $Lib
  # 'Continue': Windows PowerShell 5.1 turns any stderr line from a native command (claude prints settings
  # warnings there) into a terminating error under 'Stop'.
  $ErrorActionPreference = 'Continue'
  try {
    $out = & claude -p $prompt --permission-mode acceptEdits --add-dir $workspace `
      --allowedTools 'Read' 'Write' 'Edit' 'Glob' 'Grep' 'Bash(python *)' 2>&1 | Out-String
  } finally { Pop-Location; $ErrorActionPreference = 'Stop' }
  Add-Content -Path $log -Value $out -Encoding UTF8
  $learned = @(Get-ChildItem -LiteralPath (Join-Path $Lib 'references') -Filter *.md -ErrorAction SilentlyContinue |
    Where-Object { $_.LastWriteTime -ge $started } | ForEach-Object BaseName)
  $left = Waiting
  if ($learned.Count) {
    Log "learned: $($learned -join ', '); still waiting: $left"
    Notify 'Design library' ("Learned: " + ($learned -join ', ') + '. See design-library\references\')
  } else {
    Log "nothing learned (claude exit $LASTEXITCODE); still waiting: $left"
    Notify 'Design library' "Couldn't learn $names. See _temp\learn\watch.log"
  }
}

if ($Once) { if ((Waiting) -gt 0) { Learn }; Start-Sleep -Seconds 3; $icon.Dispose(); exit 0 }

# One watcher per user session.
$created = $false
$mutex = New-Object System.Threading.Mutex($true, 'Local\WebsitePipelineDesignLibraryWatch', [ref]$created)
if (-not $created) { exit 0 }
Log "watching $Lib"

$lastSizes = ''
$failedAt = @{}
while ($true) {
  try {
    $files = @(Drops)
    $sizes = ($files | ForEach-Object { "$($_.Name)=$($_.Length)" }) -join '|'
    # Act once the drop has stopped changing for one poll (a copy in progress keeps growing).
    if ($files.Count -and $sizes -eq $lastSizes) {
      if (-not $failedAt[$sizes] -or ((Get-Date) - $failedAt[$sizes]).TotalMinutes -ge 30) {
        Learn
        if (@(Drops).Count) { $failedAt[$sizes] = Get-Date }  # still there: prep couldn't read it; retry later
      }
    } elseif (-not $files.Count -and $lastSizes -eq '' -and $script:startupChecked -ne $true) {
      $script:startupChecked = $true
      if ((Waiting) -gt 0) { Learn }  # left pending by an earlier run that stopped part-way
    }
    $lastSizes = $sizes
  } catch { Log "error: $_" }
  Start-Sleep -Seconds 5
}
