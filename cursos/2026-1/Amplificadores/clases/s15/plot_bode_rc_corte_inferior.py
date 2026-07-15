"""Diagrama de Bode de la red RC de corte inferior (pasa-alto de 1.er orden).

Boylestad, cap. 9, Figs. 9.13-9.15:  Av(jw) = (jw/w1) / (1 + jw/w1),  w1 = 1/RC.
Genera bode_rc_corte_inferior.png en attachments/.

Ejecutar:  uv run --with matplotlib --with numpy python plot_bode_rc_corte_inferior.py
"""
import os
import numpy as np
import matplotlib.pyplot as plt

# --- Parametros de la red ---
R = 1e3          # 1 kOhm
C = 0.1e-6       # 0.1 uF
f1 = 1 / (2 * np.pi * R * C)   # frecuencia de corte inferior ~ 1591 Hz

# --- Respuesta en frecuencia ---
f = np.logspace(0, 6, 2000)          # 1 Hz .. 1 MHz
w_ratio = f / f1                      # w/w1 = f/f1
Av = (1j * w_ratio) / (1 + 1j * w_ratio)
mag_db = 20 * np.log10(np.abs(Av))
phase = np.degrees(np.angle(Av))

# --- Asintotas de magnitud ---
asin_low = 20 * np.log10(w_ratio)     # +20 dB/dec (w << w1)
asin_low[asin_low > 0] = 0            # se limita a 0 dB en la banda de paso
asin_high = np.zeros_like(f)          # 0 dB (w >> w1)
asintota = np.minimum(asin_low, asin_high)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)

# Magnitud
ax1.semilogx(f, mag_db, color="C0", lw=2.2, label="|Av| real")
ax1.semilogx(f, asintota, color="C3", ls="--", lw=1.6, label="Asintotas (+20 dB/dec y 0 dB)")
ax1.axvline(f1, color="gray", ls=":", lw=1.2)
ax1.plot(f1, -3, "ko", ms=6)
ax1.annotate(f"f1 = {f1:,.0f} Hz\n-3 dB", xy=(f1, -3),
             xytext=(f1 * 1.6, -12),
             arrowprops=dict(arrowstyle="->", color="black"), fontsize=9)
ax1.set_ylabel("Magnitud [dB]")
ax1.set_title("Red RC de corte inferior (pasa-alto)  —  R = 1 k$\\Omega$, C = 0.1 $\\mu$F")
ax1.set_ylim(-40, 5)
ax1.grid(True, which="both", alpha=0.3)
ax1.legend(loc="lower right", fontsize=9)

# Fase
ax2.semilogx(f, phase, color="C2", lw=2.2)
ax2.axvline(f1, color="gray", ls=":", lw=1.2)
ax2.axhline(45, color="gray", ls=":", lw=0.8)
ax2.plot(f1, 45, "ko", ms=6)
ax2.annotate("+45$^\\circ$ en f1", xy=(f1, 45), xytext=(f1 * 1.6, 60), fontsize=9)
ax2.set_ylabel("Fase [grados]")
ax2.set_xlabel("Frecuencia [Hz]")
ax2.set_ylim(-5, 95)
ax2.set_yticks([0, 45, 90])
ax2.grid(True, which="both", alpha=0.3)

plt.tight_layout()

out_dir = os.path.join(os.path.dirname(__file__), "attachments")
os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "bode_rc_corte_inferior.png")
plt.savefig(out, dpi=150, bbox_inches="tight")
print(f"Guardado: {out}")
