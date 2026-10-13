<#
  Creates (or reopens) a client website project from the pipeline template.

    scaffold.ps1                       asks for the business name, creates <workspace>\Concept Websites\<Name> Website
                                       (<workspace> = Claude Workspace, the folder that holds Workflow and Pipeline\)
    scaffold.ps1 -Name "Joe's HVAC"    same, without the prompt
    scaffold.ps1 -Target <dir> -NoLaunch   scaffold into an existing folder (used by /website)

  Never overwrites existing files. Without -NoLaunch it opens the brief form (brief-form\, an Edge
  app window that edits BRIEF.md and takes client files), then on "Start building" starts Claude
  Code with /website in the project folder, in auto permission mode (a safety classifier approves
  routine commands; risky ones still ask). Without Python or the form it falls back to Notepad.
#>
param(
  [string]$Name,
  [string]$Target,
  [switch]$NoLaunch
)
$ErrorActionPreference = 'Stop'
$template = Join-Path $PSScriptRoot 'template'
# The workspace is two levels above the real pipeline folder (Claude Workspace\Workflow and Pipeline\website-pipeline).
# Launchers call this script through the ~\.claude\skills\website junction, so resolve that first.
$pipeline = Get-Item $PSScriptRoot
if ($pipeline.LinkType) { $pipeline = Get-Item @($pipeline.Target)[0] }
$workspace = $pipeline.Parent.Parent.FullName

if (-not $Target) {
  if (-not $Name) { $Name = (Read-Host 'Business name').Trim() }
  if (-not $Name) { Write-Host 'No name given.'; exit 1 }
  $safe = ($Name -replace '[\\/:*?"<>|]', '').Trim()
  $concepts = Join-Path $workspace 'Concept Websites'
  New-Item -ItemType Directory -Force -Path $concepts | Out-Null
  $Target = Join-Path $concepts "$safe Website"
}

$resuming = Test-Path (Join-Path $Target 'PROJECT.md')
if ($resuming) {
  Write-Host "Existing project found: $Target (resuming)"
} else {
  New-Item -ItemType Directory -Force -Path $Target | Out-Null
  # /E recurse, /XC /XN /XO never overwrite existing files, /XD skip scratch folders left in the template
  robocopy $template $Target /E /XC /XN /XO /XD _temp qa dist __pycache__ /NFL /NDL /NJH /NJS /NP | Out-Null
  if ($LASTEXITCODE -ge 8) { Write-Host "Copy failed (robocopy $LASTEXITCODE)"; exit 1 }
  $global:LASTEXITCODE = 0
  if ($Name) {
    $brief = Join-Path $Target 'BRIEF.md'
    $text = [IO.File]::ReadAllText($brief) -replace '(?m)^Business name:.*$', "Business name: $Name"
    [IO.File]::WriteAllText($brief, $text, (New-Object Text.UTF8Encoding $false))
  }
  # Every site is a git repo from the start: phases commit as they finish and a redesign tags the old version.
  # A redesign keeps its .git (only the files were archived), so it continues the same history.
  if ((Get-Command git -ErrorAction SilentlyContinue) -and -not (Test-Path (Join-Path $Target '.git'))) {
    git -C $Target init -q -b main
    git -C $Target config core.autocrlf false
    git -C $Target add -A
    git -C $Target commit -q -m 'Scaffold from the pipeline template'
    $global:LASTEXITCODE = 0
  }
  Write-Host "Created $Target"
}

if ($NoLaunch) { exit 0 }

if (-not $resuming) {
  # Brief form app window (brief-form\brief_form.py): exit 0 = Start building, 3 = closed for later,
  # anything else = it couldn't run, so fall back to Notepad + Explorer.
  $form = Join-Path $PSScriptRoot 'brief-form\brief_form.py'
  $code = 1
  if ((Get-Command python -ErrorAction SilentlyContinue) -and (Test-Path $form)) {
    Write-Host ''
    & python $form $Target
    $code = $LASTEXITCODE
  }
  if ($code -eq 3) {
    Write-Host ''
    Write-Host '  Brief saved. Run New Website again with the same name to pick up where you left off.'
    exit 0
  }
  if ($code -ne 0) {
    Start-Process notepad.exe (Join-Path $Target 'BRIEF.md')
    Start-Process explorer.exe (Join-Path $Target 'client-assets')
    Write-Host ''
    Write-Host '  1. Fill in what you know in BRIEF.md (all optional) and save it.'
    Write-Host '  2. Drop client photos/logo into client-assets\'
    Write-Host ''
    Read-Host '  Press Enter to start Claude (Ctrl+C to stop here)' | Out-Null
  }
}
Set-Location $Target
claude --permission-mode auto '/website'
