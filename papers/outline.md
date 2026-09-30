# PhD Paper Outline — Cement Universe (publishable skeleton)

Title: Falsifiable re-checks of Taylor Cement Chemistry (1997) with 2026 open data: Bogue bias, C-S-H nanostructure, SCM discontinuity, clinker-factor CO2

Authors: [You] + contributors (this repo = supplementary material)

Abstract: Same as README abstract + 4 verdicts + live-data limits.

1. Intro: Taylor spine + Richardson 3rd ed 2025 + why 2026 re-check (NEP-MLP, LF-NMR, LCC).
2. Background: alite/belite/aluminate/ferrite; Bogue vs QXDA (NIST, PCA, ASTM C1365); C-S-H T/J; SCM pore; LC3 LCA.
3. Methods: docs/METHOD.md search-voting + 3 experiments → JSON with timestamps; UCI 1030 + Kaggle mirrors; negative-results kept.
4. Results:
 - H1: proxy +8% alite, PCA impossible-values for blends.
 - H2: thresholds H2a-H2f match literature + 2026 LF/DNP NMR numbers.
 - H3: w/c negative corr, superplasticizer leverage, age log; MIP-He gap theory.
 - H4: 0.85→0.53 tCO2/t LC3-50, substitution dominates (>90% variance).
5. Hidden patterns (teachable):
 - Abrams w/c law re-found live (corr<0).
 - Superplasticizer unlocks low-w/c (coef>0).
 - Age log effect (365d>28d same mix).
 - BT/PT vacancy ratio alpha explains MCL scatter at fixed Ca/Si.
 - Clinker factor > processing (JIndEcol).
6. Threats: n=12 subset; proxy QXDA; no lab NMR/MIP; mass-basis CO2.
7. Conclusion + future: full UCI + Rietveld + NMR + MIP-He + field LC3.

References: full URLs in docs/VALIDATION.md (NIST, PCA, Rigaku, Springer 2026×2, IOP 2026, JIndEcol 2026, UNIDO, UCI, Kaggle, Richardson).

Reproduce: docker compose up --build; python experiments/*.py; benchmarks/*.json.
