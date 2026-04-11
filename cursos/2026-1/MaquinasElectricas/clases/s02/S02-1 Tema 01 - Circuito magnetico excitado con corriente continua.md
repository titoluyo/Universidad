---
title: Circuito magnetico excitado con corriente continua
curso: "[[Motores MOC]]"
unidad: 1
semana: 2
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/circuito-magnetico
  - tema/corriente-continua
  - tema/induccion-magnetica
  - tema/reluctancia
  - tema/ley-de-hopkinson
  - tema/entrehierro
date: 2026-04-11
---

## Elementos fundamentales de un circuito magnético excitado con corriente continua

Cuando una corriente continua fluye a través de una bobina, se genera un campo magnético en su interior. La orientación de las líneas de campo o líneas de inducción se ilustra en la figura 1 y se puede deducir aplicando la **regla del tirabuzón** (también conocida como la regla de la mano derecha), considerando la dirección de la corriente. Aunque el campo magnético también se extiende fuera de la bobina, sus efectos son considerablemente más tenues. Por lo tanto, se requiere otra medida para definirlo completamente en todos los puntos del espacio en los que aparece.

Esa magnitud es la **inducción magnética o densidad de flujo**, representada como "$B$", cuya unidad es el $[\text{Wb/m}^2]$. En cada punto del espacio donde está presente, esta magnitud posee una dirección, un sentido y un valor específico. La dirección y el sentido se establecen de acuerdo con la orientación de la corriente que la genera.

![[Figura 1. Regla del tirabuzón.png]]
**Figura 1.** Regla del tirabuzón o la mano derecha

Esa magnitud es la inducción magnética o densidad de flujo, representada como "$B$", cuya unidad es el $[\text{Wb/m}^2]$. En cada punto del espacio donde está presente, esta magnitud posee una dirección, un sentido y un valor específico. La dirección y el sentido se establecen de acuerdo con la orientación de la corriente que la genera.

En ciertos contextos, en lugar de utilizar la inducción magnética, se prefiere emplear el término **"flujo magnético"** o **"flujo de inducción"** para describir la acción magnética total en una superficie determinada. Este flujo se representa con la letra $\phi$ (phi) y se mide en Weber $[\text{Wb}]$.

La relación es:

$$\phi = B \cdot S$$

Donde:
- $S$ = superficie recta por donde pasa el flujo en $\text{m}^2$

Esta fórmula es válida si $B$ se mantiene constante en cualquier parte de la sección $S$. En la figura 2 se muestra el denominado "anillo de Rowland" donde se puede establecer que la $B$ en el anillo vale:

$$B = \mu_a \cdot \frac{N \cdot i}{l}$$

![[Figura 2. Anillo de Rowland.png]]
**Figura 2.** Anillo de Rowland

Si el anillo está arrollado en el vacío el valor de $\mu$ se denomina **"permeabilidad absoluta o permeabilidad del vacío"** y vale:

$$\mu_0 = 4\pi \cdot 10^{-7} \, \frac{\text{H}}{\text{m}}$$

Si $N$ es el número de espiras del anillo, $i$ es la corriente que circula en Amper y $l$ el largo de la línea media magnética, definimos la **"intensidad de campo o excitación magnética $H$"** medida en $[\text{A-v/m}]$ o simplemente $[\text{A/m}]$ a la relación:

$$H = \frac{N \cdot i}{l} \quad \left[\frac{\text{A}}{\text{m}}\right]$$

---

![[Figura 3. Bobina común en vacío.png]]
**Figura 3.** Bobina común en vacío

Si en lugar de un anillo de Rowland tomamos una bobina común en el vacío como se muestra en la figura 3, se cumple que:

$$H \approx \frac{N \cdot i}{l}$$

![[Figura 4. Bobina con núcleo magnético.png]]
**Figura 4.** Bobina con núcleo magnético

Pero si a la bobina le colocamos un núcleo magnético como se muestra en la figura 4, el valor de la inducción magnética valdrá:

$$B = \mu_0 \cdot \mu_r \cdot \frac{N \cdot i}{l}$$

Donde $\mu_r$ es un coeficiente que indica la relación entre la permeabilidad del vacío y la permeabilidad de la sustancia colocada en el campo magnético y se denomina **permeabilidad relativa**.

---

Resumiendo, las expresiones resultan:

$$B = \mu_0 \cdot \mu_r \cdot H$$

Donde:
- $H$ $[\text{A-v/m}]$
- $B$ $[\text{Wb/m}^2]$

En la técnica se utilizan el hierro y sus aleaciones para la construcción de los circuitos magnéticos, en la figura 5 vemos las curvas de imantación $B = f(H)$ con las que trabajan normalmente en el cálculo de dichos circuitos.

![[Figura 5. Curvas de imantación B.png]]
**Figura 5.** Curvas de imantación $B = f(H)$

---

## Leyes para resolver problemas de circuitos magnéticos

Efectuemos un repaso general de las leyes que se utilizan para resolver problemas de circuitos magnéticos:

$$\phi = B \cdot S = \mu_r \cdot \mu_0 \cdot \frac{N \cdot i}{l} \cdot S = \frac{N \cdot i}{\dfrac{l}{\mu_r \cdot \mu_0 \cdot S}}$$

- Al valor $N \cdot i$ se lo llama **fuerza magnetomotriz** y se la mide en $[\text{A-v}]$ y la señalaremos con $F = N \cdot i$
- Al valor $\dfrac{l}{\mu_r \cdot \mu_0 \cdot S}$ se lo llama **reluctancia**, y se mide en $\text{Henry}^{-1}$ y lo indicaremos con ***R***:

