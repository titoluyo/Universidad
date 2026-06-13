"""Rectificador de pico: forma de onda de salida y rizado V_r.

Simula el detector de envolvente (diodo + RC). El diodo conduce solo cerca
del pico (carga el condensador a V_p); el resto del periodo el condensador
se descarga sobre R segun v_O = V_p * e^(-t/CR), generando el rizado V_r.

Aproximacion del curso (CR >> T):
    V_r = V_p * T / (C*R)

Ejecutar:  uv run --with matplotlib python plot_rizado.py
"""
import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = os.path.dirname(__file__)

# --- Parametros didacticos ---
Vp = 10.0          # tension de pico [V]
f = 60.0           # frecuencia [Hz]
T = 1.0 / f        # periodo [s]
CR = 10.0 * T      # constante de tiempo (CR >> T  ->  rizado ~10%)

# --- Simulacion del detector de envolvente ---
N = 20000
tmax = 3.05 * T
dt = tmax / N
t = [i * dt for i in range(N)]
vin = [Vp * math.cos(2 * math.pi * f * ti) for ti in t]   # pico en t=0, T, 2T...

vo = [0.0] * N
vo[0] = vin[0]
for i in range(1, N):
    # diodo conduce mientras la fuente supera la tension del condensador
    if vin[i] >= vo[i - 1]:
        vo[i] = vin[i]                          # carga (sigue al pico)
    else:
        vo[i] = vo[i - 1] * math.exp(-dt / CR)  # descarga exponencial sobre R

# Rizado teorico
Vr = Vp * T / CR

# --- Grafica ---
fig, ax = plt.subplots(figsize=(10, 5.4))
ms = [ti * 1000 for ti in t]  # a milisegundos

ax.plot(ms, vin, color="#95a5a6", lw=1.3, ls="--", label="$v_I = V_p\\cos\\omega t$ (entrada)")
ax.plot(ms, vo, color="#c0392b", lw=2.4, label="$v_O$ (salida rectificada)")

# Lineas de referencia
ax.axhline(Vp, color="#2471a3", lw=1, ls=":")
ax.axhline(Vp - Vr, color="#27ae60", lw=1, ls=":")
ax.text(ms[-1], Vp + 0.15, "$V_p$", color="#2471a3", va="bottom", ha="right", fontsize=12)

# Acotacion del rizado V_r justo antes del 2do pico (final de la descarga)
xr = 0.97 * T * 1000
ax.annotate("", xy=(xr, Vp), xytext=(xr, Vp - Vr),
            arrowprops=dict(arrowstyle="<->", color="#16a085", lw=1.8))
ax.text(xr - 0.5, Vp - Vr / 2, "$V_r$", color="#16a085", va="center", ha="right", fontsize=13)

# Marca del periodo T entre dos picos consecutivos (arriba)
yT = Vp + 0.9
ax.annotate("", xy=(T * 1000, yT), xytext=(2 * T * 1000, yT),
            arrowprops=dict(arrowstyle="<->", color="#7f8c8d", lw=1.4))
ax.text(1.5 * T * 1000, yT + 0.15, "$T = 1/f$", color="#7f8c8d", ha="center", va="bottom", fontsize=12)

# Senalar tramo de descarga
ax.annotate("descarga: $v_O=V_p\\,e^{-t/CR}$", xy=(1.4 * T * 1000, Vp - 0.5 * Vr),
            xytext=(1.55 * T * 1000, Vp - 3.4),
            arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.2),
            color="#c0392b", fontsize=11)

ax.set_title(f"Rectificador de pico — rizado $V_r$  (V_p={Vp:.0f} V, f={f:.0f} Hz, CR=10T)")
ax.set_xlabel("tiempo [ms]")
ax.set_ylabel("tension [V]")
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right")
ax.set_ylim(-Vp - 1.6, Vp + 2.0)
ax.set_xlim(0, tmax * 1000)

txt = f"$V_r = V_p\\,T/CR = {Vr:.2f}$ V  ({100*Vr/Vp:.0f}% de $V_p$)"
ax.text(0.012, 0.045, txt, transform=ax.transAxes, fontsize=11,
        bbox=dict(boxstyle="round", fc="#fdf6e3", ec="#16a085"))

plt.tight_layout()
out = os.path.join(D, "attachments", "rectificador_pico_rizado.png")
plt.savefig(out, dpi=130)
print("saved", out, "| Vr =", round(Vr, 3), "V")
