---
title: "Amplificadores de potencia - Clase A"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 2
orden: 3
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/amplificador-de-potencia
  - tema/amplificador-clase-a
  - tema/eficiencia
date: 2026-03-31
---

## Clases de amplificacion

Las etapas transistorizadas pueden desarrollar multiples funciones: amplificar, modular, detectar, oscilar, etc. Segun la polarizacion del transistor, se clasifican en:

| Clase | Senal de salida | Descripcion |
| ----- | --------------- | ----------- |
| **A** | Ciclo completo | La senal de salida circula todos los periodos |
| **B** | Medio ciclo | La senal de salida circula solo un semiperiodo |
| **AB** | Mas de medio ciclo | La senal circula mas de un semiperiodo y menos de un periodo |
| **C** | Menos de medio ciclo | La senal circula menos de un semiperiodo |
| **D** | Pulsos (onda cuadrada) | El transistor trabaja en corte y saturacion |

## Amplificadores de potencia clase A

Dos configuraciones principales:
- **Acoplo directo** a la carga (sin transformador)
- **Acoplo por transformador**

En ambos casos se identifican:
- **Recta de carga estatica (rcc):** analisis DC
- **Recta de carga dinamica (rca):** analisis AC

El punto Q se oscila a lo largo de la rca cuando hay senal de entrada. $V_{CE}$ oscila entre $V_{CE\,min}$ y $V_{CE\,max}$, e $I_C$ oscila alrededor de $I_{CQ}$.

## Clase A con acoplo directo a la carga

En esta configuracion, la **recta de carga estatica = dinamica** ($R_L$ esta siempre presente). Se situa Q en el centro de la recta para que la excursion de corriente de salida sea **maxima**.

### Punto de operacion optimo

$$V_{CE\,max} = V_{CC}$$

$$V_{CEQ} = \frac{V_{CE\,max}}{2} = \frac{V_{CC}}{2}$$

$$I_{C\,max} = \frac{V_{CC}}{R_L}$$

$$I_{CQ} = \frac{I_{C\,max}}{2} = \frac{V_{CC}}{2R_L}$$

### Potencia en la carga

$$\boxed{P_L = I_{ef}^2 \cdot R_L = \frac{V_{CC}^2 \cdot R_L}{8 \cdot R_L^2} = \frac{V_{CC}^2}{8 R_L}}$$

### Potencia disipada en el transistor (en el punto Q)

$$P_D = V_{CEQ} \cdot I_{CQ} = \frac{V_{CC}}{2} \cdot \frac{V_{CC}}{2R_L} = \frac{V_{CC}^2}{4R_L}$$

> [!warning] Potencia maxima sin senal
> Sin senal de entrada, la disipacion de potencia en el transistor es **maxima**. Toda la potencia de la fuente se disipa en el transistor.

### Potencia de la fuente

$$P_{CC} = V_{CC} \cdot I_{CQ} = \frac{V_{CC}^2}{2R_L}$$

### Eficiencia maxima

$$\boxed{\mu = \frac{P_L}{P_{CC}} = \frac{V_{CC}^2 / 8R_L}{V_{CC}^2 / 2R_L} = 0.25 = 25\%}$$

### Relaciones de potencia

$$\boxed{P_{D\,MAX} = 2 \cdot P_{L\,MAX}}$$

$$\boxed{P_{CC} = 4 \cdot P_{L\,MAX}}$$

> [!example] Regla practica
> Para obtener **4 W** en la carga, se debe disenar una fuente de **16 W** y elegir un transistor capaz de disipar **8 W**.

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
