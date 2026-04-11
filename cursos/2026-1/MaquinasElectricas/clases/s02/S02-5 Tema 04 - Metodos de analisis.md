---
title: Metodos de analisis
curso: "[[Motores MOC]]"
unidad: 1
semana: 2
orden: 5
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/circuito-magnetico
  - tema/metodo-ensayo-error
  - tema/metodo-grafico
  - tema/curva-imanacion
date: 2026-04-11
---

Existen dos métodos de análisis que podemos aplicar para resolver problemas en [[S02-1 Tema 01 - Circuito magnetico excitado con corriente continua|circuitos magnéticos]], específicamente los compuestos de materiales ferromagnéticos. En esta ocasión, exploraremos el procedimiento de ensayo y error, y el procedimiento gráfico.

## Procedimiento de ensayo y error

En el caso en que la frecuencia magnetomotriz (f.m.m.) sirva como dato de referencia, la única manera de abordar la situación es a través de un proceso iterativo de prueba y error. Es decir, la resolución comienza al seleccionar un valor para $B$ y calcular la f.m.m. necesaria, la cual se compara con la aplicación real. Luego, se ajusta el valor de $B$ hacia arriba o hacia abajo con el fin de acercar la f.m.m. al valor original, repitiendo este proceso de manera sucesiva. Con un poco de práctica, el problema se resuelve generalmente en dos o tres iteraciones como máximo.

### Ejemplo

En la figura 1 se muestra un circuito magnético realizado con chapa magnética de acero al silicio y cuya curva de imanación se muestra en la figura 2. El entrehierro es de 1 mm, la longitud magnética media de la estructura de chapa es de 1 m y la sección transversal es uniforme de valor: 20 $\text{cm}^2$. Se nos pide calcular la inducción magnética en el entrehierro.

![[Figura 1. Circuito magnético.png]]
**Figura 1.** Circuito magnético

![[Figura 2. Curva de imanación.png]]
**Figura 2.** Curva de imanación

Para este caso, analizaremos el circuito eléctrico equivalente del sistema magnético de la figura 3. Inicialmente, asumiremos que, en el punto de operación del hierro, su permeabilidad relativa es aproximadamente $\mu_r$ = 1000. Esto implica que 1 metro de hierro debe exhibir la misma reluctancia magnética que 1 milímetro de aire (entrehierro), estas dos distancias se representan en la figura 1 de este caso.

![[Figura 3. Curva de imanación.png]]
**Figura 3.** Circuito eléctrico equivalente

La f.m.m. de la bobina es:

$$\mathcal{F} = N \cdot i = 750 \times 2 = 1500 \text{ A.v}$$

Si, según nuestra suposición, las reluctancias $\mathcal{R}_{fe}$ y $\mathcal{R}_{e}$ se consideran iguales, la diferencia de potencial magnética (d.d.p.) entre los nodos 1 y 2 será idéntica a la d.d.p. entre 2 y 3, y tendrá un valor de 1500/2 = 750 A.v. Esto implica que tanto el hierro como el entrehierro requieren una fuerza magnetomotriz (f.m.m.) de la bobina equivalente a 750 A.v. Ahora bien, dado que la reluctancia del entrehierro es:

$$\mathcal{R}_e = \frac{l_e}{\mu_0 S} = \frac{1 \times 10^{-3}}{4\pi \times 10^{-7} \times 20 \times 10^{-4}} = 3{,}98 \times 10^{5} \, [\text{H}^{-1}]$$

Según la [[S01-2 Tema 01 - Los circuitos magnéticos|ley de Hopkinson]], el flujo magnético y la inducción correspondiente en el entrehierro serán respectivamente:

$$\phi_e = \frac{F}{\mathcal{R}_e} = \frac{750}{3{,}98 \times 10^{5}} = 1{,}88 \, \text{mWb} \quad \Longrightarrow \quad B_e = \frac{\phi_e}{S} = \frac{1{,}88 \times 10^{-3}}{20 \times 10^{-4}} = 0{,}94 \, \text{Teslas}$$

Dado que se trata de un circuito magnético en serie, la inducción previamente mencionada en el entrehierro será la misma que se presentará en la chapa magnética. Por lo tanto, al examinar la curva de imanación de la figura 2 con esta inducción en el entrehierro, se observa que la chapa magnética requiere un campo magnético del orden de 100 A.v/m. Dado que la longitud del hierro es de 1 metro, esto equivale a 100 A.v, lo cual es significativamente inferior al valor anticipado de 750 A.v.

### Segunda iteración ($B = 1{,}5$ T)

Este hecho indica que la inducción de 0,94 teslas obtenida con la suposición inicial ha quedado por debajo del valor real necesario para la estructura magnética. Por lo tanto, se optará por aumentar la inducción de trabajo a un valor, por ejemplo, de 1,5 teslas. En este caso, el campo en el entrehierro será entonces:

$$H_e = \frac{B_e}{\mu_0} = \frac{1{,}5}{4\pi \times 10^{-7}} = 11{,}94 \times 10^{5} \, \text{A.v/m}$$

De este modo la *d.d.p.* magnética en el entrehierro (entre los nudos 2 y 3 de la figura 3) será:

