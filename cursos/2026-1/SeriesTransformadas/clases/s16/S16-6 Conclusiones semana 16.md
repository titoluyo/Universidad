---
title: "Conclusiones — Semana 16: Transformada Z (Parte 1)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 16
orden: 6
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/transformada-z
date: 2026-07-06
---

## Conclusiones de la semana

> [!abstract] Importancia de la transformada Z
> La transformada Z es la herramienta clave del **procesamiento de señales digitales**: generaliza la transformada de Fourier de secuencias, convergiendo para una gama más amplia de señales gracias al factor $r^{-n}$. Permite analizar y diseñar **filtros digitales** mediante manipulación algebraica.

## Ideas clave

- **Definición:** $X(z) = \sum_{n=-\infty}^{+\infty} x(n)z^{-n}$; la TF es el caso $z=e^{i\omega}$ (círculo unitario $|z|=1$).
- **Herramienta:** la **serie geométrica** convierte la sumatoria en una expresión cerrada.
- **Propiedades:** linealidad, desplazamiento ($z^{-n_0}$), escala, inversión, diferenciación, convolución → resuelven ecuaciones en diferencias algebraicamente.
- **ROC:** región anular $R^-<|z|<R^+$; ceros = raíces de $N(z)$, polos = raíces de $D(z)$.

## Transformadas Z notables (de los ejercicios)

| Secuencia | Transformada Z | ROC |
| --------- | -------------- | --- |
| $a^n u(n)$ | $\dfrac{z}{z-a}$ | $|z|>|a|$ |
| $\left(\tfrac15\right)^n u(n-3)$ | $\dfrac{\frac{1}{125}z^{-3}}{1-\frac15 z^{-1}}$ | $|z|>\tfrac15$ |
| $\cos\omega t$ (discreto) | $\dfrac{z(z-\cos\omega T)}{z^2-2z\cos\omega T+1}$ | $|z|>1$ |

## Siguiente semana

La Unidad 3 continúa en la **Semana 17** con la **Transformada Z (Parte 2)**: métodos de transformada inversa y aplicaciones a ecuaciones en diferencias.

## Bibliografía

- Mitra, S. K. (2007). *Procesamiento de Señales Digitales* (3.ª ed.). McGraw-Hill. México.
