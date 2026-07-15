---
title: "Evaluación Semana 01 - Series y Transformadas"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 1
orden: 99
tipo: evaluacion
subtipo: cuestionario
tags:
  - curso/series-transformadas
  - tipo/evaluacion
  - subtipo/cuestionario
date: 2026-03-29
---

Debes presentar el desarrollo matemático considerando todos los aspectos indicados.

## 1. Resolver la raíz principal de $w^{\frac{3}{4}}+2i=0$

- Determina el módulo del número complejo.
- Determina el argumento principal mediante el plano complejo.

a. $(2)^{\frac{3}{4}}\left(\cos\frac{3\pi}{8}-i\,\text{sen}\frac{3\pi}{8}\right)$
b. $(2)^{\frac{4}{3}}\left(\cos\frac{3\pi}{8}-i\,\text{sen}\frac{3\pi}{8}\right)$
c. $(2)^{\frac{3}{4}}\left(\cos\frac{3\pi}{8}+i\,\text{sen}\frac{3\pi}{8}\right)$

### Resolución

**Despejamos** $w^{3/4}$:

$$w^{3/4} = -2i$$

Interpretamos "la raíz principal" como calcular $(-2i)^{3/4}$.

**Paso 1 — Forma polar de $-2i$:**

El número $-2i$ se ubica en el eje imaginario negativo:
- $|{-2i}| = 2$
- $\arg(-2i) = -\frac{\pi}{2}$ (argumento principal, apunta hacia abajo en el plano)

$$-2i = 2\left(\cos\left(-\frac{\pi}{2}\right) + i\,\text{sen}\left(-\frac{\pi}{2}\right)\right)$$

**Paso 2 — Aplicar la potencia $\frac{3}{4}$** usando la fórmula $z^n = |z|^n(\cos(n\theta) + i\,\text{sen}(n\theta))$:

$$(-2i)^{3/4} = 2^{3/4}\left(\cos\left(\frac{3}{4}\cdot\left(-\frac{\pi}{2}\right)\right) + i\,\text{sen}\left(\frac{3}{4}\cdot\left(-\frac{\pi}{2}\right)\right)\right)$$

$$= 2^{3/4}\left(\cos\left(-\frac{3\pi}{8}\right) + i\,\text{sen}\left(-\frac{3\pi}{8}\right)\right)$$

Usando las identidades $\cos(-\alpha) = \cos\alpha$ y $\text{sen}(-\alpha) = -\text{sen}\,\alpha$:

$$= 2^{3/4}\left(\cos\frac{3\pi}{8} - i\,\text{sen}\frac{3\pi}{8}\right)$$

**Descarte de otras opciones:**
- **b.** Tiene exponente $\frac{4}{3}$ en vez de $\frac{3}{4}$: confunde el exponente original con su inverso
- **c.** Tiene signo $+$ en la parte imaginaria, lo que correspondería a un argumento positivo $+\frac{3\pi}{8}$, pero el argumento de $-2i$ es negativo

**Teoría:** [[S01-1 Tema 01 - Funciones en el plano complejo|Funciones en el plano complejo]] (potencia polar-exponencial, forma polar)

> [!success] Respuesta: **a. $2^{\frac{3}{4}}\left(\cos\frac{3\pi}{8} - i\,\text{sen}\frac{3\pi}{8}\right)$**



## 2. Reducir la siguiente expresión $\frac{3-2i}{-1+i}$

- Aplica la conjugada para reducir la expresión.
- Aplica los conceptos de suma, resta y división de un número complejo.

a. $-\frac{5}{2}+\frac{i}{2}$
b. $-\frac{5}{2}-\frac{i}{2}$
c. $\frac{5}{2}+\frac{i}{2}$

### Resolución

**Multiplicamos numerador y denominador por la conjugada** del denominador $\overline{(-1+i)} = -1-i$:

$$\frac{3-2i}{-1+i} \cdot \frac{-1-i}{-1-i}$$

**Denominador:**

$$(-1+i)(-1-i) = (-1)^2 - (i)^2 = 1 - (-1) = 2$$

**Numerador:**

$$(3-2i)(-1-i) = -3 - 3i + 2i + 2i^2 = -3 - i + 2(-1) = -5 - i$$

**Resultado:**

$$\frac{-5-i}{2} = -\frac{5}{2} - \frac{i}{2}$$

**Descarte de otras opciones:**
- **a.** $-\frac{5}{2}+\frac{i}{2}$: tiene signo positivo en la parte imaginaria, error de signo al expandir el numerador
- **c.** $\frac{5}{2}+\frac{i}{2}$: ambos signos invertidos, como si no se hubiera aplicado el signo negativo del denominador

**Teoría:** [[S01-1 Tema 01 - Funciones en el plano complejo|Funciones en el plano complejo]] (división binómica, conjugada)

> [!success] Respuesta: **b. $-\frac{5}{2}-\frac{i}{2}$**

## 3. Exprese el siguiente número complejo en su forma polar $-1+\sqrt{3}i$

- Determina el módulo del número complejo en forma polar.
- Determina el argumento principal mediante el plano complejo.

