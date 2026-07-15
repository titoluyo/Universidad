"""Comparacion de formas de onda: rectificador de media onda vs onda completa.

Panel 1: entrada senoidal v_I.
Panel 2: media onda  v_O = max(v_I, 0)  (un solo semiciclo).
Panel 3: onda completa  v_O = |v_I|     (ambos semiciclos rectificados).

Se ignora la caida del diodo (modelo ideal) para resaltar la topologia.

Ejecutar:  uv run --with matplotlib python plot_rectificadores.py
"""
import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = os.path.dirname(__file__)

Vp = 10.0          # tension de pico [V]
f = 60.0           # frecuencia [Hz]
T = 1.0 / f
N = 4000
tmax = 2.0 * T
t = [i * tmax / N for i in range(N)]
ms = [ti * 1000 for ti in t]

vin = [Vp * math.sin(2 * math.pi * f * ti) for ti in t]
v_half = [v if v > 0 else 0.0 for v in vin]      # media onda
v_full = [abs(v) for v in vin]                    # onda completa

# Valores DC (promedio) teoricos
vdc_half = Vp / math.pi          # ~0.318 Vp
vdc_full = 2 * Vp / math.pi      # ~0.637 Vp

fig, axes = plt.subplots(3, 1, figsize=(9.5, 8.2), sharex=True)

# Panel 1: entrada
ax = axes[0]
ax.plot(ms, vin, color="#7f8c8d", lw=2)
ax.axhline(0, color="k", lw=0.8)
ax.set_title("Entrada — $v_I = V_p\\sin\\omega t$")
ax.set_ylabel("[V]")
ax.set_ylim(-Vp - 2, Vp + 2)
ax.grid(True, alpha=0.3)

# Panel 2: media onda
ax = axes[1]
ax.plot(ms, vin, color="#bdc3c7", lw=1, ls="--", label="entrada")
ax.plot(ms, v_half, color="#2471a3", lw=2.4, label="salida")
ax.axhline(vdc_half, color="#e67e22", lw=1.4, ls=":",
           label=f"$V_{{DC}}=V_p/\\pi={vdc_half:.2f}$ V")
ax.axhline(0, color="k", lw=0.8)
ax.set_title("Rectificador de MEDIA ONDA — $v_O=\\max(v_I,0)$  ($f_{out}=f$)")
ax.set_ylabel("[V]")
ax.set_ylim(-Vp - 2, Vp + 2)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=9, ncol=3)

# Panel 3: onda completa
ax = axes[2]
ax.plot(ms, vin, color="#bdc3c7", lw=1, ls="--", label="entrada")
ax.plot(ms, v_full, color="#c0392b", lw=2.4, label="salida")
ax.axhline(vdc_full, color="#e67e22", lw=1.4, ls=":",
           label=f"$V_{{DC}}=2V_p/\\pi={vdc_full:.2f}$ V")
ax.axhline(0, color="k", lw=0.8)
ax.set_title("Rectificador de ONDA COMPLETA — $v_O=|v_I|$  ($f_{out}=2f$)")
ax.set_ylabel("[V]")
ax.set_xlabel("tiempo [ms]")
ax.set_ylim(-Vp - 2, Vp + 2)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=9, ncol=3)

plt.tight_layout()
out = os.path.join(D, "attachments", "rectificadores_comparacion.png")
plt.savefig(out, dpi=130)
print("saved", out, "| Vdc_half =", round(vdc_half, 3), "| Vdc_full =", round(vdc_full, 3))
