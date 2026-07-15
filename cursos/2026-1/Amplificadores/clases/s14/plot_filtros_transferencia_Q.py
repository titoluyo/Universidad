"""Pasa bajo de 2.o orden: efecto del factor Q sobre la respuesta en magnitud.

Muestra como al subir Q los polos se acercan al eje jw y aparece el pico de
resonancia; Q = 0.707 (Butterworth) es la maxima planicie sin pico.
Ejecutar: uv run --with matplotlib --with numpy python plot_filtros_transferencia_Q.py
"""
import numpy as np
import matplotlib.pyplot as plt

f0 = 1000.0                  # frecuencia natural (Hz)
f = np.logspace(1, 5, 2000)
w = f / f0                   # frecuencia normalizada w/w0
s = 1j * w

Qs = [0.5, 0.707, 1.0, 2.0, 5.0]

fig, ax = plt.subplots(figsize=(9, 5.2))
for Q in Qs:
    H = 1.0 / (s**2 + s / Q + 1.0)        # pasa bajo 2.o orden normalizado
    label = f"Q = {Q:g}" + ("  (Butterworth)" if abs(Q - 0.707) < 1e-2 else "")
    ax.semilogx(f, 20 * np.log10(np.abs(H)), lw=2, label=label)

ax.axhline(-3, color="gray", ls="--", lw=1)
ax.axvline(f0, color="gray", ls=":", lw=1)
ax.text(1.05 * f0, -22, r"$f_0 = 1\,$kHz", color="gray")
ax.text(11, -3 + 0.6, "-3 dB", color="gray")

ax.set_xlabel("Frecuencia  f  (Hz)")
ax.set_ylabel(r"$|H(f)|$  (dB)")
ax.set_title("Pasa bajo de 2.º orden — efecto del factor Q")
ax.set_ylim(-40, 18)
ax.grid(True, which="both", ls=":", alpha=0.5)
ax.legend(loc="lower left")

fig.tight_layout()
fig.savefig("attachments/filtros_transferencia_Q.png", dpi=130)
print("Guardado: attachments/filtros_transferencia_Q.png")
