---
title: Las leyes del electromagnetismo
curso: "[[Motores MOC]]"
unidad: 1
semana: 1
orden: 3
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/ley-de-faraday
  - tema/ley-de-lenz
  - tema/fuerza-de-lorentz
  - tema/ley-de-biot-savart
date: 2026-03-28
---

Ahora que conocemos más sobre los campos y [[S01-2 Tema 01 - Los circuitos magnéticos|circuitos magnéticos]], es momento de profundizar en las leyes del electromagnetismo. Específicamente, hablaremos de la **ley de Faraday**, la **ley de Lenz**, las **corrientes de Foucault**, la **ley de Coulomb**, la **fuerza de Lorentz**, la **regla de la mano derecha** y la **ley de Biot Savart**.

## Revisa cada una de las leyes:

### Ley de Faraday

Hacia 1830, Michael Faraday, británico, y Joseph Henry, norteamericano, descubrieron la inducción electromagnética.

![[Pasted image 20260328224215.png]]

Supongamos tener como en la figura una bobina con una lamparita en serie. Si la bobina y el imán están en reposo relativo y el conjunto está libre de otras interacciones, la lamparita permanecerá apagada; si, en cambio, el imán se acerca bruscamente a la bobina, la lamparita destellará indicando que sobre ella apareció una fuerza electromotriz inducida por el movimiento del imán. La lamparita permanecerá encendida en tanto se mantenga el movimiento del imán; si este se detiene, no importa cuán cerca de la bobina, la lamparita se apagará. Si el imán se aleja de la bobina, la lamparita encenderá nuevamente hasta que este vuelva a detenerse. La lamparita será más brillante cuanto más rápido sea el movimiento del imán. El imán puede ser reemplazado por un electroimán, es decir, una bobina circulada por corriente que, como sabemos, producirá un campo magnético. En un circuito cerrado se produce una fuerza electromotriz proporcional a la variación temporal del flujo que enlaza.

La ley de la inducción de Faraday-Lenz dice que **la fuerza electromotriz inducida en un circuito es igual al valor negativo de la rapidez con la cual está cambiando el flujo que atraviesa el circuito**. La ecuación que define la ley de inducción de Faraday la podemos expresar como:

$$E = -\frac{d\phi}{dt}$$

El signo menos es una indicación del sentido de la fem inducida. Si la bobina tiene $N$ vueltas, aparece una fem en cada vuelta que se pueden sumar. Este es el caso de los toroides y solenoides, en estos casos la fem inducida será:

$$E = -N \cdot \frac{d\phi}{dt}$$

En resumen, la fuerza electromotriz inducida (Fem) en un circuito es proporcional a la rapidez con la que varía el flujo magnético que lo atraviesa, y directamente proporcional al número de espiras del inducido.

### Ley de Lenz

La ley de Lenz para el campo electromagnético relaciona cambios producidos en el campo eléctrico en un conductor con la variación de flujo magnético en dicho conductor, y afirma que los voltajes inducidos sobre un conductor y los campos eléctricos asociados son de un sentido tal que se oponen a la variación del flujo magnético que las induce. Por eso, en la ley de Faraday, tenemos un signo menos ($-$) al principio, ya que la fuerza electromotriz inducida en la bobina se opone a la variación de flujo magnético.

### Corrientes de Foucault

Las corrientes de Foucault se producen debido a inducción electromagnética de la Ley de Faraday en el interior de un material conductor como es el caso de un metal. La fuerza electromotriz inducida (femi) producirá corrientes en el interior del material debido a la baja resistencia eléctrica del mismo.

Las leyes de Faraday y de Lenz nos dicen que, si en un circuito varía el flujo de la inducción magnética, se genera en él una fuerza electromotriz inducida (**femi**) de tal sentido que trata de oponerse a la causa que lo produce. Este circuito puede ser simplemente una curva ideal en el vacío, en cuyo caso la **femi** no producirá ningún efecto detectable, pero para nuestra descripción electromagnética del espacio en base a campos es igualmente válida. 

