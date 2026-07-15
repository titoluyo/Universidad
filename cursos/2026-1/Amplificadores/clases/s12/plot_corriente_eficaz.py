"""Valor eficaz (RMS) de una corriente senoidal.

Muestra (en unidades normalizadas a I_m):
  - i(t)/I_m            : senoide entre -1 y 1
  - (i(t)/I_m)^2        : siempre >= 0, oscila a 2w entre 0 y 1
  - media de i^2 = 1/2  : nivel promedio del cuadrado
  - I_ef/I_m = 1/sqrt2  : raiz de esa media = valor eficaz (~0.707)

Ejecutar:  uv run --with matplotlib python plot_corriente_eficaz.py
"""
import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = os.path.dirname(__file__)

f = 1.0
T = 1.0 / f
N = 4000
t = [i * (2 * T) / N for i in range(N + 1)]   # dos periodos

i_n = [math.sin(2 * math.pi * f * ti) for ti in t]      # i(t)/I_m
i2 = [v * v for v in i_n]                                 # (i(t)/I_m)^2
mean_sq = 0.5                                             # promedio de sin^2 en un periodo
i_ef = math.sqrt(mean_sq)                                # 1/sqrt(2) ~ 0.707

x = [ti / T for ti in t]  # tiempo en periodos

fig, ax = plt.subplots(figsize=(9.5, 5.4))

ax.plot(x, i_n, color="#2471a3", lw=2.2, label="$i(t)/I_m = \\sin\\omega t$")
ax.plot(x, i2, color="#c0392b", lw=2.2, label="$\\left(i(t)/I_m\\right)^2 = \\sin^2\\omega t$")

# Relleno bajo i^2 (lo que se promedia)
ax.fill_between(x, 0, i2, color="#c0392b", alpha=0.12)

# Media del cuadrado y valor eficaz
ax.axhline(mean_sq, color="#8e44ad", lw=1.6, ls="--",
           label="media de $i^2$ = $1/2$")
ax.axhline(i_ef, color="#16a085", lw=1.8, ls="-",
           label=f"$I_{{ef}}/I_m = 1/\\sqrt{{2}} \\approx {i_ef:.3f}$")

ax.axhline(0, color="k", lw=0.8)
ax.text(1.5, mean_sq + 0.02, "$\\dfrac{1}{T}\\int_0^T \\sin^2\\omega t\\,dt = \\dfrac{1}{2}$",
        color="#8e44ad", fontsize=11, va="bottom")
ax.text(1.5, i_ef + 0.02, "$I_{ef}=\\sqrt{\\text{media}}$", color="#16a085",
        fontsize=11, va="bottom")

ax.set_title("Valor eficaz (RMS) de una corriente senoidal")
ax.set_xlabel("tiempo  [periodos $T$]")
ax.set_ylabel("magnitud normalizada (a $I_m$)")
ax.set_xlim(0, 2)
ax.set_ylim(-1.15, 1.25)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=9)

plt.tight_layout()
out = os.path.join(D, "attachments", "corriente_eficaz.png")
plt.savefig(out, dpi=130)
print("saved", out, "| I_ef/I_m =", round(i_ef, 4))
