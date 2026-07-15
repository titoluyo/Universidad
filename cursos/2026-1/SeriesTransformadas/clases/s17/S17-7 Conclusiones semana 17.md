---
title: "Conclusiones — Semana 17: Transformada Z (Parte 2)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 17
orden: 7
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/transformada-z-inversa
date: 2026-07-13
---

## Conclusiones de la semana

> [!abstract] Síntesis
> La **transformada Z inversa** permite regresar del dominio $z$ al dominio del tiempo discreto. Dominarla es clave para el **análisis y diseño de señales digitales**: una vez resuelto algebraicamente un sistema en $z$, la inversión devuelve la respuesta $x(n)$ en el tiempo.

## Ideas clave

- **TF especiales:** $\delta(n)\to 1$; $\delta(n-m)\to z^{-m}$; $u(n)\to \frac{z}{z-1}$; $a^n\to\frac{z}{z-a}$; $e^{-aT n}\to\frac{z}{z-e^{-aT}}$.
- **Cuatro métodos de inversión:** división larga, fracciones parciales + tabla, integral de inversión (residuos), inspección.
- **Residuos:** $x(n) = \sum_i [(z-z_i)X(z)z^{n-1}]_{z_i}$ (polos simples), vía teorema de Cauchy.
- **Transformada unilateral:** para sistemas causales; el desplazamiento incorpora las **condiciones iniciales** → resuelve ecuaciones en diferencias.

## Resumen de los ejercicios

| Ejercicio | Método | Resultado |
| --------- | ------ | --------- |
| [[S17-2 Tema 01 - Inversa por division larga\|Fibonacci]] | División larga | $y_n = 1,1,2,3,5,8,\ldots$ |
| [[S17-3 Tema 01 - Inversa por integral de inversion\|$\frac{z}{z-a}$]] | Integral de inversión | $a^n u(n)$ |
| [[S17-4 Tema 01 - Inversa por residuos\|$\frac{z}{(z-1)(z-0.8)}$]] | Residuos | $5(1-0.8^k)$ |
| [[S17-5 Tema 01 - Ecuacion en diferencias con entrada\|Ec. con entrada]] | Fracciones parciales (raíces complejas) | $100(0.5)^n -$ sinusoide amortiguada |
| [[S17-6 Tema 01 - Ecuacion en diferencias homogenea\|Ec. homogénea]] | Fracciones parciales (raíces reales) | $3^k + 2(-\tfrac12)^k$ |

## Cierre de la Unidad 3

Con la transformada Z concluye el recorrido por las **transformadas** (Laplace, Fourier, Z). La **Semana 18** cierra el ciclo (evaluación final / repaso).

## Bibliografía

- Mitra, S. K. (2007). *Procesamiento de Señales Digitales* (3.ª ed.). McGraw-Hill. México.
