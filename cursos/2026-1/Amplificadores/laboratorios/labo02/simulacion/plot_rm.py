import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from parse_raw import parse_ac_raw

D = os.path.dirname(__file__)

def curve(fn):
    names, data = parse_ac_raw(os.path.join(D, fn))
    f = [c.real for c in data[names[0]]]
    rm = [abs(data["V(c)"][i] / data["I(R1)"][i]) / 1e3 for i in range(len(f))]
    return f, rm

f1, rm1 = curve("le2_s1abierto.raw")
f2, rm2 = curve("le2_s1cerrado.raw")

plt.figure(figsize=(9, 5.2))
plt.semilogx(f2, rm2, label="S1 cerrado — SIN realimentacion", color="#c0392b", lw=2)
plt.semilogx(f1, rm1, label="S1 abierto — CON realimentacion", color="#2471a3", lw=2)
plt.axhline(11.2, ls="--", color="gray", lw=1, label="$R_f=R_3+R_4=11.2\\,k\\Omega$ (ideal)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("|Transresistencia| $|R_m|=|V_o/I_g|$  [k$\\Omega$]")
plt.title("LE2 - Respuesta en frecuencia de la transresistencia (2N2222, sim. LTspice)")
plt.grid(True, which="both", alpha=0.3)
plt.legend()
plt.xlim(10, 200000)
plt.ylim(0, 135)
plt.tight_layout()
out = os.path.join(D, "le2_respuesta_frecuencia.png")
plt.savefig(out, dpi=130)
print("saved", out)
