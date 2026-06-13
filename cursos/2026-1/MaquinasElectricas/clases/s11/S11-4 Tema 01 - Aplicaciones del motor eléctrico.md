---
title: "Tema 01 - Aplicaciones del motor eléctrico"
curso: "[[Motores MOC]]"
unidad: 3
semana: 11
orden: 4
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/clasificacion-motores
  - tema/motor-dc
  - tema/motor-asincrono
  - tema/motor-sincrono
  - tema/velocidad-de-sincronismo
date: 2026-06-01
---

> [!info] Material original
> Manual del docente: [s11-manual-aplicaciones-motor.pdf](attachments/s11-manual-aplicaciones-motor.pdf) (UTP, Semana 11).

## El motor eléctrico

Los **motores eléctricos** son máquinas eléctricas que **transforman en energía mecánica** la energía eléctrica que absorben por sus bornes. Según el **tipo de corriente** con que se alimentan, se clasifican en:

| Motores de corriente continua (DC) | Motores de corriente alterna (AC) |
| --- | --- |
| De excitación independiente | **Síncronos** |
| De excitación serie | **Asíncronos:** |
| De excitación shunt (derivación) | • Monofásicos: de bobinado auxiliar, de espira en cortocircuito, universal |
| De excitación compuesta (compound) | • Trifásicos: de rotor bobinado, de rotor en cortocircuito (jaula de ardilla) |

Los **motores de corriente alterna asíncronos** (tanto monofásicos como trifásicos) son los que tienen una **aplicación más generalizada**, gracias a su facilidad de utilización, poco mantenimiento y bajo coste de fabricación.

### Velocidad de sincronismo

La **velocidad de sincronismo** de los motores de corriente alterna viene definida por la expresión:

$$n = \frac{60 \cdot f}{P}$$

Donde:
- $n$ = velocidad en **revoluciones por minuto** [rpm]
- $f$ = **frecuencia** de la red [Hz]
- $P$ = número de **pares de polos** de la máquina

> [!note] Motor asíncrono
> Se da el nombre de **motor asíncrono** al motor de corriente alterna cuya parte móvil **gira a una velocidad distinta a la de sincronismo**. Aunque a frecuencia industrial la velocidad es fija para un determinado motor, hoy en día se recurre a **variadores de frecuencia** para regular la velocidad de estos motores.

## Aplicación de motores en DC

Debido a sus diversas opciones de configuración técnica, los **motores de corriente continua (DC)** son fundamentales en una variedad de aplicaciones. Su capacidad para **controlar fácilmente las revoluciones y el par motor**, así como su precisión de regulación y gran dinamismo, permiten una amplia gama de usos.

### Motores DC con escobillas

Siendo una forma convencional y probada de motor, **necesitan pocos o ningún componente externo**, lo que los hace especialmente adecuados para entornos adversos. Se utilizan en:

- Maquinaria rotativa, herramientas de rectificado, sistemas de transporte y aspiradoras.
- Impulso de compresores, maquinaria rotativa y sistemas de elevación como ascensores.
- Robótica (con imán permanente integrado): donde se requiere control preciso y par motor reducido.

### Motores DC sin escobillas (BLDC / Brushless)

Los **motores DC sin escobillas** (BLDC, *Brushless DC Motors*) emplean un **sistema de control electrónico** para sincronizar la conmutación de la corriente en sus bobinas, en lugar de las escobillas mecánicas. La ausencia de escobillas proporciona:

- **Mayor eficiencia energética.**
- **Vida útil más larga.**
- **Menor mantenimiento.**

Aplicaciones: drones, vehículos eléctricos, herramientas eléctricas, electrodomésticos, y en la industria la **tecnología de fabricación y automatización industrial** (sistemas de control de movimiento, accionamiento y posicionamiento).

> [!example] Motores paso a paso
> Un ejemplo prominente de los BLDC son los **motores paso a paso**, ampliamente utilizados en el **control de posicionamiento** en circuitos de regulación abierta. En entornos industriales respaldan procesos automatizados, por ejemplo en máquinas *pick and place*.

## Aplicación de motores en AC

### Motores asíncronos (de inducción)

Sus aplicaciones son muy amplias y abarcan diversos sectores industriales y comerciales:

- **Maquinaria pesada:** grúas, excavadoras, trituradoras.
- **Equipos de fabricación:** máquinas herramientas, prensas, laminadoras.
- **Sistemas de bombeo:** bombas de agua, bombas industriales.
- **Ventilación y HVAC:** ventiladores, sistemas de aire acondicionado.
- **Compresores:** para aire comprimido industrial.
- **Electrodomésticos:** lavadoras, secadoras, ventiladores de techo.
- **Equipos de cocina:** licuadoras, batidoras, hornos eléctricos.
- **Bombas de piscina y spa.**
- **Ascensores y sistemas de elevación** en edificios.
- **Transporte público:** metros, trenes, tranvías.
- **Automoción:** tracción en vehículos eléctricos, dirección asistida.
- **Generadores eléctricos** y **energía eólica** (máquina asíncrona como generador en turbinas).
- **Equipos agrícolas:** tractores, cosechadoras, sistemas de riego.

### Motores síncronos

Tienen aplicaciones específicas donde su capacidad para **mantener una velocidad constante** y su **alto factor de potencia** son beneficiosos:

- **Turbinas de vapor** y **generadores hidroeléctricos:** acoplados a generadores en plantas de energía.
- **Compresores de aire** de gran tamaño (velocidad constante y alta eficiencia).
- **Bombas de agua de gran capacidad:** flujo constante y control preciso del caudal.
- **Propulsión marina:** barcos y embarcaciones de alto rendimiento.
- **Ferrocarriles:** trenes de alta velocidad.
- **Sistemas de refrigeración:** compresores con control preciso y operación continua.
- **Sistemas de accionamiento de alta precisión:** equipos de prueba y medición.

> [!summary] Asíncrono vs síncrono
> El **motor asíncrono** domina por su robustez, bajo costo y poco mantenimiento → la mayoría de las aplicaciones industriales y domésticas. El **motor síncrono** se reserva para donde se exige **velocidad constante exacta**, **alta potencia** o **alto factor de potencia** — pero es más costoso e instala/controla con mayor complejidad. Esta comparación se retoma en las [[S11-8 Conclusiones semana 11|conclusiones]].

## Bibliografía

- Cembranos, F. (2014). *Motores síncronos*. *Revista Digital de ACTA*. Recuperado de https://www.acta.es/medios/articulos/ciencias_y_tecnologia/029001.pdf
- Rodríguez, M. (2018). *Máquinas asíncronas o de inducción*. En *Máquinas Eléctricas II*. Universidad de Cantabria.
