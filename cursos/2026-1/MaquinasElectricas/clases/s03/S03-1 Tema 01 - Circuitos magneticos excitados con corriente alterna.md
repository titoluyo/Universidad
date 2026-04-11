---
title: Circuitos magneticos excitados con corriente alterna
curso: "[[Motores MOC]]"
unidad: 1
semana: 3
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/corriente-alterna
  - tema/circuito-magnetico
  - tema/espira
  - tema/campo-magnetico-giratorio
  - tema/motor-electrico
date: 2026-04-11
---

## Circuito magnético alimentado con corriente continua

La [[S01-2 Tema 01 - Los circuitos magnéticos|ley de Hopkinson]] expresada por la ecuación:

$$\phi = \frac{F}{\mathcal{R}}$$

Donde:
- $\phi$: flujo
- $F$: f.m.m.
- $\mathcal{R}$: reluctancia

Al aplicar una tensión de alimentación de corriente continua (c.c.) a la bobina, se producirá, de acuerdo con la ley de Ohm, una corriente $I = \frac{V}{R}$, que dará lugar a una f.m.m. $F = N \cdot i$, y que según sea el valor de la reluctancia del circuito magnético determinará el flujo resultante $\phi = \frac{F}{\mathcal{R}}$.

![[Figura 1 . Sucesión de efectos en una bobina alimentada con c.c..png]]
**Figura 1.** Sucesión de efectos en una bobina alimentada con c.c.

## Circuito magnético alimentado con corriente alterna

Supongamos ahora que la bobina de la Figura 2 se alimenta con una tensión de corriente alterna (c.a.) senoidal:

$$v(t) = \sqrt{2} \cdot V \cdot \cos \, \omega t$$

Donde:
- $V$ expresa el valor eficaz de la tensión alterna aplicada.
- $\omega = 2 \cdot \pi \cdot f$ expresa la pulsación de la misma.

![[Figura 2. Bobina con núcleo de hierro.png]]
**Figura 2.** Bobina con núcleo de hierro

En este caso, se producirá una corriente de circulación **i(t)** que provocará un flujo $\phi$**(t)** en el núcleo. Este flujo variable dará lugar a una f.e.m. inducida en la bobina, de tal modo que si se aplica el segundo lema de Kirchhoff al circuito eléctrico de la Figura 1 se cumplirá:

$$v = R \cdot i + N \frac{d\phi}{dt}$$

Suponiendo que la caída de tensión en la resistencia de la bobina es pequeña en comparación con la f.e.m. inducida, la ecuación se puede escribir:

$$v = N \frac{d\phi}{dt}$$

De donde se deduce el valor del flujo $\phi(t)$:

$$\phi(t) = \frac{1}{N} \int v \, dt = \frac{\sqrt{2}}{N \cdot \omega} \cdot V \cdot \text{sen} \, \omega t$$

Donde el flujo máximo:

$$\phi_m = \frac{\sqrt{2} \cdot V}{N \cdot \omega}$$

Y teniendo en cuenta que $\omega = 2 \cdot \pi \cdot f$:

$$\boxed{V = \frac{2\pi}{\sqrt{2}} \cdot f \cdot N \cdot \phi_m = 4{,}44 \cdot f \cdot N \cdot \phi_m}$$

> [!important] Conclusión
> Por tanto, cuando la bobina se alimenta con una excitación de c.a., el flujo es función directa de la magnitud y frecuencia de la tensión aplicada, pero es absolutamente independiente de la naturaleza y características magnéticas del material que constituye el núcleo.

---

## Espira y su funcionamiento en un campo magnético

Se denomina espira a un circuito cerrado y plano. Cuando situamos esta espira en una zona del espacio con un campo magnético uniforme ($B$), experimenta una fuerza determinada, la cual se describe mediante la expresión para la fuerza en un conductor curvo. En este contexto específico:

$$\vec{F} = I \oint (\vec{dl}) \times \vec{B} = 0$$

