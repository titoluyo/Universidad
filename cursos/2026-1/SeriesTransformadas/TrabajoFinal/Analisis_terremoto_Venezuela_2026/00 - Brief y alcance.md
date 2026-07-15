---
title: "Análisis terremoto Venezuela 2026 — Brief y alcance"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
  - tema/sismo
date: 2026-06-29
---

# Análisis terremoto Venezuela 2026 · Brief y alcance

> [!info] Estado
> Carpeta de trabajo para la **variante temática** del Trabajo Final basada en el terremoto doble de Venezuela (24 jun 2026, ~7.1/7.2 y 7.5). **Aún no desarrollar**: este documento fija la línea y las condiciones. El desarrollo lo hará un agente dedicado.

## Idea y encaje con el curso

Es una **adaptación del Proyecto 2 (Transformada de Laplace)**, NO un tercer caso libre. La señal sísmica real no admite serie de Fourier analítica, así que la ruta Fourier queda descartada. El encaje válido es:

> Una **estructura** (edificio) se modela como **sistema masa–resorte–amortiguador de 2º orden**, matemáticamente **idéntico a un circuito RLC**. Con una **entrada sísmica idealizada** se resuelve la respuesta $x(t)$ **analíticamente con Laplace**, se simula y se compara el error. El terremoto de Venezuela aporta la **motivación y los antecedentes** (introducción / marco teórico).

## Condiciones que deben cumplirse (NO omitir)

> [!warning] Dos requisitos críticos antes de invertir trabajo
> 1. **Confirmar con el profesor** que se puede sustituir el escenario "Electronics S.A. / voltaje de capacitor" por uno de respuesta estructural sísmica. La consigna nombra un circuito eléctrico; la flexibilidad declarada es solo *individual/grupal*, **no de tema**. → ver [[Trabajo Final - SyT MOC|hub]].
> 2. **Entrada idealizada, no acelerograma crudo.** Para conservar la "solución teórica analítica + error" que pide la rúbrica, la excitación del suelo debe modelarse como una función simple (impulso, escalón, o **seno amortiguado**) — no el registro real punto a punto.

## Línea de trabajo (qué debe producir el agente)

1. **Antecedentes del sismo:** datos del evento del 24 jun 2026 (magnitudes, ubicación, profundidad) **citados de fuentes oficiales** (USGS, FUNVISIS) en APA. ⚠️ Verificar los datos por búsqueda web externa — no inventar cifras.
2. **Modelo físico:** estructura como sistema de 2º orden (masa $m$, rigidez $k$, amortiguamiento $c$). Establecer la **analogía RLC ↔ masa-resorte-amortiguador** (tabla de equivalencias).
3. **Entrada idealizada:** elegir y justificar la representación del movimiento del suelo (p. ej. seno amortiguado con frecuencia ~ la del sismo).
4. **Solución teórica (Laplace):** plantear la EDO de 2º orden, aplicar Laplace, despejar $X(s)$, antitransformar → $x(t)$ (o aceleración), graficar.
5. **Simulación:** Octave (o LTSPICE con el circuito RLC equivalente); obtener la respuesta simulada.
6. **Comparación y error:** teórico vs. simulado, mostrando el error.
7. **Discusión y conclusiones** (incluyendo interpretación física: resonancia, amortiguamiento).
8. **Documento PDF** (10–20 pág, Arial 12, 1.5, APA) + **video** ≤ 5 min.

## Rúbrica que debe cubrir (20 pts) — misma que Proyecto 2 (Laplace)

| Criterio | pts | Dónde se cubre |
| -------- | --- | -------------- |
| Introducción | 2 | antecedentes del sismo + objetivo |
| Marco teórico | 2 | Laplace + sistema 2º orden + analogía RLC + simulador |
| Dominio de simulación | 3 | modelo + resultados |
| Dominio teórico | 3 | desarrollo analítico de $x(t)$ con Laplace |
| Discusión y conclusiones | 4 | comparación con **error** + interpretación física |
| Referencias APA | 3 | datos sísmicos + teoría citados |
| Video | 3 | título, objetivos, metodología, análisis, conclusiones |

## Material de soporte

- Teoría Laplace: [[S14-1 Tema 01 - Transformadas de Laplace|Transformada de Laplace]].
- Sistemas de 2º orden resueltos con Laplace: [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|RLC carga y corriente]], [[S14-4 Tema 01 - Ejercicio 3 - Circuito RLC II|RLC II]].
- Consigna y rúbrica: [[S18-98 PROY Indicaciones]].
- Comparativa de viabilidad: [[00 - Brainstorming y eleccion|brainstorming]].

## Decisiones abiertas

- **Bloqueante:** ¿el profesor aprueba el cambio de escenario? (sin esto, este camino no es entregable).
- Verificar magnitudes/fecha del sismo con USGS/FUNVISIS.
- Elegir entrada idealizada (impulso / escalón / seno amortiguado).
- Modalidad individual o grupal.
