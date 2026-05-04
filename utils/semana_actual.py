"""Calcula la semana del ciclo lectivo a partir de una fecha.

Convencion Peru: las semanas comienzan el lunes.
Cada ciclo dura 18 semanas; el inicio se configura abajo.
"""
from __future__ import annotations
from datetime import date, timedelta

# Inicio de la primera semana (lunes) por ciclo.
# Agregar nuevos ciclos aqui cuando empiece uno nuevo.
INICIOS_CICLO: dict[str, date] = {
    "2026-1": date(2026, 3, 23),
}


def semana_del_ciclo(hoy: date | None = None, ciclo: str = "2026-1") -> int:
    """Numero de semana (1..18) del ciclo en que cae `hoy`.

    Devuelve 0 si `hoy` es anterior al inicio del ciclo, y >18 si ya termino.
    """
    if hoy is None:
        hoy = date.today()
    inicio = INICIOS_CICLO[ciclo]
    return (hoy - inicio).days // 7 + 1


def rango_semana(numero: int, ciclo: str = "2026-1") -> tuple[date, date]:
    """Devuelve (lunes, domingo) de la semana `numero` del ciclo."""
    inicio_ciclo = INICIOS_CICLO[ciclo]
    lunes = inicio_ciclo + timedelta(days=(numero - 1) * 7)
    domingo = lunes + timedelta(days=6)
    return lunes, domingo


if __name__ == "__main__":
    import sys
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    hoy = date.fromisoformat(arg) if arg else date.today()
    n = semana_del_ciclo(hoy)
    lunes, domingo = rango_semana(n)
    print(f"{hoy.isoformat()} ({hoy.strftime('%A')}) -> Semana {n:02d} "
          f"({lunes.isoformat()} a {domingo.isoformat()})")
