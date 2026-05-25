---
title: "Aplicación del teorema de Cauchy — Caso 1: integral con dos singularidades simples"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 7
orden: 1
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/formula-integral-de-cauchy
  - tema/punto-de-singularidad
date: 2026-05-04
---

## Enunciado

Usando la **fórmula integral de Cauchy**, calcular:

$$\oint_C \frac{z^2 + 1}{z\,(2z + 1)}\,dz$$

donde $C: |z| = 1$ (circunferencia unitaria centrada en el origen).

Fuente: [[T01-Caso1-Guion.pdf|Guion del video del docente — Caso 1]].

## Definición previa: punto de singularidad

> [!info] Definición
> Un **punto de singularidad** $z_0$ es un valor donde la función $f(z)$ **no es analítica**. En cocientes, ocurre cuando el denominador se anula. Ver [[S07-0 Tema 01 - Relacion del teorema de Cauchy y una integral|nota base del Tema 01]].

**Ejemplo.** Para $f(z) = \dfrac{z^3 + 1}{z^2 + 1}$, los singulares son las soluciones de $z^2 + 1 = 0$, es decir, $z = \pm i$.

## Paso 1: identificar los puntos de singularidad

El denominador del integrando es $z\,(2z + 1)$. Igualándolo a cero:

$$z = 0 \qquad \text{y} \qquad 2z + 1 = 0 \;\Longrightarrow\; z = -\tfrac{1}{2}$$

> [!success] Singularidades
> $z_0 = 0$ y $z_0 = -\tfrac{1}{2}$.

## Paso 2: graficar la curva y verificar singularidades interiores

La curva $C: |z| = 1$ es una circunferencia de radio 1 centrada en el origen. Verificamos:

- $z = 0$ → en el origen, **dentro** de $C$ ✓
- $z = -\tfrac{1}{2}$ → módulo $\tfrac{1}{2} < 1$, **dentro** de $C$ ✓

Ambos puntos singulares quedan **dentro** del contorno → aplicamos la fórmula integral de Cauchy para cada uno y sumamos (por el [[S06-6 Tema 06 - Teorema de extension de Cauchy|teorema de extensión]]).

> [!warning] Regla práctica
> - Singulares **dentro** del contorno → usar fórmula integral de Cauchy.
> - Singulares **fuera** del contorno → la integral vale 0 (Teorema de Cauchy puro).

## Paso 3: contribución de $z_0 = 0$

Reorganizamos para aislar el factor $(z - 0) = z$ en el denominador:

$$\oint_C \frac{z^2 + 1}{z\,(2z + 1)}\,dz \;=\; \oint_C \frac{\dfrac{z^2 + 1}{2z + 1}}{z - 0}\,dz$$

Aquí $f(z) = \dfrac{z^2 + 1}{2z + 1}$ y $z_0 = 0$. Aplicando $\oint_C \dfrac{f(z)}{z - z_0}\,dz = 2\pi i\,f(z_0)$:

$$\text{Contribución}_{z=0} = 2\pi i \cdot f(0) = 2\pi i \cdot \frac{0^2 + 1}{2(0) + 1} = 2\pi i \cdot 1 = 2\pi i$$

## Paso 4: contribución de $z_0 = -\tfrac{1}{2}$

Para aislar el factor $\left(z - \left(-\tfrac{1}{2}\right)\right) = z + \tfrac{1}{2}$, **factorizamos el 2** del término $(2z + 1)$:

$$2z + 1 = 2\left(z + \tfrac{1}{2}\right)$$

Sustituyendo:

$$\oint_C \frac{z^2 + 1}{z \cdot 2\,(z + \tfrac{1}{2})}\,dz \;=\; \oint_C \frac{\dfrac{z^2 + 1}{2z}}{z + \tfrac{1}{2}}\,dz$$

Aquí $f(z) = \dfrac{z^2 + 1}{2z}$ y $z_0 = -\tfrac{1}{2}$. Aplicamos la fórmula:

$$\text{Contribución}_{z=-1/2} = 2\pi i \cdot f\!\left(-\tfrac{1}{2}\right) = 2\pi i \cdot \frac{\left(-\tfrac{1}{2}\right)^2 + 1}{2\left(-\tfrac{1}{2}\right)} = 2\pi i \cdot \frac{\tfrac{1}{4} + 1}{-1} = 2\pi i \cdot \left(-\tfrac{5}{4}\right) = -\frac{5\pi i}{2}$$

## Paso 5: sumar contribuciones

$$\oint_C \frac{z^2 + 1}{z(2z + 1)}\,dz = 2\pi i + \left(-\frac{5\pi i}{2}\right) = \frac{4\pi i - 5\pi i}{2} = -\frac{\pi i}{2}$$

> [!success] Resultado
> $$\oint_C \frac{z^2 + 1}{z(2z + 1)}\,dz = -\frac{\pi i}{2}$$

## Conclusión

La **fórmula integral de Cauchy** convierte una integral de contorno complicada en evaluaciones puntuales de $f(z)$. La clave operativa cuando hay un **coeficiente no unitario** en el factor lineal del denominador (caso $2z + 1$) es **factorizar la constante** para llevar el factor a la forma canónica $(z - z_0)$ y absorber el inverso de la constante dentro de $f(z)$.

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §50–52.
- Material del curso: [[T01-Caso1-Guion.pdf|Guion del video Aplicación del teorema de Cauchy 1]].
