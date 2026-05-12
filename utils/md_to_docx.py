"""Convierte una nota Markdown del vault a .docx con estilos APA v7.

Uso:
    python utils/md_to_docx.py <ruta-md> [--bib ref.bib] [-o salida.docx]

Pandoc traduce $...$ y $$...$$ a ecuaciones nativas de Word (OMML).
Las citas `[@key]` se renderizan en APA v7 si se pasa --bib.
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSL = ROOT / "plantillas" / "apa-7th.csl"
REFDOC = ROOT / "plantillas" / "reference-apa7.docx"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path, help="Archivo .md de entrada")
    p.add_argument("-o", "--output", type=Path, help="Archivo .docx de salida (default: junto al .md)")
    p.add_argument("--bib", type=Path, help="Archivo .bib para citas APA")
    p.add_argument("--no-toc", action="store_true", help="No generar tabla de contenidos")
    args = p.parse_args()

    if not shutil.which("pandoc"):
        sys.exit("ERROR: pandoc no esta en PATH")
    if not args.input.exists():
        sys.exit(f"ERROR: no existe {args.input}")
    if not CSL.exists() or not REFDOC.exists():
        sys.exit(f"ERROR: faltan {CSL} o {REFDOC}")

    out = args.output or args.input.with_suffix(".docx")
    cmd = [
        "pandoc",
        str(args.input),
        "-o", str(out),
        f"--reference-doc={REFDOC}",
        "--standalone",
        "--resource-path", str(args.input.parent),
    ]
    if not args.no_toc:
        cmd += ["--toc", "--toc-depth=3"]
    if args.bib:
        if not args.bib.exists():
            sys.exit(f"ERROR: no existe {args.bib}")
        cmd += ["--citeproc", f"--bibliography={args.bib}", f"--csl={CSL}"]

    print(" ".join(cmd))
    r = subprocess.run(cmd)
    if r.returncode == 0:
        print(f"OK -> {out}")
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
