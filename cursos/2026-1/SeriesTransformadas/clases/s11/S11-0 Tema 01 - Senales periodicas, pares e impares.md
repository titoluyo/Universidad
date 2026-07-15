---
title: "Señales periódicas, pares e impares — definiciones y propiedades"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 11
orden: 0
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/senales-periodicas
  - tema/funciones-pares-impares
  - tema/series-de-fourier
date: 2026-06-01
---

## Idea central

La semana 11 abre el bloque de **series de Fourier**, que permiten descomponer una función **periódica** en una suma infinita de senos y cosenos. Antes de construir la serie, conviene caracterizar las señales con dos conceptos clave que **simplifican drásticamente** el cálculo de los coeficientes:

- La **periodicidad** (la función se repite cada cierto periodo $T$).
- La **paridad** (simetría par o impar), que anula de antemano la mitad de los coeficientes de Fourier.

Fuente: [[T01-Lectura-senales-periodicas.pdf|Lectura — Señales periódicas, pares e impares]].

## 1. Señal periódica

> [!summary] Función periódica
> Una función $f(t)$ es **periódica** si su dominio contiene a $t$ y a $t + T$, y cumple:
> $$f(t) = f(t + T)$$
> La **constante mínima** $T$ que satisface esta relación se llama **periodo** de la función.

- $f(t)$ = función de la variable (tiempo $t$).
- $T$ = periodo (el menor valor positivo que repite la función).

Geométricamente, la gráfica se repite idéntica en cada intervalo de longitud $T$ (ver figura 1 de la lectura: una onda que se reproduce cada $T$, $2T$, $3T$, …). La determinación práctica del periodo de una suma de funciones armónicas se trabaja en [[S11-1 Tema 01 - Ejercicio 1 - periodo de cos(t3) + cos(t4)|Ejercicio 1]].

## 2. Señal par

> [!summary] Función par
> $f(t)$ es **par** si:
> $$f(-t) = f(t)$$

Su gráfica es **simétrica respecto al eje vertical** (el eje $f(t)$). Ejemplo típico: la función **coseno**.

## 3. Señal impar

> [!summary] Función impar
> $f(t)$ es **impar** si:
> $$f(-t) = -f(t)$$

Su gráfica es **simétrica respecto al origen** (antisimétrica respecto al eje vertical). Ejemplo típico: la función **seno**.

## 4. Propiedades

> [!important] Álgebra de paridad y simplificación de integrales
> - **Producto:** par × par = par; impar × impar = par; **par × impar = impar**.
> - **Descomposición:** toda función $f(t)$ puede escribirse como la suma de una parte par y una parte impar.
> - **Integral en intervalo simétrico** $[-a, a]$:
>   - Si $f(t)$ es **par**: $\displaystyle\int_{-a}^{a} f(t)\,dt = 2\int_{0}^{a} f(t)\,dt$
>   - Si $f(t)$ es **impar**: $\displaystyle\int_{-a}^{a} f(t)\,dt = 0$

> [!tip] Por qué importa para Fourier
> Los coeficientes de Fourier se calculan con integrales sobre el intervalo simétrico $[-T/2,\, T/2]$:
> - Si $f$ es **par** → todos los $b_n = 0$ (la serie solo tiene **cosenos**), porque $f(t)\sin(n\omega t)$ es impar.
> - Si $f$ es **impar** → todos los $a_n = 0$ (la serie solo tiene **senos**), porque $f(t)\cos(n\omega t)$ es impar.
>
> Reconocer la paridad **antes de integrar** ahorra la mitad del trabajo. Ver [[S11-3 Tema 02 - Series de Fourier Ejercicio 1 - onda cuadrada|Ej 1]] (impar → solo senos) y [[S11-4 Tema 02 - Series de Fourier Ejercicio 2 - onda triangular|Ej 2]] (impar → solo senos).

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T01-Lectura-senales-periodicas.pdf|Lectura — Señales periódicas, pares e impares]].
