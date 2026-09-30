# METHOD — from zero to hero (reproducible)

## 0. Question
Can Taylor Ch.1-12 (1997) survive 2026 checks? Four falsifiable hypotheses:
H1 Bogue bias ~8% alite; H2 C-S-H ~1.75 Q0→Q1→Q2; H3 SCM discontinuity; H4 clinker-factor CO2.

## 1. Search protocol (one-at-a-time, voting)
- Exa `websearch` first (Bogue/QXDA, C-S-H NMR, LC3 CO2), 429 backoff 5s→10s×3, fallback `webfetch lite.duckduckgo`.
- Then one-at-a-time: `free-search search` (Kaggle concrete), `openresearch web_search/news/openalex/hacker_news`,
  `paper-search search_papers + search_arxiv`, `duckduckgo_search`, `agent-reach_search web`,
  `gitmcp search_generic_documentation`, `kaggle search_everything + discussions_search`,
  `gsd_websearch`, `superpowers semantic_search_skills` — all different keywords.
- Rule: no file edit without a source + live-data probe. All votes kept incl. negatives.

## 2. Experiments → benchmarks/*.json
- `01_bogue_verification.py`: Bogue eqs (CaO-0.7SO3-free_lime) on `data/sample_clinker.csv` → `benchmarks/bogue.json` + QXDA proxy (+8%).
- `02_hydration_benchmark.py`: thresholds H2a-H2f (LF-NMR 2026 C0.9SH3.65 vs C2.0SH4.53; DNP MCL 2.6→4.2) → `benchmarks/hydration.json`.
- `03_hidden_patterns.py`: UCI subset `data/sample_concrete.csv` → w/c corr, linear R2, coefs + H3/H4 proxies → `benchmarks/hidden_patterns.json`. Tries live UCI probe, logs fallback.

## 3. Verify
```bash
docker compose config
pip install -r requirements.txt
python experiments/01_bogue_verification.py
python experiments/02_hydration_benchmark.py
python experiments/03_hidden_patterns.py
cat benchmarks/*.json
```
Live full data: UCI 1030 via https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength + Kaggle mirrors (see VALIDATION.md). Rietveld/NMR/MIP-He require labs — logged as limits, not claimed.

## 4. Publish
`papers/outline.md` → journal paper; keep negatives; timestamps+sources in every JSON.
