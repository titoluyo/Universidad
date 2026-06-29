---
title: "Ejercicio 4 — Ecuación en diferencias con entrada (polos complejos)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 17
orden: 5
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/transformada-z-inversa
  - tema/ecuaciones-en-diferencias
  - tema/fracciones-parciales
date: 2026-07-13
---

## Enunciado

> [!question] Problema
> Resolver la ecuación en diferencias
> $$y[n+2] - 0.8\,y[n+1] + 0.25\,y[n] = x[n], \qquad x[n] = 10\,(0.5)^n$$
> con condiciones iniciales $y[0] = 4$, $y[1] = 2$.

Fuente: [[T01-EcuacionDiferencias-Guion.pdf|Guion del video — Aplicaciones a ecuaciones diferenciales]].

## Desarrollo

### Paso 1 — Aplicar la transformada Z

Con las propiedades de adelanto (que incorporan $y_0=4$, $y_1=2$) y $\mathcal{Z}\{10(0.5)^n\} = \dfrac{10z}{z - 0.5}$:

$$\bigl(z^2 Y - 4z^2 - 2z\bigr) - 0.8\bigl(zY - 4z\bigr) + 0.25\,Y = \frac{10z}{z-0.5}$$

### Paso 2 — Despejar $Y(z)$

Factorizando $Y(z)$ con el polinomio característico $z^2 - 0.8z + 0.25$:

$$Y(z)\,(z^2 - 0.8z + 0.25) = \frac{10z}{z-0.5} + 4z^2 - 1.2z$$

$$Y(z) = \frac{4z^3 - 3.2z^2 + 10.6z}{(z-0.5)\,(z^2 - 0.8z + 0.25)}$$

### Paso 3 — Factorizar el denominador (raíces complejas)

El polinomio característico tiene **raíces complejas conjugadas**:

$$z^2 - 0.8z + 0.25 = \bigl(z - 0.5\,e^{\,i\,0.6435}\bigr)\bigl(z - 0.5\,e^{-i\,0.6435}\bigr)$$

(módulo $0.5$, ángulo $\theta = 0.6435$ rad). El término de entrada aporta además un polo **real** en $z = 0.5$.

### Paso 4 — Fracciones parciales e inversa

Dividiendo $\frac{Y(z)}{z}$ y expandiendo en fracciones parciales, el residuo del polo real es $A = 100$; los polos complejos conjugados dan residuos complejos conjugados. Al invertir (propiedad de la transformada inversa con traslación), se obtiene una **componente de entrada** $(0.5)^n$ más una **oscilación amortiguada** de módulo $0.5^n$ y frecuencia $\theta = 0.6435$ rad:

> [!success] Forma de la solución
> $$y[n] = \Bigl[\,100\,(0.5)^n \;-\; (0.5)^n\bigl(\alpha\cos(0.6435\,n) + \beta\sin(0.6435\,n)\bigr)\Bigr]u(n)$$
> donde $\alpha,\beta$ son los coeficientes reales que provienen de los residuos complejos conjugados.

> [!warning] Sobre los coeficientes numéricos
> El guion del video obtiene los coeficientes $\alpha,\beta$ con ayuda de calculadora (residuos complejos $-48 \mp 16i$), pero su transcripción presenta valores poco claros (p. ej. "696"). Lo robusto del ejercicio es el **método**: polinomio característico con raíces complejas → fracciones parciales con residuos complejos conjugados → transformada inversa que da una **sinusoide amortiguada** $0.5^n$ a frecuencia $0.6435$ rad, más el término de entrada $100(0.5)^n$. Conviene recalcular $\alpha,\beta$ a mano si se requieren los valores exactos.

## Conceptos aplicados

- [[S17-1 Tema 01 - Transformada Z Parte 2#4. Transformada Z unilateral|Desplazamiento unilateral (condiciones iniciales)]].
- [[S17-1 Tema 01 - Transformada Z Parte 2#2. Transformada Z inversa|Fracciones parciales]] (con raíces complejas).
- Comparar con el caso de raíces reales: [[S17-6 Tema 01 - Ecuacion en diferencias homogenea|Ej 5]].

## Bibliografía

- Mitra, S. K. (2007). *Procesamiento de Señales Digitales* (3.ª ed.). McGraw-Hill. México.
