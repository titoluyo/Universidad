---
title: "Tema 01 - Conversión de energía electromecánica: principio de funcionamiento del motor eléctrico"
curso: "[[Motores MOC]]"
unidad: 3
semana: 10
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/conversion-electromecanica
  - tema/motor-electrico
  - tema/fuerza-de-lorentz
  - tema/clasificacion-motores
date: 2026-05-25
---

> [!info] Material original
> Manual del docente: [s10-manual-tema01-conversion-electromecanica.pdf](attachments/s10-manual-tema01-conversion-electromecanica.pdf) (UTP, Semana 10).

## El motor eléctrico

Los **motores eléctricos** son dispositivos que **transforman energía eléctrica en energía mecánica rotativa** mediante la interacción de campos magnéticos generados en sus bobinas. Constan de un **estator** y un **rotor** y se utilizan en una amplia gama de aplicaciones industriales, comerciales y residenciales.

Algunos motores eléctricos son **reversibles**: pueden convertir la energía mecánica en eléctrica y operar como **generadores** o **dinamos**. Los motores de tracción usados en locomotoras o automóviles híbridos son ejemplos de motores que desempeñan ambas funciones.

> [!example] Aplicaciones cotidianas
> Ventiladores, vibradores de teléfonos móviles, bombas de agua, medios de transporte eléctricos, electrodomésticos, herramientas eléctricas (esmeriles angulares), unidades de disco, entre otros.

Los motores pueden ser alimentados por **corriente continua (CC)** o **corriente alterna (CA)**:

- **CC:** baterías, paneles solares, dínamos, fuentes de alimentación integradas y rectificadores.
- **CA:** red eléctrica, alternadores de plantas eléctricas de emergencia, e inversores de potencia (bifásicos o trifásicos).

Los motores más pequeños se encuentran en relojes eléctricos. Los motores de uso general (con dimensiones estandarizadas) abastecen a la industria. Los motores de mayor tamaño se usan en propulsión de trenes, compresores y bombeo, con potencias que alcanzan **hasta 100 MW**.

## Principio de funcionamiento del motor eléctrico

Los motores eléctricos son aparatos que convierten **energía eléctrica en energía mecánica mediante el uso de un campo magnético**. Cada tipo de motor tiene componentes específicos cuya disposición determina la interacción entre los flujos eléctricos y magnéticos que generan la **fuerza** o el **par de torsión** del motor.

El principio básico que explica cómo se genera una fuerza debido a la interacción entre una carga eléctrica puntual $q$ en presencia de campos eléctricos y magnéticos es la **fuerza de Lorentz**:

$$\mathbf{F} = q\,(\mathbf{E} + \mathbf{v} \times \mathbf{B})$$

Donde:
- $q$ = carga eléctrica puntual
- $\mathbf{E}$ = campo eléctrico
- $\mathbf{v}$ = velocidad de la partícula
- $\mathbf{B}$ = densidad de campo magnético

> [!note] Lectura física del término $\mathbf{v} \times \mathbf{B}$
> Es el producto vectorial entre la velocidad de la carga y el campo magnético. Su módulo es máximo cuando $\mathbf{v} \perp \mathbf{B}$ y su dirección sigue la **regla de la mano derecha**. Esta componente es la responsable directa del **par electromagnético** en motores: al circular corriente por un conductor inmerso en un campo magnético, cada portador de carga siente esta fuerza, y la suma sobre todos los portadores se traduce en una fuerza neta sobre el conductor.

### Campo magnético rotativo

El estator de un motor de CA produce un **campo magnético rotativo** mediante tres bobinados desfasados 120° (configuración trifásica `U–V–W`). El campo girante "arrastra" magnéticamente al rotor, induciendo en él corrientes (motor asíncrono) o interactuando con sus polos (motor síncrono) para producir el par. Este es el principio que conecta el bloque teórico de la semana con el comportamiento físico real de un motor industrial.

## Características generales de los motores eléctricos

- Se pueden construir de **cualquier tamaño y forma**, siempre que el voltaje lo permita.
- Tienen un **par de giro elevado** y, según el tipo, **prácticamente constante**.
- Su rendimiento es **muy elevado** (típicamente ≈ **75 %**), aumentando con la potencia de la máquina.
- **No emiten contaminantes** directamente, aunque la generación de la energía eléctrica que los alimenta puede sí emitirlos.
- En general son **autoventilados**: no requieren refrigeración ni ventilación externa.

## Clasificación de motores eléctricos

### Motores de corriente continua

Según la forma como están conectados los devanados de campo y armadura:

| Tipo | Característica principal |
| --- | --- |
| **Motor serie** | Devanado de campo en serie con la armadura. Par de arranque muy alto. |
| **Motor compound** | Combina conexiones serie y shunt. Compromiso entre par alto y velocidad estable. |
| **Motor shunt (paralelo)** | Devanado de campo en paralelo con la armadura. Velocidad casi constante. |
| **Motor eléctrico sin escobillas** (BLDC) | Conmutación electrónica; mayor eficiencia y vida útil. |

Otros tipos usados en electrónica:

- **Motor paso a paso** — posicionamiento angular discreto.
- **Servomotor** — control preciso de posición/velocidad con realimentación.
- **Motor sin núcleo** (coreless) — baja inercia, respuesta dinámica rápida.

### Motores de corriente alterna

Existen tres familias principales; el **motor asíncrono** es el más usado en la industria y el que menos mantenimiento requiere:

| Tipo | Característica principal |
| --- | --- |
| **Motor universal** | Puede operar en CA o CC. Común en herramientas portátiles. |
| **Motor asíncrono (de inducción)** | Rotor gira a velocidad menor que la del campo girante (deslizamiento). Robusto y económico. |
| **Motor síncrono** | Rotor gira sincronizado con la frecuencia de red. Usado en aplicaciones de velocidad constante y alta potencia. |

> [!summary] Idea central de la semana
> La **fuerza de Lorentz** es el ladrillo físico que sostiene todo el funcionamiento de un motor eléctrico. Los conceptos de **energía** y **coenergía magnética** que veremos en el [[S10-2 Tema 02 - Función de energía y coenergía|Tema 02]] son el **aparato matemático** que permite calcular, a partir del campo magnético almacenado, la fuerza/par electromagnético resultante — diferenciando además el caso lineal del no lineal (saturación).

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Conversión de energía electromecánica: principio de funcionamiento del motor eléctrico* [Material de estudio – Manual]. UTP+class.
