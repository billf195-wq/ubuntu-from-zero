# Ubuntu From Zero

**Quick share links (email-ready):** [LINKS.md](LINKS.md)


Beginner → novice Ubuntu tutorial for Windows switchers (Ubuntu 24.04 / 26.04 GNOME).

**Two deliverables in this folder:**

1. **Shareable static HTML** — open `html/index.html` offline (relative paths; zip-friendly).
2. **Local Tkinter app** — browse lessons, search, open the full HTML lesson in your browser.

Orange accent, Light/Dark themes (HTML respects system preference + toggle; app defaults to dark with orange accent).

## Quick start (on this machine / the box)

```bash
cd /workspace/ubuntu-from-zero   # or ~/Apps/ubuntu-from-zero after install
./run.sh
```

Or:

```bash
python3 app.py
```

HTML only:

```bash
xdg-open html/index.html
# or open html/index.html in Firefox/Chrome
```

Check Python syntax:

```bash
python3 -m py_compile app.py lessons.py
```

## Suggested install on Bill’s GTR

```bash
mkdir -p ~/Apps
cp -a /path/to/ubuntu-from-zero ~/Apps/ubuntu-from-zero
cd ~/Apps/ubuntu-from-zero
chmod +x run.sh
# Optional launcher:
cp ubuntu-from-zero.desktop ~/.local/share/applications/
# Edit the desktop file Exec/Path to the real folder if needed, e.g.:
# Exec=/home/bill/Apps/ubuntu-from-zero/run.sh
# Path=/home/bill/Apps/ubuntu-from-zero
```

## Zip for sharing (HTML + media)

```bash
cd /path/to/ubuntu-from-zero
zip -r ubuntu-from-zero-html.zip html media MEDIA.md README.md
```

Recipients unzip and open `html/index.html`. No server required.

## Layout

```
ubuntu-from-zero/
  app.py                 # Tkinter UI
  lessons.py             # Lesson catalog for the app
  run.sh                 # Launcher
  ubuntu-from-zero.desktop
  README.md
  MEDIA.md               # GTR screenshot/video capture checklist
  html/
    index.html
    css/style.css
    js/app.js
    lessons/*.html       # 17 lessons
  media/
    images/              # SVG placeholders → replace on GTR
    videos/              # 6 short placeholder WebMs + posters
```

## Lessons (17)

**Beginner:** Welcome, Desktop tour, Files, Installing apps, Updates, Wi‑Fi/BT/Displays, Screenshots & shortcuts  

**Getting comfortable:** Terminal, sudo, Browser/email/printers, Backups, Troubleshooting  

**Novice:** Flatpak vs apt vs Snap, Steam/Proton, Permissions/Disks, Customize look, Next steps  

## Media

Placeholders ship so the HTML looks complete. Capture real shots on the GTR using **MEDIA.md** (exact filenames and six video slots).

## Requirements

- Python 3 + Tk (`python3-tk` on Ubuntu if missing: `sudo apt install python3-tk`)
- A browser for full lessons
- No pip packages required

## Credit

Developed by Bill Foster.

## Support / donations

Optional — thank you if you tip via PayPal:

[Donate with PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=billf195%40yahoo.com&currency_code=USD&item_name=Support%20Bill%20Foster%20apps)

## Related

- [Total IPTV Pro](https://github.com/billf195-wq/total-iptv-pro) — Android TV/phone + Desktop player (also by Bill Foster)