a. $2\left(\cos\frac{\pi}{6}+i\text{sen}\frac{\pi}{6}\right)$
b. $2\left(\cos\frac{\pi}{3}+i\text{sen}\frac{\pi}{3}\right)$
c. $2\left(\cos\frac{2\pi}{3}+i\text{sen}\frac{2\pi}{3}\right)$
	
### Resolución

Sea $z = -1 + \sqrt{3}\,i$.

**Paso 1 — Módulo:**

$$|z| = \sqrt{(-1)^2 + (\sqrt{3})^2} = \sqrt{1 + 3} = \sqrt{4} = 2$$

**Paso 2 — Argumento principal:**

$$\tan\theta = \frac{\sqrt{3}}{-1} = -\sqrt{3}$$

Como la parte real es negativa y la parte imaginaria es positiva, $z$ está en el **segundo cuadrante**:

$$\theta = \pi - \arctan(\sqrt{3}) = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$$

**Forma polar:**

$$z = 2\left(\cos\frac{2\pi}{3} + i\,\text{sen}\frac{2\pi}{3}\right)$$

**Descarte de otras opciones:**
- **a.** Ángulo $\frac{\pi}{6}$ (30°): corresponde al primer cuadrante, pero $z$ tiene parte real negativa → segundo cuadrante
- **b.** Ángulo $\frac{\pi}{3}$ (60°): también primer cuadrante, no es correcto por la misma razón

**Teoría:** [[S01-1 Tema 01 - Funciones en el plano complejo|Funciones en el plano complejo]] (forma polar, argumento principal)

> [!success] Respuesta: **c. $2\left(\cos\frac{2\pi}{3} + i\,\text{sen}\frac{2\pi}{3}\right)$**

## 4. Sea $w=f(z)=z(2-z)$, hallar los valores de $w$ para $z=1+i$

- Evalúa el valor de $z$ en la función $f(z)$.
- Identifica la parte real e imaginaria de $w$.

a. $i$
b. $\frac{1}{2}$
c. $2$

### Resolución

**Sustituimos** $z = 1 + i$ en $f(z) = z(2 - z)$:

$$w = (1+i)(2 - (1+i)) = (1+i)(1-i)$$

Aplicamos la propiedad del **producto de conjugados** $z \cdot \bar{z} = |z|^2$:

$$(1+i)(1-i) = 1^2 - i^2 = 1 - (-1) = 2$$

**Verificación expandiendo:**

$$(1+i)(1-i) = 1 - i + i - i^2 = 1 + 1 = 2$$

**Identificación de partes:** $w = 2 + 0i$, es decir:
- Parte real: $u = 2$
- Parte imaginaria: $v = 0$

**Descarte de otras opciones:**
- **a.** $w = i$: implicaría que la parte real es 0, lo cual no corresponde al cálculo
- **b.** $w = \frac{1}{2}$: no hay forma de obtener este valor con la sustitución directa

**Teoría:** [[S01-1 Tema 01 - Funciones en el plano complejo|Funciones en el plano complejo]] (funciones de variable compleja, operaciones binómicas)

> [!success] Respuesta: **c. $w = 2$**

## 5. Hallar el valor de $\arg z$ para $z=-\frac{2}{1+\sqrt{3}i}$

- Aplica la conjugada.
- Identifica el argumento de $z$ en el plano.

a. $\frac{\pi}{6}$
b. $\frac{3\pi}{2}$
c. $\frac{2\pi}{3}$

### Resolución

**Paso 1 — Simplificar** multiplicando por la conjugada del denominador $\overline{(1+\sqrt{3}\,i)} = 1 - \sqrt{3}\,i$:

$$z = -\frac{2}{1+\sqrt{3}\,i} \cdot \frac{1-\sqrt{3}\,i}{1-\sqrt{3}\,i}$$

**Denominador:**

$$(1+\sqrt{3}\,i)(1-\sqrt{3}\,i) = 1^2 + (\sqrt{3})^2 = 1 + 3 = 4$$

**Numerador:**

$$-2(1-\sqrt{3}\,i) = -2 + 2\sqrt{3}\,i$$

**Resultado:**

$$z = \frac{-2 + 2\sqrt{3}\,i}{4} = -\frac{1}{2} + \frac{\sqrt{3}}{2}\,i$$

**Paso 2 — Determinar el argumento:**

- Parte real: $-\frac{1}{2} < 0$
- Parte imaginaria: $\frac{\sqrt{3}}{2} > 0$
- $z$ está en el **segundo cuadrante**

$$\tan\theta = \frac{\sqrt{3}/2}{-1/2} = -\sqrt{3}$$

$$\theta = \pi - \arctan(\sqrt{3}) = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$$

**Descarte de otras opciones:**
- **a.** $\frac{\pi}{6}$: corresponde al primer cuadrante (ambas partes positivas), pero $z$ tiene parte real negativa
- **b.** $\frac{3\pi}{2}$: apunta hacia el eje imaginario negativo, pero $z$ tiene parte imaginaria positiva

**Teoría:** [[S01-1 Tema 01 - Funciones en el plano complejo|Funciones en el plano complejo]] (argumento principal, conjugada, división)

> [!success] Respuesta: **c. $\arg z = \frac{2\pi}{3}$**
