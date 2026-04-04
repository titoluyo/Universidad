---
title: "Introduccion a circuitos electronicos amplificadores"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 1
orden: 6
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/amplificador-de-potencia
  - tema/clases-de-amplificadores
date: 2026-03-31
---

## Datos del curso

- **Docente:** Mg. Ing. Jorge Luis Robles Bokun
- **Horario:** Lunes 18:30-20:00 y Martes 18:30-20:00 (sede central)
- **Ambientes:** 09B0404 (teoria) y Lab. Esp. Cktos electronicos 09B0104

## Logro general del curso

Al finalizar el curso, el estudiante desarrolla diferentes configuraciones de circuitos electronicos aplicados en problemas de ingenieria en cada una de sus etapas, a traves del calculo y los resultados numericos encontrados a partir de la simulacion.

## Logro de la Unidad 1

Amplificadores de potencia, Amplificador Diferencial (A.D.) y Amplificador Operacional (A.O.): analizar y disenar las diferentes clases de amplificadores, amplificadores diferenciales y operacionales en casos practicos.

## Repaso de saberes previos

### Modelo Pi del transistor BJT en AC

$$r_\pi = \frac{v_{be}}{i_b} = \frac{V_T}{I_{BQ}} = \frac{\beta V_T}{I_{CQ}}$$

$$g_m = \frac{I_{CQ}}{V_T}$$

Donde:
- $r_\pi$ = resistencia de entrada del modelo Pi
- $g_m$ = transconductancia
- $V_T \approx 26\,mV$ (voltaje termico a temperatura ambiente)

### Modulacion AM

La modulacion de amplitud (AM) es una tecnica esencial en comunicaciones electronicas, variando la amplitud de una onda portadora segun la senal de audio.

$$S(t) = A_c [1 + m(t)] \cos(2\pi f_c t)$$

Donde:
- $m(t) = A_m \cos(2\pi f_m t)$ = senal mensaje
- $c(t) = A_c \cos(2\pi f_c t)$ = senal portadora

## Introduccion a los amplificadores

Las etapas transistorizadas o de estado solido pueden desarrollar multiples funciones: **amplificar, modular, detectar, oscilar**, etc. Para lograr tal objetivo el transistor suele recibir en sus diversos electrodos la polarizacion conveniente.

- Cuando opera como **amplificador de RF o AF**, el transistor se polariza de tal forma que el ciclo de senal completo aparece amplificado en la salida.
- Cuando opera como **detector**, la salida es equivalente a solo la mitad del ciclo de entrada.

## Amplificador de potencia

Es la **ultima etapa** del transistor. Tiene la funcion principal de amplificar senales — no necesariamente la tension, sino tambien corriente — y transmitirla a la carga.

### Tipos de amplificadores

- Amplificadores de **potencia**
- Amplificadores de **tension**
- Amplificadores de **corriente**
- Amplificador de **transconductancia**
- Amplificador de **audiofrecuencia**
- Amplificadores clase A, B, AB, C

### Funcionamiento

Un amplificador puede trabajar de manera:
- **Pasiva:** variando la relacion entre voltaje y corriente, manteniendo constante la potencia (como un transformador)
- **Activa:** tomando la potencia de una fuente de alimentacion, aumentando la potencia de senal a su salida

## Clasificacion de amplificadores de potencia

### Amplificador de Clase A

Es la manera mas simple de un amplificador de potencia. Utiliza **un solo transistor** en configuracion emisor comun para producir una salida invertida.

- El transistor conduce durante **360°** (ciclo completo) de la senal de entrada
- Punto Q ubicado en el **centro** de la recta de carga
- **Baja distorsion**

> [!warning] Desventaja
> La clase A es **poco eficiente** (~25% sin transformador, ~50% con transformador). Para potencias altas (e.g. 50 W), el amplificador utiliza mucha corriente y genera alta temperatura.

### Amplificador de Clase B

El transistor amplifica la senal en **la mitad de su periodo** (180° o $\pi$).

- Utiliza **dos o mas transistores** (NPN y PNP) polarizados de tal manera que cada uno solo conduce durante un medio ciclo de la onda de entrada
- Punto Q ubicado en el **corte** de la recta de carga
- **Mayor eficiencia** (~78.5%) que clase A
- Presenta **distorsion por cruce** (crossover) cerca de 0 V

### Amplificador de Clase AB

Es un tipo **hibrido** que combina las caracteristicas fundamentales de los amplificadores Clase A y Clase B con el objetivo de aprovechar sus ventajas.

- Conduce ligeramente mas de 180° pero menos de 360°
- Reduce la distorsion de cruce de la clase B
- Eficiencia intermedia entre clase A y B

### Amplificador de Clase C

- El transistor conduce durante **menos de 180°** de la senal de entrada
- **Mayor eficiencia** (~90%) de todas las clases analogicas
- Se utiliza como **sintonizadores de audio** y en **transmision de altas frecuencias**
- Las estaciones de radiodifusion utilizan amplificadores clase C por su buen rendimiento de conversion

> [!abstract] Resumen de clases
>
> | Clase | Angulo de conduccion | Eficiencia | Distorsion | Aplicacion |
> | ----- | -------------------- | ---------- | ---------- | ---------- |
> | A | 360° | ~25-50% | Baja | Audio de alta fidelidad |
> | B | 180° | ~78.5% | Cruce por cero | Push-pull |
> | AB | 180° - 360° | Intermedia | Reducida | Audio de potencia |
> | C | < 180° | ~90% | Alta | RF, transmisores AM |

## Conclusiones

- El BJT se construye con tres regiones semiconductoras separadas por dos uniones P-N (NPN y PNP)
- Tiene 3 configuraciones: colector comun, base comun y emisor comun
- Las uniones P-N deben estar correctamente polarizadas con voltajes de CD externos
- Un transistor o multiples etapas se puede analizar en DC y AC
- Los circuitos moduladores se dividen en moduladores de bajo y alto nivel
- Los amplificadores clase C permiten la transmision de altas frecuencias con buen rendimiento de conversion
