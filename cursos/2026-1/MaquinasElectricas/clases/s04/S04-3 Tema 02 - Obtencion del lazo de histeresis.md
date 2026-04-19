---
title: Obtencion del lazo de histeresis
curso: "[[Motores MOC]]"
unidad: 1
semana: 4
orden: 3
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/histeresis
  - tema/curva-imanacion
  - tema/permeabilidad
  - tema/materiales-magneticos
date: 2026-04-19
---

![[s04-t02-banner.jpg]]

## Curva de imanación

La curva de la **Figura 1** se denomina *"curva de imanación de la muestra"* y la de la **Figura 2** representa algunas formas de *"curvas de magnetización"* (o imanación) para diversos materiales empleados en la construcción de máquinas eléctricas.

Se observa que la **chapa magnética** posee mejores cualidades magnéticas que el **hierro fundido** o que el **acero fundido**, ya que para la misma excitación magnética $H$ se consiguen inducciones más elevadas, lo que supone un volumen menor del material.

![[s04-t02-fig1-curva-imanacion-hierro.png]]
**Figura 1.** Curva de imanación del hierro.

![[s04-t02-fig2-curva-diversos-materiales.png]]
**Figura 2.** Curva de imanación de diversos materiales.

### Ecuación de Fröelich

Para resolver ejercicios prácticos o estudiar un circuito magnético con ayuda de un ordenador es más conveniente utilizar una expresión analítica que relacione $B$ con $H$. Una ecuación típica debida a **Fröelich** es:

$$B = \frac{a H}{1 + b H}$$

Donde:
- $B$ = densidad de flujo magnético (inducción) [T]
- $H$ = intensidad de campo magnético [A·vuelta/m]
- $a$, $b$ = constantes propias del material, elegidas para aproximar la curva real de magnetización

### Permeabilidad variable

La relación $B = f(H)$ en estas curvas **no es lineal**, lo que indica que la permeabilidad del material, definida por la siguiente ecuación, **no es constante** para diferentes valores de $H$:

$$\mu = \frac{B}{H}$$

Donde:
- $\mu$ = permeabilidad absoluta del material [H/m]
- $B$ = inducción magnética [T]
- $H$ = intensidad de campo magnético [A·vuelta/m]

---

## Proceso de obtención de la curva de histéresis

Para observar este fenómeno, consideremos que la muestra ferromagnética se introduce dentro de una bobina como indica la **Figura 3**. En la **Figura 4** se muestra la curva $B = f(H)$ que se obtiene al aplicar excitaciones magnéticas $H$ de diferente magnitud y signo.

![[s04-t02-fig3-bobina-nucleo.png]]
**Figura 3.** Bobina con núcleo ferromagnético.

![[s04-t02-fig4-obtencion-histeresis.png]]
**Figura 4.** Proceso de obtención de la curva de histéresis.

### Secuencia del ciclo

1. **Punto $a$ — material desmagnetizado:** partimos del material sin magnetización previa.
2. **Tramo $a \to b$:** al aplicar un campo $H$ creciente (introduciendo una corriente en la bobina en la dirección indicada en la Figura 3), la inducción $B$ sigue la curva de imanación hasta alcanzar el **punto $b$** (saturación positiva).
3. **Tramo $b \to c$ — reducción de $H$:** cuando se hace disminuir $H$, el valor de $B$ se reduce, pero **según un camino diferente** al de la magnetización inicial.
4. **Punto $c$ — inducción remanente ($B_r$):** al volver $H$ a cero, persiste una cierta magnetización. Al valor de $B$ en este punto se le conoce con el nombre de **magnetismo o inducción remanente** y constituye el **estado de magnetización permanente** de la muestra.
5. **Punto $d$ — campo coercitivo ($H_c$):** determina el **campo opuesto** que resulta necesario aplicar para **desmagnetizar la muestra** (por inversión en el sentido de la corriente de la bobina).
6. **Tramo $d \to e$:** si continuamos aumentando $H$ en el sentido negativo, llegamos a la saturación negativa en el **punto $e$**.
7. **Retorno $e \to b$:** al invertir nuevamente el sentido de cambio de $H$, se cierra la curva formando el **ciclo de histéresis**.

