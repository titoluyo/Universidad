---
title: "Tema 01 - Máquinas de corriente alterna"
curso: "[[Motores MOC]]"
unidad: 4
semana: 15
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/maquinas-de-corriente-alterna
  - tema/campo-magnetico-giratorio
  - tema/maquina-sincrona
  - tema/maquina-asincrona
  - tema/deslizamiento
date: 2026-06-29
---

> [!info] Material original
> Manual del docente: [S15-Manual-Maquinas-de-corriente-alterna.pdf](attachments/S15-Manual-Maquinas-de-corriente-alterna.pdf) (UTP, Semana 15).

Las **máquinas de corriente alterna (CA)** incluyen **generadores**, que transforman energía mecánica en energía eléctrica de CA, y **motores**, que convierten la energía eléctrica de CA en energía mecánica. Aunque los principios básicos son simples, la construcción de las máquinas reales puede ser complicada.

Con esta unidad se abandona el mundo de la corriente continua (motores shunt, serie y compuesto) para entrar en el de las máquinas alimentadas por redes trifásicas, que son las de uso industrial masivo.

## Principio de funcionamiento de una máquina de corriente alterna

### Campos magnéticos giratorios

El **estator** de una máquina eléctrica de inducción (motor) es **igual al del generador de CA**. En cambio el **rotor**, denominado **de jaula de ardilla**, es totalmente distinto: está formado por un cilindro de barras de cobre o de aluminio.

Estas barras se unen en sus extremos mediante **dos anillos de metal** (anillos de cortocircuito). Dado que **no existe conexión eléctrica entre el rotor y el estator**, la corriente que circula por el rotor es **inducida** por el campo magnético que crean las bobinas del estator. Este detalle es la clave de toda la máquina asíncrona: el rotor no se alimenta desde ninguna fuente, se "alimenta solo" por inducción.

En una **máquina trifásica**, las bobinas $B_1$, $B_2$ y $B_3$ están separadas **120 grados eléctricos** y sus extremos se conectan a una red trifásica, bien en **estrella** o bien en **triángulo**.

El campo magnético resultante originado por las tres bobinas **gira** y tiene **intensidad constante**: al desfasarse las tres corrientes 120° en el tiempo y estar las bobinas desfasadas 120° en el espacio, la suma vectorial de los tres campos da un vector de módulo fijo que rota. Ese **campo magnético giratorio** es el que arrastra al rotor.

## Tipos de máquinas de corriente alterna

Existen **dos clases principales** de máquinas de corriente alterna: las **máquinas síncronas** y las **máquinas de inducción** (también conocidas como **máquinas asíncronas**).

| Máquinas síncronas | Máquinas asíncronas (de inducción) |
| --- | --- |
| Son motores y generadores cuya **corriente de campo magnético es proporcionada por una fuente de potencia de CA externa**. | Son motores y generadores cuya **corriente de campo magnético se suministra a través de la inducción magnética**. |

Los **circuitos de campo** de la mayoría de las máquinas síncronas y de inducción están ubicados **en los rotores**.

### Máquinas síncronas

Se trata de máquinas con un **inductor alimentado por corriente continua (CC)**, también conocido como **devanado de excitación o campo**, típicamente ubicado en el **rotor** y alimentado mediante **dos anillos**.

El **inducido**, generalmente **trifásico**, se encuentra en el **estator**. En máquinas de baja potencia a menudo se invierte la posición, con el **inductor en el estator** y el **inducido en el rotor**, con **tres anillos** en este último.

Cuando funciona como **generador**, la energía mecánica se introduce por el eje y, al aplicar CC al inductor, se genera una **fuerza electromotriz (FEM)** en el inducido a una frecuencia específica. La CC necesaria para alimentar el inductor se obtiene de una pequeña **dinamo excitatriz** ubicada en el mismo eje de la máquina.

La **frecuencia de la carga** $f_L$, que coincide con la del inducido, es **directamente proporcional a la velocidad**:

