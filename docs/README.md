# BuildtheCrew PRD — GitHub Pages site

A self-contained, dependency-free static site that publishes `BuildtheCrew-PRD.md` as a clean docs-style web page.

## What's in this folder

| File | Purpose |
| --- | --- |
| `index.html` | The rendered PRD page. Open it locally in a browser to preview before publishing. |
| `BuildtheCrew-PRD.md` | The raw markdown, linked from the page footer ("View raw markdown"). |
| `.nojekyll` | Tells GitHub Pages to serve files as-is and skip Jekyll preprocessing. |
| `README.md` | This file. |

No build step, no JS bundles, no external CDNs. Light + dark theme baked in via `prefers-color-scheme`.

## Preview locally

Just open `index.html` in your browser, or run a tiny static server:

```bash
cd buildthecrew-site
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Publish on GitHub Pages — pick one of two paths

### Option A — Dedicated repo (simplest, recommended)

1. On github.com, create a **new public repo**, e.g. `buildthecrew-prd`. Don't initialize it with a README.
2. Locally, in this folder, run:
   ```bash
   git init
   git add .
   git commit -m "Initial PRD site"
   git branch -M main
   git remote add origin https://github.com/<your-username>/buildthecrew-prd.git
   git push -u origin main
   ```
3. On GitHub, go to **Settings → Pages**.
4. Under **Source**, choose **Deploy from a branch**.
5. Set **Branch** to `main` and **folder** to `/ (root)`. Click **Save**.
6. Wait ~30–60 seconds. The page banner will show your URL, e.g. `https://<your-username>.github.io/buildthecrew-prd/`.

### Option B — Drop into an existing repo's `/docs` folder

Useful if you already have a `buildthecrew` codebase and just want the PRD published from it.

1. Copy this whole folder's contents into `docs/` at the root of your repo (so you get `docs/index.html`, `docs/BuildtheCrew-PRD.md`, `docs/.nojekyll`).
2. Commit and push to `main`.
3. On GitHub, go to **Settings → Pages**.
4. **Source** = **Deploy from a branch**, **Branch** = `main`, **Folder** = `/docs`. Save.
5. Site URL: `https://<your-username>.github.io/<repo-name>/`.

## Updating the page later

If you edit the PRD markdown:

1. Update `BuildtheCrew-PRD.md` in the repo.
2. Update the matching section in `index.html` (the page renders the markdown statically — there's no live conversion).
3. `git commit` + `git push`. Pages auto-rebuilds within a minute.

If you'd prefer the markdown to be the single source of truth and the HTML to regenerate automatically, ask Claude to swap this in for a **GitHub Actions workflow** that converts `BuildtheCrew-PRD.md` → `index.html` on every push.

## Custom domain (optional)

1. Add a `CNAME` file in this folder containing only your domain, e.g. `prd.buildthecrew.com`.
2. At your DNS provider, add a `CNAME` record pointing that subdomain to `<your-username>.github.io`.
3. In **Settings → Pages**, enter the same custom domain and tick **Enforce HTTPS** once the cert provisions.

## Troubleshooting

- **Page is blank or unstyled**: Make sure `.nojekyll` made it into the repo (it's a hidden file — `git status` should show it on first commit).
- **404 after pushing**: Pages can take up to a minute on first publish. Refresh the Settings → Pages page; the banner will turn green when it's live.
- **Links to the markdown 404**: The footer links to `BuildtheCrew-PRD.md` relative to the page. Make sure that file is in the same directory as `index.html`.
