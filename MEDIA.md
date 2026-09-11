# MEDIA capture checklist (GTR)

Replace placeholders under `media/images/` and `media/videos/` with real captures from Bill’s GTR running Ubuntu 24.04 or 26.04 GNOME. Keep **the same filenames** so HTML and the app keep working.

## General tips

- Resolution: 1920×1080 (or native laptop res); export PNG for UI shots, WebM or MP4 for clips.
- Hide personal info (email, notifications, wallpaper photos of people).
- Prefer a clean dock: Files, Firefox, Terminal, Settings, App Center.
- Dark Yaru + orange accent looks consistent with this project (Settings → Appearance).
- Short clips: 15–45 seconds. No need for voiceover if on-screen steps are clear (optional quiet mic).

## Images — replace these SVGs with PNG/JPG (same basename OK if you update HTML, or overwrite as `.svg` replacements by changing refs — easiest: export as PNG and update lesson `src` OR keep name and convert: `foo.png` then edit HTML).

**Recommended:** save as PNG using the **same basename** and update the lesson HTML `src` from `.svg` to `.png`, *or* export SVG screenshots. Simplest workflow on GTR:

1. Capture with PrtSc → save into `~/Apps/ubuntu-from-zero/media/images/`
2. Rename to match the list below (overwrite the placeholder file name stem).

### Required / strongly recommended shots

| File | What to capture |
|------|-----------------|
| `hero-ubuntu.svg` | Clean desktop overview (Activities closed), dock visible |
| `01-welcome.svg` | Same or login/welcome feel |
| `activities-overview.svg` | Activities overview with search |
| `dock.svg` | Close-up of left dock with favorites |
| `top-bar.svg` | Top bar / system menu open |
| `files-home.svg` | Files app on Home |
| `03-files.svg` | Files with sidebar (Home, Downloads, Trash) |
| `app-center.svg` | App Center search results |
| `04-install-apps.svg` | App install progress or listing |
| `software-updater.svg` | Software Updater window |
| `05-updates.svg` | Updater or terminal apt upgrade |
| `settings-wifi.svg` | Settings → Wi‑Fi |
| `06-wifi-bt-display.svg` | Displays settings |
| `screenshot-tool.svg` | Screenshot UI (PrtSc) |
| `07-screenshots.svg` | Screenshot tool + a sample shot |
| `terminal-window.svg` | Terminal with `pwd` / `ls` demo |
| `08-terminal.svg` | Terminal lesson cover |
| `password-prompt.svg` | Polkit / sudo password dialog (blur if needed) |
| `09-sudo.svg` | Cover for sudo lesson |
| `firefox.svg` | Firefox on a neutral page |
| `10-browser-email.svg` | Browser + optional Thunderbird |
| `timeshift.svg` | Timeshift main window |
| `11-backups.svg` | USB copy or Timeshift |
| `checklist.svg` | Optional annotated checklist |
| `12-troubleshoot.svg` | Network settings or updater stuck (staged) |
| `flatpak-vs-apt.svg` | App Center showing source choice if available |
| `13-package-types.svg` | Cover |
| `steam-proton.svg` | Steam Play compatibility settings |
| `14-gaming.svg` | Steam library (no private info) |
| `disks-app.svg` | GNOME Disks overview |
| `15-permissions.svg` | Users settings or `ls -l` in terminal |
| `appearance.svg` | Appearance with dark + orange accent |
| `16-customize.svg` | Wallpaper picker |
| `learning-path.svg` | Optional diagram or desktop with notes |
| `17-next-steps.svg` | Cover |
| `02-desktop.svg` | Desktop tour cover |

## Videos — six slots (already wired in HTML)

Record 15–45s WebM/MP4; overwrite these files in `media/videos/`:

| File | Capture script |
|------|----------------|
| `desktop-tour.webm` | Super → show Activities → open Settings → show system menu → back to desktop |
| `files-app.webm` | Open Files → Home → Downloads → Trash → USB if present |
| `install-app.webm` | App Center → search VLC (or similar) → show Install button (need not finish) |
| `terminal-basics.webm` | Open Terminal → `pwd` → `ls` → `cd Downloads` → `cd` |
| `updates.webm` | Open Software Updater (or show `sudo apt update` typed, don’t need full upgrade on camera) |
| `appearance.webm` | Settings → Appearance → toggle Dark → pick orange accent → change wallpaper |

Posters `*-poster.svg` can stay or be replaced with a frame grab PNG (update HTML `poster=` if you change extension).

## After capture

1. Keep relative paths; zip `html/` + `media/` for sharing.
2. Open `html/index.html` offline to spot-check images/videos.
3. Optional: compress videos with `ffmpeg -i in.webm -b:v 800k out.webm`.