Ya que la suma de todos los vectores $dl$ sobre una trayectoria cerrada es nula. Es decir, **la fuerza neta ejercida por un campo $B$ uniforme sobre un circuito cerrado de corriente es nula.**

Sin embargo, la espira no permanece en reposo ya que el momento ejercido por las fuerzas magnéticas es distinto de cero. Según la ecuación de la dinámica de rotación, este hecho provoca un giro en la espira de modo que la aceleración angular adquirida sea paralela al momento de las fuerzas. Analizamos como ejemplo el movimiento de una espira rectangular.

Se trata de una espira rectangular de lados **a** y **b** situada en un campo magnético **B** uniforme, contenido en el plano de la espira. Calculamos la fuerza neta que ejerce el campo sumando la fuerza sobre cada uno de los lados. La fuerza es nula sobre cada uno de lados **a**, por ser el campo paralelo al conductor.

Aplicamos la expresión para la fuerza sobre un conductor rectilíneo para cada lado **b** (**lado 1 y lado 2**):

![[Figura 3. Bobina en un campo magnético.png]]
**Figura 3.** Bobina en un campo magnético

![[Figura 4. Lado 1.png]]
**Figura 4.** Lado 1

![[Figura 5. Lado 2.png]]
**Figura 5.** Lado 2

El resultado es un par de fuerzas (igual módulo y sentido opuesto) que ejercen un momento ($\tau$) con respecto al centro del lado $a$, tal y como se muestra en la imagen frontal de la espira. Como los momentos ejercidos por ambas fuerzas tienen el mismo sentido, el módulo del momento resultante vendrá dado por la expresión:

$$\tau = \frac{a}{2} F_1 + \frac{a}{2} F_2 = 2 I b B \frac{a}{2} = I \cdot B \cdot a \cdot b = I \cdot B \cdot A$$

Donde **A** es el área de la espira.

![[Figura 6.png]]
**Figura 6.** Vista frontal de la espira con par de fuerzas

Debido al momento resultante de las fuerzas, la espira adquiere una aceleración angular paralela a dicho momento y se produce una rotación. Generalicemos este resultado cuando el campo **B** no está contenido en el plano de la espira.

### Momento magnético de una espira $\mu$

Definimos una nueva magnitud, llamada momento magnético de la espira **μ** que es independiente del campo magnético y que sólo tiene en cuenta las características del conductor (intensidad de corriente y área). El vector área **A** tiene de módulo el área de la espira, dirección perpendicular al plano que la contiene y sentido el que da la regla de la mano derecha según el sentido de la corriente eléctrica:

$$\vec{\mu} = I \cdot \vec{A}$$

Las unidades del **μ** en el S.I. son $\text{A} \cdot \text{m}^2$.

La expresión general para el momento de las fuerzas queda:

$$\vec{\tau} = \vec{\mu} \times \vec{B}$$

Que coincide con el resultado obtenido en el ejemplo anterior cuando **μ** y **B** son perpendiculares.

![[Figura 7. Regla de la mano derecha.png]]
**Figura 7.** Regla de la mano derecha

El momento de las fuerzas, y la aceleración angular, dependerá del ángulo **θ** entre **μ** y **B**. Si la espira está colocada con su momento paralelo al campo (el plano de la espira es perpendicular al campo) el momento de las fuerzas es nulo y la espira no sufre ninguna rotación.

![[Figura 8. Momentos de las fuerzas.png]]
**Figura 8.** Momentos de las fuerzas

En síntesis, debido al momento de las fuerzas magnéticas, una espira en un campo magnético **B** adquiere una aceleración angular, es decir, gira, de modo que **su momento magnético μ tiende a colocarse paralelo al campo magnético**.

> [!tip] Principio fundamental
> ***Este constituye el principio de funcionamiento de los motores eléctricos.***

---

## Campo magnético giratorio

Cuando un campo magnético es generado por el estator de una máquina de corriente alterna, mientras que el otro campo magnético proviene del rotor de la máquina, se generará un par en el rotor. Este par provocará que el rotor gire y se alinee con el campo magnético producido por el estator.

