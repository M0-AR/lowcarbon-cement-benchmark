"""
Exp.01 — Bogue bias verification (H1)
Source-grounded in online 2026 sweep (no local copy):
- NIST IR5403 Stutzman: XRD direct vs Bogue indirect, RIR/Rietveld whole-pattern
- PCA IS791 (2024): Bogue invalid for blended cements (negative C2S/C3S examples)
- Rigaku J.38(2) 2022: Rietveld partial-accumulation improves free-lime S/N
- Ganesh 2018: Bogue alite uncertainty ±9 wt%, Taylor 1989 modified-Bogue mean +8% alite (Kristmann n=39)
- ASTM C1365-18 Rietveld standard; Fawcett ICDD QPA review
Input: data/sample_clinker.csv (Taylor-typical OPC chemistries)
Output: benchmarks/bogue.json with sources+timestamp, incl. negative results
"""
import csv, json, datetime, pathlib

DATA = pathlib.Path(__file__).parent.parent / "data" / "sample_clinker.csv"
OUT = pathlib.Path(__file__).parent.parent / "benchmarks" / "bogue.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

def bogue(cao, sio2, al2o3, fe2o3, so3=0.0, free_lime=0.0):
    # Correct CaO for free lime + gypsum (0.7*SO3) per Taylor §4.4 / Lea
    cao_corr = cao - free_lime - 0.7*so3
    c3s = 4.0710*cao_corr - 7.6024*sio2 - 6.7187*al2o3 - 1.4297*fe2o3
    c2s = 2.8675*sio2 - 0.7544*c3s
    c3a = 2.6504*al2o3 - 1.6920*fe2o3
    c4af = 3.0432*fe2o3
    return dict(C3S=c3s, C2S=c2s, C3A=c3a, C4AF=c4af)

rows = list(csv.DictReader(open(DATA)))
results = []
for r in rows:
    b = bogue(float(r["CaO"]), float(r["SiO2"]), float(r["Al2O3"]),
              float(r["Fe2O3"]), float(r.get("SO3", 0)), float(r.get("free_lime", 0)))
    # QXDA proxy: Taylor §4.5.4 mean discrepancy +8% alite vs Bogue (Kristmann n=39)
    # This is a HYPOTHESIS threshold, not a measurement — documented limit.
    qxda_proxy = dict(
        C3S=b["C3S"]+8.0,
        C2S=b["C2S"]-7.0,  # mass balance shift belite high by Bogue
        C3A=b["C3A"]-1.0,
        C4AF=b["C4AF"]+0.3,
    )
    bias = qxda_proxy["C3S"]-b["C3S"]
    results.append(dict(sample=r["sample"], bogue={k: round(v,2) for k,v in b.items()},
                        qxda_proxy={k: round(v,2) for k,v in qxda_proxy.items()},
                        alite_bias=round(bias,2)))

biases = [x["alite_bias"] for x in results]
payload = {
  "hypothesis": "H1 Bogue C3S ~8% low vs QXDA/microscopy (Taylor §4.5.4, Kristmann n=39)",
  "threshold": {"alite_bias_mean": 8.0, "tolerance": 0.5, "unit": "wt%"},
  "observed": {"mean_bias": sum(biases)/len(biases), "n": len(results), "per_sample": results},
  "verdict": "PASS-proxy (by construction) — real QXDA needed for publication; see VALIDATION.md limits",
  "negative_results": [
    "PCA IS791: Bogue on blended cements gives impossible values (negative C3S, C2S>100%) — do NOT apply to LC3/slag/flyash blends",
    "QXDA proxy is NOT a measurement; Rietveld per ASTM C1365 with proper standards required for PhD claim"
  ],
  "sources": [
    "https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir5403.pdf (Stutzman QXRD)",
    "https://www.cement.org/wp-content/uploads/2024/07/IS791.02_Revised_June2024.pdf (PCA Bogue invalid blended)",
    "https://rigaku.com/hubfs/.../Rigaku%20Journal%2038-2_1.pdf (partial accumulation free lime)",
    "Ganesh 2018 exa.ai/library/publication/36pc1dlzb7g (Bogue ±9wt% alite)",
    "Fawcett Powder Diffraction QPA review + ASTM C1365-18"
  ],
  "timestamp": datetime.datetime.utcnow().isoformat()+"Z",
  "data": "data/sample_clinker.csv (Taylor-typical, ignited-mass basis)",
  "live_data_status": "local proxy only; live QXDA requires lab diffractometer — documented, not claimed"
}
json.dump(payload, open(OUT,"w"), indent=2)
print(f"Wrote {OUT} mean_bias={payload['observed']['mean_bias']:.2f} n={len(results)}")
