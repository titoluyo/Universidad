---
title: Teorema de extension de Cauchy
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 6
orden: 6
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/teorema-de-cauchy
  - tema/extension-de-cauchy
  - tema/singularidad
  - tema/deformacion-de-contorno
date: 2026-05-03
---

## Introduccion

El [[S06-3 Tema 06 - Teorema de Cauchy|Teorema de Cauchy]] admite una **extensión** que permite trabajar con dominios no necesariamente simplemente conexos y manejar **singularidades**. Esta extensión introduce la idea fundamental de **deformación de contornos**.

> [!info] Material original
> Video del docente + transcripción en [[T03-Guion-extension-Cauchy.pdf|Guion - Teorema de extensión]].

## Enunciados de los teoremas

### Teorema (recordatorio del Teorema de Cauchy)

Si una función $f(z)$ es analítica en un dominio conexo $D$, entonces:

$$\oint_{C} f(z)\,dz = 0$$

para toda trayectoria simple cerrada $C$ contenida en $D$.

### Teorema (definicion de singularidad)

Si una función no es analítica en $z_0$ pero **sí es analítica en al menos un punto de todo entorno** de $z_0$, decimos que $z_0$ es una **singularidad** de la función.

### Teorema de extension (deformacion de contornos)

Las integrales de línea de una función analítica $f(z)$ alrededor de **dos contornos cerrados simples** son **idénticas** si uno de los contornos puede transformarse en el otro mediante una **deformación continua y sin parar**, **siempre y cuando** la deformación **no cruce ningún punto de singularidad**.

> [!summary] Idea visual
> Si tienes una banda elástica (contorno) en el plano y la deformas sin pasar por puntos de singularidad, la integral de $f$ sobre ella se mantiene constante. Las singularidades actúan como "clavos" que la banda no puede atravesar.

## Ejemplo de aplicacion

Sea $f(z) = \dfrac{\cos z}{z^2 + 1}$. Considerar 4 contornos $C_1, C_2, C_3, C_4$ cerrados simples (la figura del docente muestra distintas posiciones relativas alrededor de los puntos $\pm i$). Explicar la validez de:

a) $\displaystyle \int_{C_1} f(z)\,dz = \int_{C_2} f(z)\,dz$
b) $\displaystyle \int_{C_3} f(z)\,dz = \int_{C_4} f(z)\,dz$

### Paso 1: Identificar los puntos de singularidad

Los puntos donde el denominador se anula:

$$z^2 + 1 = 0 \implies (z + i)(z - i) = 0 \implies z = \pm i$$

> [!warning] Singularidades de $f(z) = \cos z / (z^2 + 1)$
> $f$ es analítica en todo $\mathbb{C}$ **excepto** en $z = i$ y $z = -i$. Estos son los "clavos" que las deformaciones no pueden cruzar.

### Paso 2: Analizar (a) — $C_1 \to C_2$

En la figura, $C_1$ y $C_2$ encierran ambos al punto $z = i$ pero **no encierran** $z = -i$. Al deformar $C_1$ hasta convertirlo en $C_2$, la deformación **solo "absorbe"** el punto $i$ pero **no cruza** $-i$. Como ningún punto de singularidad es cruzado durante la deformación, ambos contornos son equivalentes:

$$\int_{C_1} f(z)\,dz = \int_{C_2} f(z)\,dz \checkmark$$

### Paso 3: Analizar (b) — $C_3 \to C_4$

Similarmente, $C_3$ y $C_4$ están en una región donde la deformación entre ellos no requiere cruzar $\pm i$. Por lo tanto:

$$\int_{C_3} f(z)\,dz = \int_{C_4} f(z)\,dz \checkmark$$

### Caso invalido: $C_1 \to C_3$

Si intentamos deformar $C_1$ (que rodea $+i$) hasta $C_3$ (que está en otra región), tendríamos que cruzar el punto de singularidad $-i$ (o $+i$, dependiendo de las posiciones). Esa deformación **no es continua sin parar** en el sentido del teorema, por lo que **no podemos** afirmar:

$$\int_{C_1} f(z)\,dz \neq \int_{C_3} f(z)\,dz \quad \text{en general}$$

## Implicaciones

1. **Reducción de integrales:** un contorno complicado se puede deformar en otro más simple (e.g. circunferencia pequeña centrada en una singularidad) sin cambiar el valor de la integral.
2. **Principio para residuos:** la integral alrededor de una singularidad solo depende del comportamiento local de $f$ cerca de esa singularidad → motiva la teoría de residuos (semanas posteriores).
3. **Dominios multiplemente conexos:** se generaliza el Teorema de Cauchy a regiones con "huecos" (cada hueco con su propia singularidad encerrada).

## Conexion con [[S06-1 Tema 06 - Integral de contorno en funciones complejas#Ejercicio resuelto: $\oint \dfrac{dz}{z} = 2\pi i$ con $C: |z|=1$|el resultado ∮dz/z = 2πi]]

Por el Teorema de extensión: para **cualquier** contorno cerrado simple $C$ que rodee al origen una sola vez en sentido antihorario:

$$\oint_{C} \frac{dz}{z} = 2\pi i$$

(no solo para la circunferencia unitaria). Esto es el primer ejemplo no trivial donde la integral no es cero — porque $z = 0$ es singularidad de $1/z$ — y prepara el camino para la **fórmula integral de Cauchy** (semana 7).
