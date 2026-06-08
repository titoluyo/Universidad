import os, cmath

D = os.path.dirname(__file__)

def parse_ac_raw(path):
    with open(path, "r", errors="replace") as f:
        lines = f.read().splitlines()
    nvars = npts = None
    vars_start = vals_start = None
    for i, ln in enumerate(lines):
        if ln.startswith("No. Variables:"):
            nvars = int(ln.split(":")[1])
        elif ln.startswith("No. Points:"):
            npts = int(ln.split(":")[1])
        elif ln.startswith("Variables:"):
            vars_start = i + 1
        elif ln.startswith("Values:"):
            vals_start = i + 1
            break
    names = []
    for k in range(nvars):
        parts = lines[vars_start + k].split()
        names.append(parts[1])
    # parse complex values: each point = nvars lines, each "re\tim"
    data = {n: [] for n in names}
    idx = vals_start
    for p in range(npts):
        for k in range(nvars):
            toks = lines[idx].split()
            # first var line begins with point index; value is last token "re,im"
            re_str, im_str = toks[-1].split(",")
            data[names[k]].append(complex(float(re_str), float(im_str)))
            idx += 1
    return names, data

def nearest(freqs, target):
    return min(range(len(freqs)), key=lambda i: abs(freqs[i].real - target))

GUIDE_F = [20,100,200,1000,2000,5000,10000,20000,50000,70000,100000,150000]

for label, fn in [("S1 ABIERTO (con realim.)", "le2_s1abierto.raw"),
                  ("S1 CERRADO (sin realim.)", "le2_s1cerrado.raw")]:
    names, data = parse_ac_raw(os.path.join(D, fn))
    freqs = data[names[0]]  # frequency vector
    vc = data["V(c)"]
    ir1 = data["I(R1)"]     # Ig
    print("\n==== " + label + " ====")
    print(f"{'f[Hz]':>8} | {'|Rm|[kOhm]':>11} | {'fase Rm':>8} | {'|Zi|[kOhm]':>11}")
    for tf in GUIDE_F:
        i = nearest(freqs, tf)
        ig = ir1[i]
        rm = vc[i] / ig
        zi = 1.0 / ig          # Vg = 1 (AC), Zi = Vg/Ig
        print(f"{tf:>8} | {abs(rm)/1e3:>11.3f} | {cmath.phase(rm)*180/cmath.pi:>8.1f} | {abs(zi)/1e3:>11.4f}")
print("ok")