> [!info] Parámetros característicos del ciclo
> - **Inducción remanente $B_r$** (punto $c$): magnetización que queda al anular la excitación.
> - **Campo coercitivo $H_c$** (punto $d$): excitación necesaria para anular la magnetización remanente.
> - **Área del ciclo:** representa la energía disipada por unidad de volumen en cada ciclo (pérdidas por histéresis).

### Tabla de parámetros para diversos materiales

En la Tabla 1 se muestran algunos valores característicos de la curva de histéresis (y algunos otros parámetros) para diversos materiales empleados en la Tecnología Eléctrica.

![[s04-t02-tabla1-parametros-materiales.png]]
**Tabla 1.** Parámetros de la curva de histéresis para diversos materiales.

---

## Ejercicio 1 — Cálculo con permeabilidad relativa constante

### Enunciado

El núcleo central del circuito magnético de la **Figura 5** está bobinado con **800 espiras**. El material es **acero fundido** con un valor de la **permeabilidad relativa $\mu_r = 1000$**. Calcular la corriente $i$ que debe aplicarse a la bobina para obtener en el entrehierro un flujo de **1 mWb**.

![[s04-t02-fig5-circuito-magnetico.png]]
**Figura 5.** Circuito magnético.

### Datos

- $N = 800$ espiras
- $\mu_r = 1000$ (acero fundido)
- $\phi = 1 \, \text{mWb} = 10^{-3} \, \text{Wb}$
- Longitud de las columnas laterales: $l = 700 \, \text{mm}$
- Sección: $S = 2000 \, \text{mm}^2 = 2000 \times 10^{-6} \, \text{m}^2$

### Resolución

El circuito eléctrico equivalente es el indicado en la **Figura 6**, donde:
- $R_1$ = reluctancia de cada uno de los núcleos laterales
- $R_c$ = reluctancia del núcleo central
- $R_e$ = reluctancia del entrehierro

![[s04-t02-fig6-circuito-equivalente.png]]
**Figura 6.** Circuito equivalente.

**Reluctancia de las columnas laterales:**

$$R_1 = \frac{l}{\mu_r \cdot \mu_0 \cdot S} = \frac{700 \times 10^{-3}}{1000 \cdot 4\pi \times 10^{-7} \cdot 2000 \times 10^{-6}} = 27{,}85 \times 10^{4} \, [H^{-1}]$$

Donde:
- $R_1$ = reluctancia de cada columna lateral [H⁻¹ = A·vuelta/Wb]
- $l$ = longitud magnética de la columna [m]
- $\mu_r$ = permeabilidad relativa del material
- $\mu_0 = 4\pi \times 10^{-7} \, \text{H/m}$ = permeabilidad del vacío
- $S$ = sección transversal [m²]

**Reluctancias del núcleo central y del entrehierro:**

$$R_c = 4{,}97 \times 10^{4} \, [H^{-1}] \, ; \quad R_e = 19{,}9 \times 10^{4} \, [H^{-1}]$$

**Reluctancia equivalente de las columnas laterales (en paralelo):**

$$R_{eq} = \frac{R_1}{2} = 13{,}92 \times 10^{4} \, [H^{-1}]$$

Esto da lugar al siguiente circuito de la **Figura 7**:

![[s04-t02-fig7-seccion-circuito-equivalente.png]]
**Figura 7.** Sección del circuito equivalente.

**Aplicando la [[S01-2 Tema 01 - Los circuitos magnéticos|ley de los circuitos magnéticos (Ley de Hopkinson)]]:**

$$\sum N \cdot i = \phi \cdot \sum R = 10^{-3} \cdot (4{,}97 + 19{,}9 + 13{,}92) \times 10^{4} = 387{,}9 \, A \cdot v$$

Donde:
- $\sum N \cdot i$ = fuerza magnetomotriz total [A·vuelta]
- $\phi$ = flujo magnético en el núcleo central [Wb]
- $\sum R$ = reluctancia equivalente total ($R_c + R_e + R_{eq}$) [H⁻¹]

Solo hay una bobina de $N$ vueltas con una corriente $i$, por tanto:

$$i = \frac{387{,}9}{800}$$

$$\boxed{i = 0{,}485 \, A}$$

---

## Ejercicio 2 — Cálculo con curva de magnetización analítica

### Enunciado

Resolver el problema anterior suponiendo que la curva de magnetización del acero fundido viene expresada por la ecuación:

$$B = \frac{1{,}8 \times 10^{-3} \, H}{1 + 10^{-3} \, H} \quad ; \quad B \text{ [Tesla]} \, ; \quad H \left[A \cdot \frac{v}{m}\right]$$

### Resolución

**Paso 1: Flujo en las columnas laterales (por simetría)**

Debido a la simetría del circuito, el flujo en las columnas laterales vale la mitad que en la columna central:

$$\phi_1 = \frac{\phi}{2} = 0{,}5 \times 10^{-3} \, Wb$$

Donde:
- $\phi_1$ = flujo en cada columna lateral [Wb]
- $\phi$ = flujo en la columna central [Wb]

**Paso 2: Inducción en las columnas laterales**

Como la sección lateral es igual a $2000 \, \text{mm}^2$, la inducción en estas columnas será:

$$B_1 = \frac{\phi_1}{S} = \frac{0{,}5 \times 10^{-3}}{2000 \times 10^{-6}} = 0{,}25 \, \text{Teslas}$$

Donde:
- $B_1$ = inducción en las columnas laterales [T]
- $\phi_1$ = flujo en las columnas laterales [Wb]
- $S$ = sección transversal [m²]

**Paso 3: Intensidad de campo $H_1$ desde la curva de magnetización**

Sustituyendo $B_1 = 0{,}25 \, T$ en la ecuación de Fröelich del material:

$$0{,}25 = \frac{1{,}8 \times 10^{-3} \, H_1}{1 + 10^{-3} \, H_1} \Rightarrow H_1 = 161{,}29 \, A \cdot \frac{v}{m}$$

**Paso 4: Intensidad de campo en el núcleo central $H_c$**

El núcleo central tiene **doble flujo y doble sección** que las columnas laterales, por lo que se deduce idéntico valor de la inducción $B$ y, en consecuencia, de la excitación $H$:

$$H_c = H_1 = 161{,}29 \, A \cdot \frac{v}{m}$$

**Paso 5: Intensidad de campo en el entrehierro $H_e$**

En el entrehierro, la inducción es la misma que en el núcleo central ($B = 0{,}25 \, T$) y la permeabilidad es la del vacío ($\mu_r = 1$):

$$B = 0{,}25 \, \text{Teslas} \Rightarrow H_e = \frac{B}{\mu_0} = \frac{0{,}25}{4\pi \times 10^{-7}} = 1{,}99 \times 10^{5} \, A \cdot \frac{v}{m}$$

Donde:
- $H_e$ = intensidad de campo en el entrehierro [A·v/m]
- $B$ = inducción en el entrehierro [T]
- $\mu_0 = 4\pi \times 10^{-7} \, \text{H/m}$

**Paso 6: Aplicación de la ley de Ampère**

Aplicando la ley de Ampère a lo largo del circuito magnético (columna lateral + núcleo central + entrehierro):

$$N \cdot i = H_1 \cdot l_1 + H_c \cdot l_c + H_e \cdot l_e$$

$$N \cdot i = 161{,}29 \times 0{,}7 + 161{,}29 \times 0{,}25 + 1{,}99 \times 10^{5} \times 10^{-3}$$

$$N \cdot i = 352{,}23 \, A \cdot v$$

$$i = \frac{352{,}23}{800}$$

$$\boxed{i = 0{,}44 \, A}$$

> [!note] Comparación de resultados
> El **Ejercicio 1** con $\mu_r = 1000$ constante da $i = 0{,}485 \, A$, mientras que el **Ejercicio 2** con la curva de magnetización real (Fröelich) da $i = 0{,}44 \, A$. La diferencia proviene de que la permeabilidad real no es constante sino que depende de $H$, y en este punto de operación el material presenta una permeabilidad efectiva algo mayor que $\mu_r = 1000$.

---

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6ta. ed.). McGraw-Hill Interamericana.