Si hubiera una manera de hacer girar el campo magnético del estator, entonces el par inducido en el rotor provocaría que "persiguiera" constantemente en círculos al campo magnético del estator. Esto, en breves palabras, es el principio básico de la operación de un motor de c.a.

### ¿Cómo se puede lograr que el campo magnético del estator gire?

El caso más sencillo de un campo magnético giratorio es un estator vacío que contiene tres bobinas, cada una separada por 120°. Debido a que tal devanado solo produce un polo magnético norte y uno sur, es un devanado de dos polos. Para comprender el concepto de un campo magnético giratorio, se aplica un grupo de corrientes al estator y se ve el resultado en momentos específicos de tiempo.

Suponiendo que las corrientes en las tres bobinas se obtienen de las ecuaciones:

$$i_{aa'}(t) = I_M \cdot \text{sen} \, \omega t \, \text{A}$$

$$i_{bb'}(t) = I_M \cdot \text{sen} (\omega t - 120°) \, \text{A}$$

$$i_{cc'}(t) = I_M \cdot \text{sen} (\omega t - 240°) \, \text{A}$$

La corriente $i_{aa'}$ en la bobina fluye hacia el extremo **a** de la bobina y sale por el extremo **a'** de ella. Produce la intensidad de campo magnético $H_{aa'}$ y de la misma forma, en las bobinas bb' y cc' se producen los campos magnéticos $H_{bb'}$ y $H_{cc'}$:

$$H_{aa'}(t) = H_M \cdot \text{sen} \, \omega t \, |0° \quad \text{A.vueltas/m}$$

$$H_{bb'}(t) = H_M \cdot \text{sen} (\omega t - 120°) \, |120° \quad \text{A.vueltas/m}$$

$$H_{cc'}(t) = H_M \cdot \text{sen} (\omega t - 240°) \, |240° \quad \text{A.vueltas/m}$$

![[Figura 8. Un estator trifásico simple. Vector de Haa en el estator.png]]
**Figura 8.** a) Un estator trifásico simple. b) Vector de $H_{aa'}$ en el estator.

Estudiando los instantes de tiempo $\omega t = 0°$ y $\omega t = 90°$, el campo magnético neto resultante en ambos instantes se muestra en la figura 9:

![[Figura 9. Vector de campo magnético de un estator en el tiempo 0. Vector de campo en el estator en el tiempo 90.png]]
**Figura 9.** a) Vector de campo magnético de un estator en el tiempo $\omega t = 0°$, b) Vector de campo en el estator en el tiempo $\omega t = 90°$.

### Video demostrativo

[Video: Semana 3 - Demostración de un campo magnético giratorio](https://www.youtube.com/watch?v=HgnS_QXKWY8)

### Material descargable

- [Abrir .MP4](https://utp-prd-upload-file-storage.s3.amazonaws.com/pao/content/94e3c109-d9b4-4b29-9178-348632e021c5/Semana%2B3%2B-%2BVide_CPWIAZ.mp4)
- [Abrir .MP3](https://utp-prd-upload-file-storage.s3.amazonaws.com/pao/content/cf57f9f9-90af-4584-9909-7b29cdca5258/Semana%2B3%2B-%2BAudi_BEYYOI.mp3)
- [Abrir .PDF](https://utp-prd-upload-file-storage.s3.amazonaws.com/pao/content/1717cd7c-8395-49ce-b259-d8e6163616df/Semana%2B3%2B-%2BGuio_NNJFLG.pdf)

---

## Bibliografía

- Chapman, S. (2005). *Máquinas Eléctricas*. McGraw-Hill.
- Martín, T. & Serrano, A. (17 de marzo de 2009). *Espira*. Universidad Politécnica de Madrid. Recuperado de [enlace](https://www2.montes.upm.es/dptos/digfa/cfisica/magnet/espira.html)