$$f_L = f_2 = \pm\,\frac{n\,p}{60}$$

- $f_L$ = frecuencia de la carga.
- $f_2$ = frecuencia del inducido.
- $n$ = velocidad de giro del rotor (rpm).
- $p$ = número de **pares** de polos.

La máquina síncrona puede **operar como motor** al introducir corriente alterna de frecuencia $f_2$ en el inducido, con el inductor $f_1 = 0$ (está alimentado en CC, de ahí la frecuencia nula). Esto genera un **par en el rotor** que lo hace girar a una velocidad determinada:

$$n = \frac{60\,f_2}{p}$$

- $n$ = velocidad de giro (rpm).
- $f_2$ = frecuencia aplicada al inducido (Hz).
- $p$ = número de pares de polos.

La **magnitud del par** en el motor síncrono es **directamente proporcional a la frecuencia** (velocidad de sincronismo). Sin embargo, su **desventaja** es que **gira a una velocidad fija**, lo que puede causar **problemas de arranque** y **pérdida de sincronismo** ante bruscos pares de frenado. Por eso estos motores se emplean cuando se requiere una **alta constancia en la velocidad**, como en relojes eléctricos y ciertos servomecanismos.

### Máquinas asíncronas o de inducción

Son **máquinas rotativas**, $n \neq 0$, y se caracterizan por:

$$f_1 \neq 0 \qquad f_2 = f_1 \pm \frac{n\,p}{60} \qquad f_L = f_2$$

- $f_1$ = frecuencia del devanado inductor (estator).
- $f_2$ = frecuencia del devanado inducido (rotor).
- $f_L$ = frecuencia de la carga.
- $n$ = velocidad del rotor (rpm); $p$ = número de pares de polos.

Las máquinas de inducción tienen un **devanado inductor en el estator**, alimentado con corriente alterna de frecuencia $f_1$. Para máquinas con potencia superior a $1/2\ \text{CV}$, este devanado es **trifásico**, al igual que la corriente de alimentación, generando un **campo magnético giratorio** cuya velocidad se determina según:

$$n = \frac{60\,f_1}{p}$$

- $n$ = velocidad del campo giratorio, o **velocidad de sincronismo** (rpm).
- $f_1$ = frecuencia de alimentación del estator (Hz).
- $p$ = número de **pares** de polos (ojo: no el número de polos; 4 polos → $p = 2$).

En la **mayoría de los casos**, el rotor de la máquina de inducción está compuesto por **conductores cortocircuitados por dos anillos extremos**, formando la **jaula de ardilla**.

#### Funcionamiento como motor

En la situación de **motor**, el **campo giratorio del estator induce fuerzas electromotrices** en el devanado del rotor. Si el rotor está **en cortocircuito** (jaula de ardilla) o **conectado a través de un reóstato de arranque** (rotor devanado o con anillos), se generan **corrientes en el rotor**. Estas corrientes, al interactuar con el campo giratorio del estator, hacen que la máquina gire a una velocidad $n$ **muy cercana y ligeramente inferior a la velocidad de sincronismo** $n_1$. Esto se expresa mediante la **segunda identidad** de la ecuación característica:

$$f_2 = f_1 - \frac{n\,p}{60}$$

Aquí está la razón del nombre **asíncrona**: si el rotor alcanzara el sincronismo ($n = n_1$), no habría velocidad relativa entre el campo y las barras, no se induciría FEM, no habría corriente ni par. El motor **necesita quedarse atrás** para funcionar.

Se denomina **deslizamiento** $s$ al cociente:

$$s = \frac{n_1 - n}{n_1} = \frac{\dfrac{60\,f_1}{p} - n}{\dfrac{60\,f_1}{p}} = \frac{f_2}{f_1}$$

- $s$ = deslizamiento (adimensional; se expresa también en %).
- $n_1$ = velocidad de sincronismo (rpm).
- $n$ = velocidad real del rotor (rpm).
- $f_2$ = frecuencia del rotor; $f_1$ = frecuencia del estator.

