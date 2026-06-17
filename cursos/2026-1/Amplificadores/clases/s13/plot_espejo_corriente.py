"""Característica de salida de un espejo de corriente bipolar.

Compara la fuente ideal (corriente constante) con la real (pendiente debida
al efecto Early / resistencia de salida finita r_o = V_A / I_C).

Ejecutar:  uv run --with matplotlib --with numpy python plot_espejo_corriente.py
"""
import numpy as np
import matplotlib.pyplot as plt

I_REF = 1.0      # mA (corriente de referencia / espejada)
V_A = 50.0       # V  (tensión de Early del transistor de salida)
V_CE_SAT = 0.2   # V  (límite de saturación del transistor de salida)

r_o = V_A / I_REF  # kΩ con I en mA -> resistencia de salida

vce = np.linspace(0, 10, 500)

# Real: I_O = I_REF * (1 + V_CE / V_A) en la región activa; en saturación cae a 0.
i_real = np.where(vce >= V_CE_SAT, I_REF * (1 + vce / V_A), I_REF / V_CE_SAT * vce)
i_ideal = np.where(vce >= V_CE_SAT, I_REF, I_REF / V_CE_SAT * vce)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(vce, i_ideal, "--", color="tab:green", lw=2,
        label="Ideal: $I_O = I_{REF}$ (constante)")
ax.plot(vce, i_real, color="tab:blue", lw=2,
        label=r"Real: pendiente $1/r_o$ (efecto Early)")

ax.axvline(V_CE_SAT, color="grey", ls=":", lw=1)
ax.text(V_CE_SAT + 0.1, 0.15, r"$V_{CE,sat}$", color="grey")
ax.axhline(I_REF, color="tab:green", ls=":", lw=0.8, alpha=0.6)
ax.text(8.2, I_REF + 0.02, "$I_{REF}$", color="tab:green")

# Anotar la resistencia de salida
ax.annotate(f"$r_o = V_A/I_C = {r_o:.0f}\\ k\\Omega$",
            xy=(7, I_REF * (1 + 7 / V_A)), xytext=(3.5, 1.18),
            arrowprops=dict(arrowstyle="->", color="tab:blue"), color="tab:blue")

ax.set_xlabel("$V_{CE}$ del transistor de salida [V]")
ax.set_ylabel("Corriente de salida $I_O$ [mA]")
ax.set_title("Característica de salida del espejo de corriente bipolar")
ax.set_xlim(0, 10)
ax.set_ylim(0, 1.3)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right")

fig.tight_layout()
fig.savefig("attachments/espejo_corriente.png", dpi=130)
print("Guardado attachments/espejo_corriente.png")
