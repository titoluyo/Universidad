---
title: "Etapa 0 — Brainstorming y elección del proyecto"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
date: 2026-06-29
---

# Etapa 0 — Brainstorming y elección

Objetivo: decidir **qué proyecto** desarrollar y **en qué modalidad** (individual/grupal) antes de invertir tiempo. Hay que escoger **uno solo** de los dos proyectos.

## Las dos opciones

### Proyecto 1 — Serie de Fourier (señal senoidal rectificada)
- **Qué se pide:** hallar **analíticamente** la serie de Fourier de una **señal senoidal rectificada de media onda** y aproximarla; comparar teoría vs. simulación con el error.
- **Herramienta:** **GNU Octave** (programa de aproximación de la señal).
- **Teoría de respaldo en el vault:** [[S11-2 Tema 02 - Series de Fourier|Series de Fourier]], [[S12-0 Tema 01 - Analisis de las series de Fourier|medio rango y media onda]], [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|error cuadrático del seno rectificado]], [[S16-5 Tema 02 - Programa Octave|Programa Octave]].

### Proyecto 2 — Transformada de Laplace (voltaje de un capacitor)
- **Qué se pide:** determinar **analíticamente** $V_o$ y graficar $V_o(t)$ de un circuito aplicando la **transformada de Laplace**; comparar teoría vs. simulación con el error.
- **Herramienta:** simulador de circuitos (**LTSPICE**) o Octave.
- **Teoría de respaldo en el vault:** [[S14-1 Tema 01 - Transformadas de Laplace|Transformada de Laplace]], [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|circuito RLC]], [[S14-4 Tema 01 - Ejercicio 3 - Circuito RLC II|circuito RLC II]].

## Comparación rápida

| Criterio | Proyecto 1 (Fourier) | Proyecto 2 (Laplace) |
| -------- | -------------------- | -------------------- |
| Cobertura de teoría en el vault | Muy alta (S11, S12, incl. error del seno rectificado) | Alta (S14) |
| Herramienta de simulación | Octave (ya documentado en S16-5) | LTSPICE (instalar/configurar) o Octave |
| Parte analítica | Integrales de coeficientes $a_n,b_n$ | Antitransformada / fracciones parciales |
| Cálculo del error simulado vs. teórico | Directo (error cuadrático ya visto en [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado\|S12-3]]) | Comparar $V_o(t)$ punto a punto |
| Riesgo principal | Definir bien el enunciado exacto de la señal | Definir bien los valores R, L, C y la fuente |

> [!tip] Recomendación (a confirmar por el usuario)
> **Proyecto 1 (Fourier con Octave)** parece el camino de menor fricción: el vault ya tiene la teoría completa de la señal rectificada, el **cálculo del error cuadrático ya está resuelto** en [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|S12-3]], y **Octave ya está documentado** en [[S16-5 Tema 02 - Programa Octave|S16-5]] (no requiere instalar LTSPICE). Elegir Proyecto 2 si se prefiere trabajar con circuitos eléctricos y ya se domina LTSPICE.

## Decisión

> [!success] Decisión tomada
> - **Proyecto elegido:** _(Proyecto 1 / Proyecto 2)_ → **por decidir**
> - **Modalidad:** _(Individual / Grupal)_ → **por decidir**
> - **Integrantes** (si grupal): _…_
> - **Señal / circuito concreto a analizar:** _(definir parámetros exactos una vez elegido)_

## Lluvia de ideas / notas libres

- _…_
