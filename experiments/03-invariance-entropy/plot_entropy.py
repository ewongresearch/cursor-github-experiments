from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from entropy import demo_system, invariance_entropy_continuous, invariance_entropy_discrete

DOCS_DIR = Path(__file__).resolve().parents[2] / "docs"

def build_chart(output_dir: Path = DOCS_DIR) -> dict:
    A = demo_system()
    eigenvalues = np.linalg.eigvals(A)
    h_continuous = invariance_entropy_continuous(A)
    h_discrete = invariance_entropy_discrete(A)
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.axhline(0, color="#888", linewidth=0.8)
    ax.axvline(0, color="#888", linewidth=0.8)
    ax.scatter(np.real(eigenvalues), np.imag(eigenvalues), s=120, c="#2563eb")
    ax.set_title("Invariance Entropy - Demo Linear System")
    ax.set_xlabel("Re(lambda)")
    ax.set_ylabel("Im(lambda)")
    ax.grid(True, alpha=0.25)
    ax.text(0.02, 0.98, f"Continuous: {h_continuous:.4f}\nDiscrete: {h_discrete:.4f}",
            transform=ax.transAxes, va="top")
    chart_path = output_dir / "entropy-chart.png"
    fig.tight_layout()
    fig.savefig(chart_path, dpi=144)
    plt.close(fig)

    summary = {"continuous": h_continuous, "discrete": h_discrete}
    (output_dir / "entropy-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Invariance Entropy</title></head>
<body style="font-family:system-ui;max-width:900px;margin:2rem auto">
<h1>Experiment 03: Invariance Entropy</h1>
<p>Continuous: {h_continuous:.4f} | Discrete: {h_discrete:.4f}</p>
<img src="entropy-chart.png" style="max-width:100%"></body></html>"""
    (output_dir / "index.html").write_text(html, encoding="utf-8")
    return {"continuous": h_continuous, "discrete": h_discrete, "chart": str(chart_path)}

if __name__ == "__main__":
    result = build_chart()
    print(f"Chart: {result['chart']}")
    print(f"Continuous: {result['continuous']:.4f}, Discrete: {result['discrete']:.4f}")
