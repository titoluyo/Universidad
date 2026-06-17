"""Distribución de corriente de polarización con un banco de espejos.

Una sola corriente de referencia I_REF genera varias corrientes de bias
escaladas por la relación de áreas (BJT) o de tamaños W/L (MOSFET) de cada
transistor de salida. Ilustra por qué un único espejo polariza todo el chip.

Ejecutar:  uv run --with matplotlib --with numpy python plot_polarizacion_espejos.py
"""
import numpy as np
import matplotlib.pyplot as plt

I_REF = 100.0  # uA, corriente de referencia única

# (etiqueta de la etapa, relación de áreas m = A_salida / A_referencia)
etapas = [
    ("Ref\n(diodo)", 1.0),
    ("Etapa 1\nm=1", 1.0),
    ("Etapa 2\nm=2", 2.0),
    ("Etapa 3\nm=0.5", 0.5),
    ("Cola par dif.\nm=4", 4.0),
]
labels = [e[0] for e in etapas]
m = np.array([e[1] for e in etapas])
corrientes = I_REF * m

colores = ["tab:grey"] + ["tab:blue"] * (len(etapas) - 1)

fig, ax = plt.subplots(figsize=(8.5, 5))
barras = ax.bar(labels, corrientes, color=colores, edgecolor="black", alpha=0.85)

for b, val, mm in zip(barras, corrientes, m):
    ax.text(b.get_x() + b.get_width() / 2, val + 8,
            f"{val:.0f} µA\n($mI_{{REF}}$, m={mm:g})",
            ha="center", va="bottom", fontsize=9)

ax.axhline(I_REF, color="tab:green", ls="--", lw=1.2)
ax.text(len(etapas) - 0.4, I_REF + 6, "$I_{REF}=100\\ \\mu A$",
        color="tab:green", ha="right")

ax.set_ylabel("Corriente de polarización [µA]")
ax.set_title("Una referencia, varias corrientes de bias escaladas (espejos)")
ax.set_ylim(0, 480)
ax.grid(True, axis="y", alpha=0.3)

fig.tight_layout()
fig.savefig("attachments/polarizacion_espejos.png", dpi=130)
print("Guardado attachments/polarizacion_espejos.png")
