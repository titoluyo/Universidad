"""Diagrama de Bode de un pasa bajo de 1.er orden: real vs. asintotico.

Magnitud (dB) y fase (grados), fc = 1 kHz, A0 = 1 (0 dB).
Ejecutar: uv run --with matplotlib --with numpy python plot_bode_primer_orden.py
"""
import numpy as np
import matplotlib.pyplot as plt

fc = 1000.0
f = np.logspace(1, 5, 2000)
H = 1.0 / (1.0 + 1j * (f / fc))          # pasa bajo 1.er orden, A0 = 1

mag = 20 * np.log10(np.abs(H))
phase = np.degrees(np.angle(H))

# Asintotas de magnitud: 0 dB hasta fc, luego -20 dB/dec
mag_asin = np.where(f <= fc, 0.0, -20 * np.log10(f / fc))

# Asintotas de fase: 0 deg hasta fc/10, -90 deg desde 10 fc, recta intermedia
phase_asin = np.clip(-45 * np.log10(f / fc) - 45, -90, 0)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6.5), sharex=True)

ax1.semilogx(f, mag, lw=2, label="Real")
ax1.semilogx(f, mag_asin, "k--", lw=1.3, label="Asíntotas")
ax1.axhline(-3, color="gray", ls=":", lw=1)
ax1.axvline(fc, color="gray", ls=":", lw=1)
ax1.text(11, -3 + 0.7, "-3 dB", color="gray")
ax1.text(1.1 * fc, 3, r"$f_c = 1\,$kHz", color="gray")
ax1.set_ylabel(r"$|H(f)|$  (dB)")
ax1.set_title("Bode — pasa bajo de 1.er orden  (−20 dB/década)")
ax1.set_ylim(-42, 8)
ax1.grid(True, which="both", ls=":", alpha=0.5)
ax1.legend(loc="lower left")

ax2.semilogx(f, phase, lw=2, color="tab:orange", label="Real")
ax2.semilogx(f, phase_asin, "k--", lw=1.3, label="Asíntotas")
ax2.axhline(-45, color="gray", ls=":", lw=1)
ax2.axvline(fc, color="gray", ls=":", lw=1)
ax2.text(11, -45 + 3, r"$-45°$", color="gray")
ax2.set_ylabel(r"Fase  $\phi(f)$  (°)")
ax2.set_xlabel("Frecuencia  f  (Hz)")
ax2.set_ylim(-100, 10)
ax2.set_yticks([0, -45, -90])
ax2.grid(True, which="both", ls=":", alpha=0.5)
ax2.legend(loc="lower left")

fig.tight_layout()
fig.savefig("attachments/bode_primer_orden.png", dpi=130)
print("Guardado: attachments/bode_primer_orden.png")
