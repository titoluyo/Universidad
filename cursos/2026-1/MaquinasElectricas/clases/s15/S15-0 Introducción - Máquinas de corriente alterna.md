---
title: Introducción a la semana 15 - Máquinas de corriente alterna
curso: "[[Motores MOC]]"
unidad: 4
semana: 15
orden: 0
tipo: introduccion
tags:
  - curso/motores
  - tipo/introduccion
  - tema/maquinas-de-corriente-alterna
  - tema/campo-magnetico-giratorio
  - tema/maquina-sincrona
  - tema/deslizamiento
date: 2026-06-29
---

## Bienvenida

¡Te damos la bienvenida! En esta sesión de aprendizaje **identificaremos los principios de funcionamiento de una máquina asíncrona de corriente alterna**, y los contrastaremos con los de la **máquina síncrona**.

## Material de estudio: H5P (recurso interactivo)

Recurso interactivo H5P embebido en el portal — presentación de apertura sobre los **campos magnéticos giratorios**, con tres preguntas de repaso.

🔗 [Abrir recurso H5P](https://canvasutp.h5p.com/content/1292241271421543278/embed)

### Actividad de repaso: campos magnéticos giratorios

Antes de empezar, recordemos algunos conceptos importantes sobre los campos magnéticos giratorios.

> [!question] 1. ¿Qué efecto se observa en un campo magnético giratorio?
> - ✅ **Generación de corriente eléctrica**
> - Atracción de materiales ferromagnéticos
> - Incremento de la intensidad magnética estática
> - Desviación de partículas cargadas
> - Anulación del campo magnético
>
> Un campo que **varía en el tiempo** respecto a un conductor induce en él una fuerza electromotriz y, si el circuito está cerrado, una **corriente**. Es exactamente el mecanismo que alimenta al rotor de jaula de ardilla, que no tiene ninguna conexión eléctrica con el estator.

> [!question] 2. ¿Cuál es la ley fundamental que describe el fenómeno del campo magnético giratorio?
> - Ley de Coulomb
> - Ley de Ampére
> - ✅ **Ley de Faraday**
> - Ley de Ohm
> - Ley de Gauss
>
> La **ley de Faraday** ($e = -\,d\phi/dt$) explica que la variación del flujo concatenado induce una FEM. La ley de Ampère describe cómo la corriente **crea** el campo; Faraday describe cómo el campo **variable** genera tensión, que es el efecto útil aquí.

> [!question] 3. ¿Cómo se puede aumentar la inducción de un campo magnético giratorio?
> - Disminuyendo la velocidad de rotación
> - Aumentando la distancia entre el imán y el objeto giratorio
> - Incrementando el tamaño del imán
> - Reduciendo el número de vueltas del objeto giratorio
> - ✅ **Incrementando el área del objeto giratorio expuesto al campo magnético**
>
> El flujo concatenado es $\phi = B \cdot A$: a **mayor área expuesta**, mayor flujo y mayor FEM inducida. Las otras opciones reducen la variación de flujo o la alejan del conductor.

## Mapa de la semana

> [!info] De la corriente continua a la corriente alterna
> La [[S14-8 Conclusiones semana 14|semana 14]] cerró la **Unidad 3** con el arranque, frenado y la regulación de velocidad de los motores DC. Con esta semana se abre la **Unidad 4**: las **máquinas de corriente alterna**, las de uso industrial masivo. El punto de partida es el **campo magnético giratorio** que producen tres bobinas a 120° eléctricos alimentadas por una red trifásica, y del cual nacen las dos grandes familias: la **síncrona** (rotor enganchado al campo, velocidad fija) y la **asíncrona o de inducción** (rotor alimentado solo por inducción, que debe girar **por debajo** del sincronismo → **deslizamiento**).

### Bloques de la semana

1. [[S15-1 Tema 01 - Máquinas de corriente alterna|Máquinas de corriente alterna]] — campo magnético giratorio, máquinas síncronas vs. asíncronas, velocidad de sincronismo $n = \dfrac{60 f_1}{p}$, **deslizamiento** $s = \dfrac{n_1 - n}{n_1} = \dfrac{f_2}{f_1}$ y frecuencia del rotor $f_r = s\,f_e$.
2. [[S15-2 Ejercicio resuelto - Máquina asíncrona trifásica (Video)|Ejercicio: máquina asíncrona trifásica]] — aplicación numérica de la velocidad de sincronismo, el deslizamiento y la frecuencia del rotor.
3. [[S15-99 Laboratorio 3 - Velocidad-tension y par-corriente motor cc excitacion independiente|🧪 Laboratorio Calificado 3 (LC3)]] — curvas **velocidad-tensión** y **par-corriente** del motor DC con excitación independiente; tarea **calificada** entregada (19/20).
4. [[S15-100 Laboratorio 3 - Resolucion desarrollo y resultados|LC3: resolución, desarrollo y resultados]] — mediciones, gráficas y análisis del informe.
5. [[S15-8 Conclusiones semana 15|Conclusiones]] — ideas clave de la sesión.

## Logro de aprendizaje

El estudiante será capaz de **explicar el principio de funcionamiento de las máquinas de corriente alterna** a partir del **campo magnético giratorio**, **distinguir** la máquina **síncrona** de la **asíncrona (de inducción)** según el origen de la corriente de campo, y **calcular** la velocidad de sincronismo, el **deslizamiento** y la frecuencia del rotor de un motor trifásico.

## Utilidad e importancia

Las máquinas de corriente alterna trifásicas son **el caballo de batalla de la industria**: bombas, ventiladores, compresores, fajas transportadoras y generación eléctrica. Comprender el campo giratorio y el **deslizamiento** es el requisito para todo lo que sigue —circuito equivalente, potencia y par del motor de inducción— y para interpretar correctamente la placa de características de cualquier motor en planta.

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Introducción a la semana 15: Máquinas de corriente alterna* [Material de estudio – H5P]. UTP+class.
