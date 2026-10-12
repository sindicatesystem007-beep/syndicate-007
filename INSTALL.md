# Safe local run

Copy/extract only RELEASE_MANIFEST.json allowlisted files to an empty directory.
Do not copy a private checkout or .git history. Open demo.html directly: static,
JavaScript-free HTML, no server/network/storage needed.

Optional Python 3.10+: `python demo_runner.py`; no requirements or package install.
No real credentials, services or production API. Never run private tooling from this
snapshot. Windows/macOS/Linux with an existing Python/browser are sufficient.

No production install command is promised: this distribution is documentation/demo,
not the private application. No files are written by the runner.
