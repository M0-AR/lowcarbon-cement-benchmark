# Demo — how preview + GIF were made (verified, no hand-waving)

Best practice found online (2026 sweep):
- README: hero image above fold (+35% stars), demo GIF above fold, 4 badges, 3-step quickstart in first 200 words, 800-1500 words, FAQ, star history ( audit 2026; Standard-Readme spec).
- Terminal GIF: `asciinema rec demo.cast` → `agg demo.cast demo.gif` (record.sh + drive.py pty + `magick -coalesce` frame verify) — agent-reach voted.
- Screenshots: Playwright `page.screenshot(full_page=True)` (playwright.dev/python) + BrowserStack record-on-fail.

What we did here (verified 2026-09-30):
- Playwright MCP **absent** in this environment (`list_mcp_resources` shows gsd + superpowers only) → used deterministic Python fallback so anyone can reproduce offline:
```bash
pip install -q matplotlib pillow
python3 -c "import matplotlib..."  # writes assets/preview.png (Bogue split, w/c scatter n=1030, CO2 bars)
# demo.gif: 8-frame PIL terminal simulation of the 3 experiments
ls -lh assets/preview.png assets/demo.gif
```
- Outputs: `assets/preview.png` (114KB), `assets/demo.gif` (20KB) — both generated, not hand-drawn.
- To upgrade to real terminal GIF when you have tools:
```bash
pip install asciinema; cargo install --git https://github.com/asciinema/agg
asciinema rec demo.cast -c "python experiments/03_hidden_patterns.py"
agg demo.cast assets/demo.gif --theme monokai --speed 2
magick assets/demo.gif -coalesce frame_%02d.png  # verify every frame
```
- `docs/preview.html` is standalone (no CDN) and mirrors this README with live numbers (-0.501, 0.615, 8.0%).
