---
title: Introducción a la semana 17 - Curvas características y máquina síncrona
curso: "[[Motores MOC]]"
unidad: 4
semana: 17
orden: 0
tipo: introduccion
tags:
  - curso/motores
  - tipo/introduccion
  - tema/motor-sincrono
  - tema/curva-par-velocidad
  - tema/placa-de-caracteristicas
  - tema/generador-sincrono
date: 2026-07-13
---

## Bienvenida

¡Te damos la bienvenida! En esta sesión de aprendizaje analizaremos las **curvas características del motor síncrono**, aprenderemos a leer la **placa de características** del motor asíncrono y estudiaremos la **máquina síncrona trifásica**, incluido su **funcionamiento como generador**.

## Material de estudio: H5P (recurso interactivo)

Recurso interactivo H5P embebido en el portal — **crucigrama** de apertura para repasar los conceptos del **motor síncrono**.

🔗 [Abrir recurso H5P](https://canvasutp.h5p.com/content/1292242301690232868/embed)

> [!question] Crucigrama de apertura: conceptos del motor síncrono
> Antes de empezar, repasemos la terminología del motor síncrono. Intenta resolver cada pista antes de mirar la columna de respuestas.
>
> | # | Pista | Respuesta |
> | --- | --- | --- |
> | 1 | Es la parte giratoria del motor síncrono que está magnetizada y se mueve sincronizadamente con el campo magnético producido por el estator. | **ROTOR** |
> | 2 | Es la parte estática del motor que contiene las bobinas de cobre que generan el campo magnético que interactúa con el rotor. | **ESTATOR** |
> | 3 | El control de ________ en los motores síncronos puede lograrse mediante la variación de la frecuencia de alimentación o mediante el ajuste del voltaje aplicado al motor, lo que permite adaptarse a diferentes condiciones de carga y requisitos de operación. | **VELOCIDAD** |
> | 4 | Es un tipo de motor eléctrico en el cual la velocidad de rotación está sincronizada con la frecuencia de la corriente eléctrica suministrada. | **SÍNCRONO** |
> | 5 | En un motor síncrono, este es generado por un imán permanente o por una corriente continua en el rotor para crear el par de torsión necesario para la rotación. | **CAMPO MAGNÉTICO** |
> | 6 | Es la fuerza de rotación producida por el motor síncrono. En un motor síncrono, el ____ de torsión es proporcional a la intensidad del campo magnético y a la corriente en el rotor. | **PAR** |
> | 7 | El motor síncrono puede requerir un __________ especial para alcanzar su velocidad de sincronización. Esto puede ser necesario debido a la inercia del rotor y otros factores. | **ARRANCADOR** |
> | 8 | Los motores síncronos pueden ayudar a mejorar el factor de _________ de un sistema eléctrico al compensar la energía reactiva. Esto es útil en aplicaciones donde se quiere reducir el costo de la energía eléctrica y optimizar la eficiencia del sistema. | **POTENCIA** |
> | 9 | Los motores síncronos se utilizan en una variedad de aplicaciones ___________ donde se requiere un control preciso de la velocidad y alta eficiencia, como en compresores, bombas, ventiladores y en la generación de energía. | **INDUSTRIALES** |

> [!tip] Las tres ideas que deja el crucigrama
> 1. El **rotor** del motor síncrono lleva el **campo magnético** (imán permanente o CC) y queda **enganchado** al campo giratorio del **estator**: su **velocidad** solo cambia si cambia la **frecuencia** de alimentación.
> 2. Ese enganche tiene un costo: el motor **no arranca solo** y necesita un **arrancador** especial para vencer la inercia y alcanzar el sincronismo.
> 3. A cambio, ajustando la excitación puede **compensar energía reactiva** y **mejorar el factor de potencia** de toda la planta — de ahí su uso **industrial** en compresores, bombas y ventiladores grandes.

## Mapa de la semana

> [!info] Del modelo interno al comportamiento externo de la máquina de CA
> La [[S16-8 Conclusiones semana 16|semana 16]] modeló el **motor de inducción** por dentro: circuito equivalente, flujo de potencia y par. Esta semana cierra la **Unidad 4** mirando la máquina **desde fuera**: las **curvas características** ($\tau$–$n$) y la **regulación de velocidad** del motor asíncrono, la lectura práctica de su **placa de características**, y la **máquina síncrona trifásica**, tanto como motor como en su **funcionamiento como generador**. Con ello queda completo el recorrido de las máquinas de corriente alterna, antes del **Examen Final** de la semana 18.

### Bloques de la semana

1. [[S17-1 Tema 01 - Curvas características del motor asíncrono y regulación de velocidad|Curvas características del motor asíncrono y regulación de velocidad]] — curva par-velocidad desde el circuito equivalente, equivalente de Thevenin, $\tau_{máx}$ y $s_{máx}$, y los cuatro métodos de regulación de velocidad.
2. [[S17-2 Ejercicio resuelto - Regulación de velocidad de motor de inducción (Video)|Ejercicio: regulación de velocidad de un motor de inducción]] — motor de rotor devanado 460 V / 25 hp: par máximo, par de arranque y efecto de duplicar $R_2$.
3. [[S17-3 Tema 02 - Análisis de la placa de característica del motor asíncrono|Análisis de la placa de características del motor asíncrono]] — valores nominales (potencia, voltaje, corriente, factor de potencia, velocidad, eficiencia), **clase NEMA de diseño** y letras de código.
4. [[S17-4 Tema 03 - Máquina síncrona trifásica|Máquina síncrona trifásica]] — par inducido $\tau_{ind} = k\,B_R \times B_S$, **circuito equivalente**, diagrama fasorial y curva **par-velocidad**.
5. [[S17-5 Tema 04 - Principio de funcionamiento como generador|Principio de funcionamiento como generador]] — la máquina síncrona operando como **generador** trifásico.
6. [[S17-99 Evaluación Semana 17 - Cuestionario de autoevaluación|📝 Cuestionario de autoevaluación]] — **no calificado**, de práctica, del 13 al 17 de julio.

## Logro de aprendizaje

El estudiante será capaz de **analizar las curvas características** ($\tau$–$n$) y los **métodos de regulación de velocidad** del **motor asíncrono**, **interpretar la placa de características** de un motor para verificar su aptitud frente a una carga, y **describir el funcionamiento de la máquina síncrona trifásica** tanto como **motor** como en su operación como **generador**.

## Utilidad e importancia

La **placa de características** es lo primero que se lee en planta: de ella dependen la conexión, la protección y la verificación de que el motor sirve para la carga. Y el **motor síncrono** aporta algo que ningún motor de inducción puede dar: velocidad **rigurosamente constante** y la capacidad de **compensar energía reactiva** para **mejorar el factor de potencia** de toda la instalación, reduciendo el costo de la energía. Comprender la **máquina síncrona como generador** es, además, la base de la **generación eléctrica** en centrales hidráulicas, térmicas y eólicas.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas eléctricas* (5.ª ed.). McGraw-Hill.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Introducción a la semana 17: Curvas características y máquina síncrona* [Material de estudio – H5P]. UTP+class.
