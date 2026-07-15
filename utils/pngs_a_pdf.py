"""Junta varias imagenes (PNG/JPG) en un solo PDF, una por pagina.

Pensado para armar el PDF de entrega de evaluaciones a partir de fotos/escaneos
de la resolucion manuscrita (p. ej. los PA / PC del portal UTP).

Uso (con uv, sin necesidad de instalar nada de forma global):

    uv run --with img2pdf python utils/pngs_a_pdf.py <carpeta_o_imagenes> [-o salida.pdf]

Ejemplos:
    # Todas las imagenes de una carpeta, en orden alfabetico (por eso conviene
    # nombrarlas ...-P01, ...-P02, ...). Salida: <carpeta>/<carpeta>.pdf
    uv run --with img2pdf python utils/pngs_a_pdf.py "cursos/2026-1/SeriesTransformadas/clases/s10/PA04"

    # Lista explicita de imagenes y nombre de salida
    uv run --with img2pdf python utils/pngs_a_pdf.py p1.png p2.png p3.png -o entrega.pdf

Notas:
- img2pdf es *sin perdida*: incrusta el PNG/JPG tal cual (no recomprime).
- Cada imagen se ajusta a una pagina A4 vertical (--tamano para cambiar, o
  --nativo para usar el tamano nativo de cada imagen como pagina).
- Requiere `uv` (https://astral.sh/uv). Ver "Si falta algo" en CLAUDE.md.
"""
from __future__ import annotations

import argparse
import os
import sys

EXTS = (".png", ".jpg", ".jpeg")


def juntar(imagenes: list[str], salida: str, tamano: str = "A4", nativo: bool = False) -> str:
    """Escribe `salida` (PDF) con una imagen por pagina, en el orden dado."""
    import img2pdf

    for f in imagenes:
        if not os.path.exists(f):
            raise FileNotFoundError(f"No existe la imagen: {f}")

    if nativo:
        layout = None
    else:
        paper = {
            "A4": (210, 297),
            "CARTA": (216, 279),
            "LETTER": (216, 279),
        }[tamano.upper()]
        pagesize = (img2pdf.mm_to_pt(paper[0]), img2pdf.mm_to_pt(paper[1]))
        layout = img2pdf.get_layout_fun(pagesize)

    kwargs = {} if layout is None else {"layout_fun": layout}
    with open(salida, "wb") as fh:
        fh.write(img2pdf.convert(imagenes, **kwargs))
    return salida


def resolver_imagenes(entradas: list[str]) -> list[str]:
    """Si la unica entrada es una carpeta, lista sus imagenes ordenadas.

    En otro caso, devuelve las entradas tal cual (orden explicito del usuario).
    """
    if len(entradas) == 1 and os.path.isdir(entradas[0]):
        carpeta = entradas[0]
        archivos = sorted(
            os.path.join(carpeta, n)
            for n in os.listdir(carpeta)
            if n.lower().endswith(EXTS)
        )
        if not archivos:
            raise FileNotFoundError(f"No hay imagenes {EXTS} en {carpeta}")
        return archivos
    return entradas


def salida_por_defecto(entradas: list[str]) -> str:
    """PDF de salida por defecto: <carpeta>/<carpeta>.pdf o ./salida.pdf."""
    if len(entradas) == 1 and os.path.isdir(entradas[0]):
        carpeta = os.path.abspath(entradas[0])
        return os.path.join(carpeta, os.path.basename(carpeta) + ".pdf")
    return os.path.join(os.getcwd(), "salida.pdf")


def main() -> int:
    p = argparse.ArgumentParser(description="Junta imagenes en un PDF (una por pagina).")
    p.add_argument("entradas", nargs="+", help="Carpeta con imagenes, o lista de imagenes en orden.")
    p.add_argument("-o", "--salida", help="Ruta del PDF de salida.")
    p.add_argument("--tamano", default="A4", help="Tamano de pagina: A4 (def.) o CARTA.")
    p.add_argument("--nativo", action="store_true", help="Usar el tamano nativo de cada imagen como pagina.")
    args = p.parse_args()

    imagenes = resolver_imagenes(args.entradas)
    salida = args.salida or salida_por_defecto(args.entradas)

    juntar(imagenes, salida, tamano=args.tamano, nativo=args.nativo)
    print(f"OK -> {salida}")
    print(f"paginas: {len(imagenes)} | bytes: {os.path.getsize(salida)}")
    for i, f in enumerate(imagenes, 1):
        print(f"  p{i}: {os.path.basename(f)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