**Una aplicación de las corrientes de Foucault son diferentes tipos de frenos magnéticos** utilizados en motores eléctricos, trenes, etc. y en motores eléctricos como los llamados de jaula de ardilla o los modernos alternadores de automóvil.

### Ley de Coulomb

La ley de Coulomb señala que **la fuerza $F$** (newton, N) **con que dos cargas eléctricas** $Q$ y $q$ (culombio, C) **se atraen o repelen es proporcional al producto de las mismas e inversamente proporcional al cuadrado de la distancia** $r$ (metro, m) **que las separa**:

$$F = \frac{k \cdot q_1 \cdot q_2}{r^2}$$

Donde:

- $F$: Magnitud de fuerza
- $k$: constante de Coulomb
- $q_1$ y $q_2$: Producto de dos cargas
- $r^2$: cuadrado de la distancia de las cargas
- $N$: Newton

### Fuerza de Lorentz

La fuerza de Lorentz es la **fuerza ejercida por el campo electromagnético que recibe una partícula cargada o una corriente eléctrica**.

En resumen, según la expresión de la ley de Lorentz, la fuerza de Lorentz será:

- **Nula:**
    - Si la partícula no posee carga: $q = 0 \implies F = 0$.
    - Si la partícula está en reposo: $v = 0 \implies F = 0$.
    - Si la velocidad de la partícula es paralela al campo: $F = |q| \cdot v \cdot B \cdot \sin(0^\circ) \implies F = 0$.

- **Máxima:**
    - Si $v$ y $B$ son perpendiculares ($\alpha = 90^\circ$): $F = |q| \cdot v \cdot B \cdot \sin(90^\circ) = |q| \cdot v \cdot B$.

$$\vec{F} = \vec{F}_e + \vec{F}_m \quad (1)$$

$$\vec{F}_e = q\vec{E} \quad (2) \text{ (fuerza eléctrica)}$$

$$\vec{F}_m = q\vec{v} \times \vec{B} \quad (3) \text{ (fuerza magnética)}$$

$$\vec{F} = q\vec{E} + q\vec{v} \times \vec{B} \quad (4)$$

Donde:

- $q$ = carga eléctrica (C)
- $\vec{E}$ = intensidad del campo eléctrico $\left(\frac{V}{m}\right)$
- $\vec{v}$ = velocidad de la carga $\left(\frac{m}{s}\right)$
- $\vec{B}$ = densidad de flujo magnético (T)

### Regla de la mano derecha

La regla de la mano derecha es básica para estudiar el comportamiento de los campos magnéticos. Veamos el siguiente video para descubrir de qué trata.

[Video: regla de la mano derecha](https://www.youtube.com/watch?v=PyTS_IDGOE0)

### Ley de Biot-Savart

Al igual que una carga origina un campo eléctrico o una masa un campo gravitatorio, un elemento de corriente genera un campo magnético. Biot y Savart llegaron a la conclusión de que, al circular una corriente por un conductor, esta genera un campo magnético.

![[Pasted image 20260328225601.png]]

La expresión matemática que define esta ley es:

$$d\vec{B} = \frac{\mu_0}{4\pi} \frac{I \cdot d\vec{s} \times \hat{r}}{r^2} \quad \text{(forma diferencial)}$$

$$\vec{B} = \frac{\mu_0 \cdot I}{4\pi} \int \frac{d\vec{s} \times \hat{r}}{r^2} \quad \text{(campo magnético total a partir de la integral)}$$

## Bibliografía

- Departamento de Física Aplicada III. (21 de junio de 2013). _Ley de Lorentz_. Universidad de Sevilla. Recuperado el 10 de marzo del 2024 de [https://acortar.link/KDCVoF](https://acortar.link/KDCVoF)
- Rodríguez, M. (2014). _Materiales y circuitos magnéticos_. Universidad de Cantabria.
