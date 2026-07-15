"""Asintotas de magnitud de los factores elementales del diagrama de Bode.

Replica el "diccionario de factores" del material del curso (todos con w0 = 1 kHz):
derivada (+20), integral (-20), 1.er orden (+/-20 con codo) y 2.o orden (+/-40 con codo).
Ejecutar: uv run --with matplotlib --with numpy python plot_bode_factores.py
"""
import numpy as np
import matplotlib.pyplot as plt

f0 = 1000.0
f = np.logspace(1, 5, 2000)
r = f / f0  # w/w0

# Asintotas (magnitud en dB)
deriv = 20 * np.log10(r)                       # (jw/w0):      +20 dB/dec
integ = -20 * np.log10(r)                      # (jw/w0)^-1:   -20 dB/dec
fo_cero = np.where(f <= f0, 0.0, 20 * np.log10(r))    # (1+jw/w0):    0 -> +20
fo_polo = np.where(f <= f0, 0.0, -20 * np.log10(r))   # (1+jw/w0)^-1: 0 -> -20
so_cero = np.where(f <= f0, 0.0, 40 * np.log10(r))    # 2.o orden:    0 -> +40
so_polo = np.where(f <= f0, 0.0, -40 * np.log10(r))   # 2.o orden^-1: 0 -> -40

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5), sharey=True)

# Izquierda: pendiente constante (cero/polo en el origen)
ax1.semilogx(f, deriv, lw=2, label=r"derivada $(jw/w_0)$  +20")
ax1.semilogx(f, integ, lw=2, label=r"integral $(jw/w_0)^{-1}$  -20")
ax1.set_title("Factores de pendiente constante")
ax1.legend(loc="upper left", fontsize=9)

# Derecha: factores con codo en w0
ax2.semilogx(f, fo_cero, lw=2, label=r"$(1+jw/w_0)$  +20")
ax2.semilogx(f, fo_polo, lw=2, label=r"$(1+jw/w_0)^{-1}$  -20")
ax2.semilogx(f, so_cero, lw=2, ls="--", label=r"2.º orden  +40")
ax2.semilogx(f, so_polo, lw=2, ls="--", label=r"2.º orden$^{-1}$  -40")
ax2.set_title("Factores de 1.er y 2.º orden (codo en $w_0$)")
ax2.legend(loc="upper left", fontsize=9)

for ax in (ax1, ax2):
    ax.axvline(f0, color="gray", ls=":", lw=1)
    ax.axhline(0, color="gray", lw=0.8)
    ax.text(1.1 * f0, -38, r"$w_0$", color="gray")
    ax.set_xlabel(r"$\log\,w$   (f, Hz)")
    ax.set_ylim(-42, 42)
    ax.grid(True, which="both", ls=":", alpha=0.5)
ax1.set_ylabel(r"$G_{dB}$")

fig.suptitle("Diagrama de Bode — diccionario de factores  ($w_0 = 1\\,$kHz)")
fig.tight_layout()
fig.savefig("attachments/bode_factores.png", dpi=130)
print("Guardado: attachments/bode_factores.png")
