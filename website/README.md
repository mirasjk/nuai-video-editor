# NU AI product website

Dependency-free Turkish and English product pages for the macOS application.

## Update the content

Edit the language dictionaries or template in build.py, then regenerate both pages:

    python3 website/build.py

From the repository root, preview locally:

    python3 -m http.server 4173 --directory website

The Turkish page is at / and the English page is at /en/.
The gallery uses real application screenshots from docs/screenshots.
The interactive transcript in the hero is explicitly labeled as a workflow illustration.

## Deploy with Coolify

Create an application from this public repository. Select Static as the build pack,
set Base directory to /website and Publish directory to /.
The site consists of finished HTML, CSS, JavaScript and image assets; no Node build is needed.

The download buttons link to the existing v0.1.0 Apple Silicon DMG on GitHub Releases.
Update the download URL and version metadata in build.py when a new binary is released.
