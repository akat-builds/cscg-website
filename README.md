# Carolina Sports Consulting Group — website

Static redesign of carolinasportsconsultinggroup.com. No framework, no dependencies.

## How it's organized

- `src/data.py` — **all site content**: people, bios, logos, services, FAQ, apply-form link. Edit this to update the roster each semester.
- `src/build.py` — page templates; generates every page into `dist/`.
- `src/styles.css`, `src/main.js` — design and interactions (copied into `dist/` on build).
- `dist/` — the built site Vercel serves.

## Making a change

```bash
python3 src/build.py          # rebuilds dist/
python3 -m http.server -d dist 8000   # preview at http://localhost:8000
```

Commit and push to `main`; Vercel rebuilds and redeploys automatically (it runs `python3 src/build.py`, and falls back to the committed `dist/` if Python isn't available).

## Common edits

- **New member:** add a row to `EXEC`, `CDP`, or a team in `PROJECTS` in `src/data.py`. Headshot = the Sanity image id, or swap in any image URL.
- **New project team:** add a `(client name, logo, [members])` entry to `PROJECTS`.
- **Application link:** `APPLY_FORM` in `src/data.py`.
- **Contact form:** currently display-only (`main.js` shows a note on submit). Point it at Formspree or similar to collect messages.

Images are loaded from the original site and the Sanity CDN.
