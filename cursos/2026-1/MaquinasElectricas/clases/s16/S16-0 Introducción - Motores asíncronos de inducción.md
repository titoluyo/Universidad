---
title: Introducción a la semana 16 - Motores asíncronos de inducción
curso: "[[Motores MOC]]"
unidad: 4
semana: 16
orden: 0
tipo: introduccion
tags:
  - curso/motores
  - tipo/introduccion
  - tema/motor-de-induccion
  - tema/jaula-de-ardilla
  - tema/circuito-equivalente
  - tema/potencia-y-par
date: 2026-07-06
---

## Bienvenida

¡Te damos la bienvenida! En esta sesión de aprendizaje estudiaremos el **motor asíncrono de inducción trifásico**: su **principio de funcionamiento**, su **circuito equivalente** y el balance de **potencia y par**.

La historieta de apertura plantea el caso de una **inyectora de plástico**, la máquina que funde el plástico y lo inyecta en moldes para crear piezas con formas específicas. El ingeniero le explica a María que su motor —**por lo general un motor trifásico de jaula de ardilla**— es el encargado de generar la **presión** necesaria para inyectar el plástico fundido en el molde con precisión y rapidez. De él dependen la **potencia** y la **eficiencia** del proceso: cuanto más potente sea el motor, más rápido se producen las piezas y con mejor calidad; y cuanto más eficiente sea, menores serán los **costos de producción** y el **tiempo de ciclo**. El motor no solo importa para el funcionamiento de la máquina, sino para la **calidad y la productividad** de las piezas que produce.

> [!info] Material original
> Historieta de introducción del docente: [S16-Introduccion.pdf](attachments/S16-Introduccion.pdf) (UTP, Semana 16).

## Mapa de la semana

> [!info] Del campo giratorio al motor de inducción real
> La [[S15-8 Conclusiones semana 15|semana 15]] estableció el marco de las **máquinas de corriente alterna**: el **campo magnético giratorio**, la **velocidad de sincronismo** $n_1 = \dfrac{60 f_1}{p}$ y el **deslizamiento** $s$. Esta semana bajamos al detalle del protagonista industrial: el **motor asíncrono de inducción**. Veremos cómo se construye (rotor de **jaula de ardilla** vs. **devanado**), cómo se modela eléctricamente —resulta ser **un transformador giratorio**— y cómo se contabilizan la **potencia** y el **par** desde la red hasta el eje.

### Bloques de la semana

1. [[S16-1 Tema 01 - Principio de funcionamiento de las máquinas asíncronas trifásicas|Principio de funcionamiento de las máquinas asíncronas trifásicas]] — aspectos constructivos, rotor de jaula de ardilla y rotor devanado, desarrollo del **par inducido** ($\tau_{ind} = k\,B_R \times B_S$) y por qué el motor nunca alcanza el sincronismo.
2. [[S16-2 Tema 02 - Circuito equivalente de un motor de inducción|Circuito equivalente de un motor de inducción]] — el motor como **transformador giratorio**, modelo del circuito del rotor y circuito equivalente **por fase** referido al estator.
3. [[S16-3 Tema 03 - Potencia y par en los motores de inducción|Potencia y par en los motores de inducción]] — diagrama de **flujo de potencia**, potencia en el **entrehierro**, potencia convertida, pérdidas, **eficiencia** y par inducido vs. par de carga.
4. [[S16-4 Ejercicio resuelto - Ecuación de potencia (Video)|Ejercicio: ecuación de potencia]] — motor de $480\ \text{V}$, $50\ \text{hp}$: potencia en el entrehierro, convertida, de salida y eficiencia.
5. [[S16-5 Ejercicio resuelto - Ecuación de torque (Video)|Ejercicio: ecuación de torque]] — motor de $460\ \text{V}$, $25\ \text{hp}$, 4 polos, con $s = 2{,}2\ \%$: velocidad, corriente, factor de potencia, potencias, torques y eficiencia.
6. [[S16-99 Evaluación Semana 16 - AC Actividad de Participación (PA)|🔴 AC-S16 - Actividad de Participación (PA)]] — evaluación **calificada** (componente de la PA), 10–12 de julio.
7. [[S16-8 Conclusiones semana 16|Conclusiones]] — ideas clave de la sesión.

## Logro de aprendizaje

El estudiante será capaz de **explicar el principio de funcionamiento del motor asíncrono de inducción trifásico**, **distinguir** el rotor de **jaula de ardilla** del **devanado**, **construir e interpretar** su **circuito equivalente** por fase, y **calcular** el flujo de potencia, la **eficiencia** y los **pares** (inducido y de carga) a partir de los datos del motor y del deslizamiento.

## Utilidad e importancia

El **motor de inducción de jaula de ardilla** es el motor más usado en la industria: robusto, barato y de mantenimiento mínimo, mueve inyectoras, bombas, compresores, ventiladores y fajas. Saber calcular su **potencia de salida**, su **par** y su **eficiencia** es lo que permite **dimensionar** correctamente un accionamiento, estimar su **consumo** y justificar económicamente la elección de un motor de alta eficiencia frente a uno estándar.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas eléctricas* (5.ª ed.). McGraw-Hill.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Introducción a la semana 16: Motores asíncronos de inducción* [Infografía estática]. UTP+class.
