"""Respuesta en magnitud (dB) de los cuatro filtros activos basicos de 2.o orden.

Misma frecuencia de corte / central f_c = 1 kHz para comparar.
Ejecutar: uv run --with matplotlib --with numpy python plot_filtros_activos.py
"""
import numpy as np
import matplotlib.pyplot as plt

fc = 1000.0          # frecuencia de corte / central (Hz)
Q = 1.0 / np.sqrt(2) # Butterworth (Q = 0.707) para pasa bajo/alto
Qbp = 3.0            # factor Q del pasa banda / supresor (banda mas estrecha)

f = np.logspace(1, 5, 2000)   # 10 Hz .. 100 kHz
s = 1j * (f / fc)             # frecuencia normalizada (jw/wc)

# Funciones de transferencia normalizadas de 2.o orden
H_lp = 1.0 / (s**2 + s / Q + 1.0)            # pasa bajo
H_hp = s**2 / (s**2 + s / Q + 1.0)           # pasa alto
H_bp = (s / Qbp) / (s**2 + s / Qbp + 1.0)    # pasa banda
H_bs = (s**2 + 1.0) / (s**2 + s / Qbp + 1.0) # supresor de banda (notch)


def dB(H):
    return 20.0 * np.log10(np.abs(H))


fig, ax = plt.subplots(figsize=(9, 5.2))
ax.semilogx(f, dB(H_lp), label="Pasa bajo", lw=2)
ax.semilogx(f, dB(H_hp), label="Pasa alto", lw=2)
ax.semilogx(f, dB(H_bp), label="Pasa banda (Q=3)", lw=2)
ax.semilogx(f, dB(H_bs), label="Supresor de banda (Q=3)", lw=2)

ax.axhline(-3, color="gray", ls="--", lw=1)
ax.axvline(fc, color="gray", ls=":", lw=1)
ax.text(1.05 * fc, 2, r"$f_c = 1\,$kHz", color="gray")
ax.text(11, -3 + 0.6, "-3 dB", color="gray")

ax.set_xlabel("Frecuencia  f  (Hz)")
ax.set_ylabel(r"$|H(f)|$  (dB)")
ax.set_title("Filtros activos de 2.º orden — respuesta en magnitud")
ax.set_ylim(-40, 8)
ax.grid(True, which="both", ls=":", alpha=0.5)
ax.legend(loc="lower center", ncol=2)

fig.tight_layout()
fig.savefig("attachments/filtros_activos_respuesta.png", dpi=130)
print("Guardado: attachments/filtros_activos_respuesta.png")