$$U_{23} = H_e \cdot l_e = 11{,}94 \times 10^{5} \times 1 \times 10^{-3} = 1194 \, \text{A.v}$$

Para calcular la d.d.p. magnética en el hierro (entre los nudos 1 y 2 de la figura 3) es preciso ver primero el campo magnético que requiere el hierro para la inducción de 1,5 teslas. La curva de imanación de la figura 2 nos indica que se necesitan unos 510 A.v/m, por lo que la f.m.m. $U_{12}$ será:

$$U_{12} = H_{Fe} \cdot l_{Fe} = 510 \times 1 = 510 \, \text{A.v}$$

Lo que requerirá una *f.m.m.* total en la bobina:

$$F = U_{12} + U_{23} = 1194 + 510 = 1704 \, \text{A.v}$$

Que es superior al valor de 1500 A.v que tiene la bobina según indica el enunciado, pero se acerca bastante a ella. Es preciso entonces reducir un poco la inducción de prueba.

### Tercera iteración ($B = 1{,}4$ T)

Probemos ahora con 1,4 teslas, que es un valor algo inferior al anterior. En este caso el campo en el entrehierro tendrá un valor:

$$H_e = \frac{B_e}{\mu_0} = \frac{1{,}4}{4\pi \times 10^{-7}} = 1{,}11 \times 10^{6} \, \text{A.v/m}$$

Por consiguiente, la diferencia de potencial magnético en el entrehierro será:

$$U_{23} = H_e \cdot l_e = 1{,}11 \times 10^{6} \times 1 \times 10^{-3} = 1110 \, \text{A.v}$$

Se calcula la ***d.d.p.*** magnética en el hierro. Como quiera que la inducción en el hierro es también de 1,4 Teslas, la curva de imanación de la figura 2 nos indica que el campo magnético en el hierro es de 400 A.v/m por lo que la **f.m.m.** $U_{12}$ será:

$$U_{12} = H_{Fe} \cdot l_{Fe} = 400 \times 1 = 400 \, \text{A.v}$$

Lo que requerirá una **f.m.m.** total en la bobina:

$$F = U_{12} + U_{23} = 1110 + 400 = 1510 \, \text{A.v}$$

Que coincide prácticamente con la **f.m.m.** que tiene la bobina. Es decir, **la inducción magnética en el entrehierro es prácticamente de 1,4 teslas**.

---

## Procedimiento gráfico

De acuerdo con el circuito eléctrico equivalente de la Figura 3, la **f.m.m.** de la bobina es igual a la suma de las ***d.d.p.*** magnético entre los nudos 1 y 2 (hierro) y 2-3 (entrehierro) es decir:

$$F = Ni = H_{Fe} \cdot l_{Fe} + H_e \cdot l_e$$

Y al despejar el campo magnético en el hierro resulta la siguiente ecuación:

$$H_{Fe} = \frac{Ni}{l_{Fe}} - \frac{H_e \cdot l_e}{l_{Fe}} \quad \text{...(a)}$$

Y como quiera que la inducción magnética en el entrehierro coincide con la del hierro (circuito serie), el valor del campo en el entrehierro es:

$$H_e = \frac{B_e}{\mu_0} = \frac{B_{Fe}}{\mu_0}$$

Que al llevar a la ecuación (a) da lugar a:

$$H_{Fe} = \frac{Ni}{l_{Fe}} - \frac{B_{Fe} \cdot l_e}{\mu_0 \cdot l_{Fe}} \quad \text{...(b)}$$

Que es la ecuación de una recta que relaciona la inducción y el campo magnético en el hierro. Al dibujar esta recta en el gráfico de la curva de imanación del hierro, tal como se muestra en la figura 2, la intersección con esta curva nos da directamente el resultado. Al sustituir valores numéricos en (b), la ecuación de la recta viene expresada por:

$$H_{Fe} = \frac{1500}{1} - \frac{B_{Fe}}{4\pi \times 10^{-7}} \cdot \frac{10^{-3}}{1} = 1500 - 796 \cdot B_{Fe}$$

La intersección de esta recta con el eje de ordenadas es:

$$H_{Fe} = 0 \quad \Longrightarrow \quad B_{Fe} = \frac{1500}{796} = 1{,}88 \, \text{T}$$

Que corresponde al **punto A** de la figura 2. La intersección con el eje de abscisas es:

$$B_{Fe} = 0 \quad \Longrightarrow \quad H_{Fe} = 1500 \, \text{A.v/m}$$

![[Figura 2. Curva de imanación.png]]
**Figura 2.** Curva de imanación (con recta de carga)

Que corresponde al **punto B** de la figura 2. De este modo se puede dibujar la recta y la intersección de la misma con la curva de imanación da lugar al **punto C** que corresponde a una inducción magnética de prácticamente **1,4 teslas** y a un campo magnético necesario de 400 A.v/m; y como la longitud del hierro es de 1 metro, corresponden a una **f.m.m.** de 400 A.v por lo que el resto de 1500 − 400 = 1100 A.v será la **f.m.m.** requerida por el entrehierro, valores que coinciden con los obtenidos con el procedimiento anterior de ensayo y error.

---

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6ta. ed.). McGraw-Hill Interamericana.
