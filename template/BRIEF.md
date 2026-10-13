# Brief

Fill in what you know and leave the rest blank. Claude works out everything else from links and photos.
Drop client photos, logos and screenshots into `client-assets/`.

Project type: sample           <!-- sample = portfolio piece (Claude invents missing details) · client = real business (facts only) -->

Business name:
What they do (one line):
Location / service area:
Phone:
Email:
Address:
Hours:
Links (existing site, Google Business Profile, Facebook, Instagram):

Who the customers are:
What makes them different (owner, history, real work, how they do it):
Pages needed (blank = Claude decides):
Main thing visitors should do (call / quote / book / visit):
Form endpoint:                 <!-- blank = demo mode (listed at handoff) · netlify (Netlify Forms; needs Deploy host: netlify) · web3forms:<access key> (free; the inbox owner gets the key at web3forms.com) · a Formspree URL -->
Online booking link (Calendly / Cal.com, optional):

Must have:
Must avoid:
Style references (links, or file names in client-assets/):

## Pre-answers (so Claude doesn't stop to ask)

Deploy preview: yes            <!-- noindex preview when the build passes QA -->
Deploy host: cloudflare        <!-- cloudflare (Workers static assets, ex-Pages: unlimited free bandwidth) · netlify -->
Use stock photos for gaps: yes
AI image prompts: no           <!-- yes = write image-generation prompts for the gaps instead of stock -->
GSAP motion: no                <!-- no = light reveals and parallax only · yes = 1–3 signature scroll moments with GSAP (pinned story, split-text headline, horizontal gallery, animated filter, line-and-nodes trace, sticker badge); name them under Must have, or Claude picks · advanced = a full motion system like an award-site build (intro loader, one animated scene behind the page that morphs per section, line-by-line text reveals, smooth wheel scrolling, glows); name a reference site under Style references, or Claude picks -->
Pause for direction review: no <!-- yes = stop after the homepage so you can review it -->