$$\mathcal{R} = \frac{l}{\mu_r \cdot \mu_0 \cdot S}$$

Luego, el valor del flujo magnético resulta:

$$\phi = \frac{F}{\mathcal{R}}$$

Que nos indica que el flujo es función de la fuerza magnetomotriz y de la reluctancia.

Esta ley se denomina **Ley de Ohm de los circuitos magnéticos** por su similitud con la ley para los circuitos eléctricos o también **[[S01-2 Tema 01 - Los circuitos magnéticos|Ley de Hopkinson]]**.

---

## La resolución de circuitos magnéticos

El cálculo de los circuitos magnéticos implica recurrir a curvas del tipo $B = f(H)$, lo que nos obliga a la utilización de métodos gráficos. Por lo tanto, el grado de exactitud está condicionado a esta forma de operación.

La permeabilidad relativa $\mu_r$ puede ser escrita como:

$$\mu_r = \frac{B}{\mu_0 \cdot H}$$

Sin embargo, la relación entre la inducción magnética $B$ y la intensidad de campo $H$ **no es lineal** ni tiene formas matemáticas de fácil expresión. Por lo tanto, basándonos en la analogía existente entre la Ley de Hopkinson y la Ley de Ohm podemos afirmar que todo lo dicho en la resolución de circuitos eléctricos es aplicable a la resolución de los circuitos magnéticos.

---

## Método de resolución directa para un circuito magnético excitado con corriente continua

El problema usual es, conociendo las dimensiones, el material y el número de espiras de la bobina excitadora, determinar qué corriente continua es necesaria para crear un flujo constante de valor conocido.

### Datos necesarios

- Flujo constante $\phi$
- Las dimensiones (secciones, longitudes, etc.)
- Material [curva $B = f(H)$]
- Número de espiras de la bobina excitadora

### Incógnita

- Valor de la corriente continua necesaria para establecer el valor de flujo constante conocido $i$ $[\text{A}]$.

### Pasos para la resolución

Revisemos los pasos para resolver un problema de circuito magnético (con núcleo y entrehierro) excitado con corriente continua, tomando como referencia la figura 6:

1. Calculamos el valor de la inducción en el hierro $B_{fe}$ como:

$$B_{fe} = \frac{\phi}{S_{fe}}$$

2. Con este valor entramos en la curva $B = f(H)$ para el material del circuito magnético (en este caso, hierro) y obtenemos el valor de la intensidad de campo que es capaz de provocarla: con $B_{fe} \Longrightarrow$ determino $H_{fe}$

3. Conociendo las dimensiones del núcleo calculamos el largo $l_{fe}$ de la línea media magnética, que es la línea promedio de todas las líneas de flujo que pueden existir en el núcleo.

4. Con $H_{fe}$ y $l_{fe}$ aplicando la Ley de circuitación calculamos los ***N x i*** necesarios a saber:

$$H_{fe} \cdot l_{fe} = (N \cdot i)_{fe}$$

5. Como se conoce el número de espiras $N$ de la bobina se obtiene la corriente necesaria para crear el flujo $\phi$:

$$i = I = \frac{(N \cdot i)_{fe}}{N}$$

![[Figura 6. Transformador con núcleo laminado y entrehierro.png]]
**Figura 6.** Transformador con núcleo laminado y entrehierro

### Resolución de un ejercicio con núcleo laminado y entrehierro

A partir de la figura 6, debemos calcular la **"sección efectiva"** de hierro atento a que es laminado y no macizo, luego introducimos un coeficiente denominado **"factor de laminación"** $K_{fe}$ que suele valer **0,90 a 0,95**.

Luego la sección del hierro vale:

$$S_{fe} = K_{fe} \cdot S$$

Con este valor, repetimos el procedimiento detallado anteriormente y determinamos los $(N \cdot i)_{fe}$.

Solo queda determinar los amper-vueltas necesarios para crear el flujo en el entrehierro para lo cual seguimos el siguiente proceso:

1. Calculamos la sección ideal del entrehierro con la fórmula:

$$S_\delta = (a + \delta)(b + \delta)$$

Y con ella:

$$B_\delta = \frac{\phi}{S_\delta}$$

2. Con este valor, dado que el material del entrehierro es el aire y $\mu_r = 1$, la intensidad de campo $H$ valdrá:

$$H_\delta = \frac{B_\delta}{\mu_0}$$

3. Aplicando la ley de circuitación para el entrehierro:

$$H_\delta \cdot \delta = (N \cdot i)_\delta$$

4. Tomando ahora todo el circuito magnético:

$$H_{fe} \cdot l_{fe} + H_\delta \cdot l_\delta = (N \cdot i)_{fe} + (N \cdot i)_\delta = (N \cdot i)$$

Donde:

$$i = I = \frac{(N \cdot i)}{N}$$

> [!info] Nota
> Normalmente, el sumando $(N \cdot i)_\delta$, que representa la tensión magnética en el entrehierro, es muy superior a la tensión magnética en el núcleo, por lo que los entrehierros se procura que sean pequeños.

---

## Bibliografía

- Ferro, G. (2016). *Circuitos Magnéticos*. En *Electrotecnia*. Universidad Nacional de Mar del Plata. Recuperado de [enlace](http://www3.fi.mdp.edu.ar/dtoelectrica/files/electrotecnia/e_im_9_circuitos_magneticos.pdf)