La última igualdad, $s = f_2/f_1$, es especialmente útil: el deslizamiento se puede leer indistintamente como una **relación de velocidades** o como una **relación de frecuencias**.

#### Funcionamiento como generador

Si la máquina asíncrona, que funciona como motor a una velocidad $n$ **menor** que la de sincronismo $n_1$, es **forzada externamente** a girar su rotor a una velocidad **superior a la de sincronismo** y en la misma dirección, el **deslizamiento se vuelve negativo** según

$$s = \frac{n_1 - n}{n_1}$$

En esta situación, la máquina **absorbe energía mecánica y la convierte en energía eléctrica**, que es devuelta a la red a través del estator a una frecuencia $f_1$.

Aunque la máquina opera como generador, este método **rara vez se emplea en la práctica** debido a su **dependencia de la red eléctrica** para suministrar la corriente de magnetización necesaria. Sin embargo, existen técnicas de **autoexcitación de generadores asíncronos** utilizando **condensadores**.

## Frecuencia eléctrica del rotor

Un motor de inducción opera mediante la **inducción de voltajes y corrientes en el rotor** de la máquina, razón por la cual a menudo se le denomina **transformador rotatorio**. Similar a un transformador, el **primario (estator)** induce un voltaje en el **secundario (rotor)**; sin embargo, a diferencia de un transformador, **la frecuencia en el secundario no tiene que ser necesariamente igual a la frecuencia en el primario**.

El comportamiento se entiende con los dos casos extremos:

- Cuando el rotor de un motor **se bloquea**, su frecuencia será **la misma que la del estator**. Si la velocidad del rotor es $0\ \text{r/min}$, la frecuencia en el rotor es igual a la frecuencia del estator y el **deslizamiento es 1**.
- Si el rotor gira **a velocidad síncrona**, la frecuencia en el rotor será **cero**: $f_r = 0\ \text{Hz}$ y el **deslizamiento es 0**.

Para una velocidad de rotación **arbitraria** del rotor, la frecuencia del rotor es **proporcional a la diferencia** entre la velocidad del campo magnético síncrono y la velocidad del rotor. La frecuencia en el rotor se puede expresar como:

$$f_r = s \cdot f_e$$

- $f_r$ = frecuencia del rotor.
- $f_e$ = frecuencia del estator (campo magnético).
- $s$ = deslizamiento.

> [!summary] Idea central
> Toda máquina de CA trifásica parte del **campo magnético giratorio**: tres bobinas a 120° eléctricos alimentadas por una red trifásica producen un campo de **intensidad constante que rota** a la **velocidad de sincronismo** $n = \dfrac{60\,f_1}{p}$ (con $p$ = **pares** de polos). De ahí las dos familias: la **síncrona**, con inductor en CC y rotor "enganchado" al campo a velocidad fija ($n = 60f_2/p$), y la **asíncrona o de inducción**, cuyo rotor de jaula de ardilla se alimenta **solo por inducción** y debe girar **ligeramente por debajo** del sincronismo para que exista FEM, corriente y par. Esa diferencia relativa es el **deslizamiento** $s = \dfrac{n_1 - n}{n_1} = \dfrac{f_2}{f_1}$, que además fija la **frecuencia del rotor** $f_r = s\,f_e$ ($s=1$ a rotor bloqueado, $s=0$ en sincronismo) y se vuelve **negativo** cuando la máquina se arrastra por encima del sincronismo y pasa a **generador**. Aplicación numérica en [[S15-2 Ejercicio resuelto - Máquina asíncrona trifásica (Video)]]; el modelo eléctrico detallado se desarrolla en [[S16-2 Tema 02 - Circuito equivalente de un motor de inducción]] y el balance energético en [[S16-3 Tema 03 - Potencia y par en los motores de inducción]].

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
