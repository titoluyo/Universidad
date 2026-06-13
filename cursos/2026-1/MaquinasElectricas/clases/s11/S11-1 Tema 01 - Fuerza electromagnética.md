---
title: "Tema 01 - Fuerza electromagnética"
curso: "[[Motores MOC]]"
unidad: 3
semana: 11
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/fuerza-electromagnetica
  - tema/fuerza-de-lorentz
  - tema/maquina-rotativa
date: 2026-06-01
---

> [!info] Material original
> Separata del docente: [s11-separata-fuerza-electromagnetica.pdf](attachments/s11-separata-fuerza-electromagnetica.pdf) (UTP, Semana 11).

## ¿Qué es la fuerza electromagnética?

Cuando una **carga eléctrica está en movimiento**, esta crea a su alrededor un **campo eléctrico** y un **campo magnético**. Este campo magnético ejerce una fuerza sobre cualquier otra carga eléctrica que esté situada dentro de su radio de acción. Esta fuerza que ejerce un campo magnético es la **fuerza electromagnética**.

Una **espira rectangular**, al girar dentro de un campo magnético, experimenta **inducción electromagnética**. Este proceso genera corriente eléctrica en el conductor, fundamental para la operación de **generadores y motores eléctricos** en diversas aplicaciones industriales.

Si en lugar de tener un hilo conductor rectilíneo tenemos una **espira rectangular**, aparecerán un **par de fuerzas de igual valor pero de diferente sentido**, situadas sobre los dos lados perpendiculares al campo magnético. Esto **no provocará un desplazamiento**, sino que la espira **girará sobre sí misma**.

![[Fig 1. Espira rectangular girando en un campo magnetico.png]]
> Espira rectangular girando entre los polos magnéticos: el par de fuerzas $F$ (de igual magnitud y sentido opuesto) sobre los lados perpendiculares al campo hace girar la espira sobre su eje.

## Fuerza electromagnética en una máquina rotativa

La fuerza electromagnética en una máquina rotativa se genera debido a la **interacción entre los campos magnéticos y los conductores eléctricos que transportan corriente**. Este fenómeno se rige por la **ley de Lorentz**, que establece que una carga eléctrica en movimiento dentro de un campo magnético experimentará una fuerza **perpendicular** tanto a la dirección del campo magnético como a la dirección del movimiento de la carga:

$$\vec{F} = q\,\vec{v} \times \vec{B}$$

Donde:
- $q$ = carga eléctrica
- $\vec{v}$ = velocidad de la carga
- $\vec{B}$ = densidad de campo magnético

> [!note] Relación con la fuerza de Lorentz completa
> Esta es la componente magnética de la [[S10-1 Tema 01 - Conversión de energía electromecánica|fuerza de Lorentz]] $\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$. En las máquinas rotativas el término que produce el par es justamente $q\,\vec{v}\times\vec{B}$.

La fuerza de Lorentz generada en una espira rectangular girando en un campo magnético es la **fuerza resultante** experimentada por las cargas eléctricas en movimiento dentro del conductor. En el caso de la espira rectangular, esta fuerza **impulsa el movimiento de las cargas a lo largo del conductor**, lo que resulta en la generación de corriente eléctrica.

![[Fig 2. Fuerza electromagnetica en una maquina rotativa (motor).png]]
> Sección transversal de una máquina rotativa. Leyenda: ▩ Material ferromagnético · ✶ corriente saliente · × corriente entrante · ╲ campo magnético. Las fuerzas $F$ sobre los conductores producen el par motor.

### Funcionamiento como motor

En una máquina rotativa, como un **motor**, se aprovecha esta interacción para **producir movimiento mecánico**. La corriente eléctrica fluye a través de **bobinas de alambre situadas en un campo magnético** generado por imanes permanentes o electroimanes. La interacción entre el campo magnético y la corriente eléctrica genera una fuerza electromagnética que hace que las bobinas experimenten un **par motor**, provocando el **giro del eje** del motor y, por ende, el movimiento mecánico.

### Funcionamiento como generador

En un **generador eléctrico** el proceso es **inverso**: el movimiento mecánico (por ejemplo, proveniente de una turbina en una central eléctrica) induce un **cambio en el flujo magnético** a través de las bobinas del generador, lo que a su vez **genera una corriente eléctrica** en dichas bobinas debido a la **ley de inducción electromagnética de Faraday**.

![[Fig 3. Maquina rotativa funcionando como generador.png]]
> Sección de una máquina rotativa como generador: el **inductor** (polos N–S del rotor) crea el campo y el **inducido** (devanados del estator) recoge la f.e.m. generada por el movimiento.

> [!summary] En resumen
> La fuerza electromagnética en una máquina rotativa se origina a partir de la **interacción entre campos magnéticos y corrientes eléctricas**, lo que permite **convertir energía eléctrica en movimiento mecánico (motor) o viceversa (generador)**.

## Bibliografía

- Universidad de Vigo. (2011). *Dispositivos y máquinas rotatorias*. Universidad de Vigo. Recuperado de https://quintans.webs.uvigo.es/recursos/Web_electromagnetismo/dispositivos_maquinasrotatorias.htm
- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
