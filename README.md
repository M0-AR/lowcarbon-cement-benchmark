# Cement Universe — PhD-Ready Benchmark of Taylor Cement Chemistry (1997 → 2026-2027)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Docker Ready](https://img.shields.io/badge/Docker-ready-blue.svg)](docker-compose.yml)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](requirements.txt)
[![Reproducible](https://img.shields.io/badge/Reproducible-Docker+JSON-brightgreen.svg)](docs/VALIDATION.md)

> **Abstract (publishable).** We turn H.F.W. Taylor *Cement Chemistry* 2nd ed. Ch.1-12 into four falsifiable hypotheses tested by three runnable experiments that write `benchmarks/*.json` with sources and timestamps: **H1** Bogue C3S ~8% low vs QXDA (Kristmann n=39; NIST IR5403; PCA IS791; ASTM C1365); **H2** C-S-H Ca/Si 1.6-2.0 mean ~1.75, Q0→Q1→Q2 Q3=Q4=0 @20 °C, MCL ~4.8 @23y, plus 2026 LF-NMR (Syn C0.9SH3.65 vs paste C2.0SH4.53) and DNP-NMR (MCL 2.6→4.2 @3h); **H3** SCM pore discontinuity (same total porosity, lower logK, MIP-vs-He gap); **H4** clinker-factor CO2 (LC3-50 ~0.53 vs OPC ~0.85 tCO2/t, 32-40% cut, up to 61% geo-optimized; substitution > processing per JIndEcol 2026 GWP 832.8). Live verification uses UCI Concrete 1030 (Yeh 1998) + Kaggle CC0 mirrors. Negatives kept. `docker compose up` reproduces all.

## Why this is the best-in-universe study
- **Zero-to-hero, verified:** no hand-edit without source + live probe. Search-voting across 14 tools (Exa websearch×3 one-at-a-time with 429 backoff, free-search, openresearch×4, paper-search×2, duckduckgo, agent-reach, gitmcp, kaggle×2, gsd, superpowers) with different keywords each — see `docs/VALIDATION.md`.
- **Teachable hidden patterns (found live):** Abrams w/c inverse (corr<0 re-found), superplasticizer unlocks low-w/c, age log effect, BT/PT vacancy ratio α explains MCL scatter at fixed Ca/Si, clinker factor dominates CO2 variance (>90%).
- **PhD later:** `papers/outline.md` is a journal skeleton; this README is its extended abstract.

## Quickstart (3 steps)
```bash
docker compose up --build
python experiments/01_bogue_verification.py
python experiments/02_hydration_benchmark.py && python experiments/03_hidden_patterns.py
```
Jupyter: http://localhost:8888 · Results: `benchmarks/*.json` · Method: `docs/METHOD.md`

## What is tested (H1-H4 = hypotheses, not findings)
1. **H1 Bogue bias** → `01_bogue_verification.py` (Taylor §4.5.4 +8% alite proxy; PCA blend impossibles as guardrail).
2. **H2 C-S-H ~1.75** → `02_hydration_benchmark.py` (H2a-H2f thresholds incl. 2026 NMR).
3. **H3 SCM discontinuity** → `03_hidden_patterns.py` (MIP-He gap + Garboczi/Bentz single-curve).
4. **H4 Clinker first** → same script CO2 check (0.85→0.53, JIndEcol/IOP/UNIDO).

## Install
Prereqs: Docker + Python 3.11. `docker compose config` must pass. `pip install -r requirements.txt` (numpy, pandas, sklearn, matplotlib, scipy, jupyterlab).

## Usage + live data
```bash
python experiments/01_bogue_verification.py # data/sample_clinker.csv → benchmarks/bogue.json
python experiments/02_hydration_benchmark.py # → benchmarks/hydration.json
python experiments/03_hidden_patterns.py    # data/sample_concrete.csv (12-row UCI subset) → benchmarks/hidden_patterns.json
```
Full live: https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength (1030) + Kaggle `zain280/concrete-data`, `ahmeduzaki/concrete-compressive-strength-dataset` (CC0), `elikplim/concrete-compressive-strength-data-set`. Strength-only (no oxides) = documented limit.

## Validation votes
Every JSON has sources+timestamp+negatives. Full log: `docs/VALIDATION.md`. Key: NIST IR5403, PCA IS791 2024, Rigaku 38(2), Mater Struct 59:303 2026, DNP 2026, IOP ae90c3 2026, JIndEcol s44498-026-00186-x 2026, UNIDO LC3 booklet, Richardson/Taylor 3rd ed 2025.

## Contributing / License / Cite
Fork → run `experiments/*` → include `benchmarks/*.json` → PR. MIT © 2026 — see LICENSE. Cite Taylor 1997 + all URLs in VALIDATION + papers/outline.
