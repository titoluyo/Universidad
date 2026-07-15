---
title: Curvas experimentales de los materiales magnéticos
curso: "[[Motores MOC]]"
unidad: 2
semana: 6
orden: 3
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/ferromagnetismo
  - tema/ferritas
  - tema/curva-histeresis
  - tema/saturacion
  - tema/coercitividad
  - tema/magnetizacion-remanente
  - tema/superparamagnetismo
date: 2026-04-27
---

> [!info] Fuente
> Esta nota desarrolla el **Manual "Curvas experimentales de los materiales magnéticos"** entregado por el docente — PDF embebido al final.

## Introducción

A nivel macroscópico, el comportamiento de los **materiales magnéticos** es muy semejante al de los **ferromagnetos**, tanto es así que durante muchos años fueron empleados de manera intercambiable.

Entre los ferromagnetos más comúnmente utilizados se encuentran las **ferritas**, que son materiales cerámicos con diferentes composiciones químicas, tales como el manganeso, níquel, cobalto, zinc, entre otros. Las ferritas poseen un elevado interés tecnológico debido a la combinación de dos características fundamentales:

1. **Facilidad relativa con la que pueden magnetizarse (alta permeabilidad).**
2. **Baja conductividad electrónica** — esto posibilita su aplicación en dispositivos de **alta frecuencia**, entre otras aplicaciones.

> [!note] Conexión con la semana
> Las ferritas ya aparecieron en [[S06-2 Tema 01 - Materiales magnéticos|materiales magnéticos]] como uno de los seis materiales típicos del transformador; aquí estudiamos el origen físico de su curva característica.

## Mecanismo microscópico: alineación de espines

La curva de histéresis de los materiales ferromagnéticos (como hierro y níquel, los más utilizados) se entiende a partir del comportamiento de los espines de los electrones bajo un campo magnético externo $H$:

| Estado | Descripción |
| ------ | ----------- |
| **A** — Material desmagnetizado | Los espines de los electrones están dispuestos de manera aleatoria. |
| **B** — Aplicando campo $H$ | Los espines comienzan a girar en la misma dirección que el campo aplicado. |
| **C** — Saturación $M_s$ | Todos los electrones quedan alineados con el campo. |
| **D** — Magnetización remanente $M_R$ | Al retirar gradualmente el campo, queda una magnetización residual. |
| **E** — Coercitividad $H_c$ | Al aplicar un campo inverso suficiente para desmagnetizar, los electrones quedan desordenados otra vez. |
| **F** — Saturación negativa | Aumentando la intensidad del campo inverso, los electrones se alinean en dirección opuesta al campo inicial. |

Posteriormente se invierte el proceso para completar un ciclo de histéresis.

> [!example] Estados A–F en el cuadro de la figura 1
> A) Antes, B) durante y C) después de aplicar un campo magnético — el bloque resaltado en naranja muestra la zona donde los espines responden al campo $\mathbf{H}$ aplicado.

## Curva de histéresis ferromagnética

La trayectoria $A \to B \to C \to D \to E \to F$ y su retorno cierran el **ciclo de histéresis** característico de los materiales ferromagnéticos.

> [!summary] Parámetros característicos del ciclo
> - **Magnetización de saturación** $M_s$: valor máximo de $M$ con $|H|$ creciente.
> - **Magnetización remanente** $M_R$: valor de $M$ cuando $H = 0$ (después de saturar).
> - **Coercitividad** $H_c$: valor de $|H|$ inverso necesario para llevar $M$ a cero.
> - **Área encerrada** = energía disipada por ciclo → [[S05-1 Tema 01 - Perdidas magneticas en el nucleo#Pérdidas por histéresis|pérdidas por histéresis]].

Inicialmente los electrones se encuentran en estado desordenado y, al aplicar el campo $H$, se alinean en su misma dirección. Cuando se retira el campo, la magnetización disminuye debido a la **orientación estocástica** de los momentos magnéticos en la muestra.

## Diferencia entre paramagnético y superparamagnético

Aunque este comportamiento guarda similitudes con los materiales **paramagnéticos**, es posible distinguir entre un material paramagnético y uno **superparamagnético** mediante la **forma de la curva de magnetización**:

| Tipo | Forma | Saturación |
| ---- | ----- | ---------- |
| **Superparamagnético** | Curva $M$–$H$ con forma de "S" reversible (**sin histéresis**) | Se alcanza a **intensidades de campo moderadas** |
| **Paramagnético**      | Respuesta lineal sin saturación práctica                  | Se alcanza solo a **intensidades muy elevadas** |

La ausencia de ciclo de histéresis distingue al superparamagnetismo del ferromagnetismo clásico, aun cuando ambos pueden saturarse.

## Manual original

![[s06-t01-manual-curvas-experimentales.pdf]]

## Bibliografía

- Martínez, S. (2006). *Materiales magnéticos puros, compuestos e híbridos* [Tesis de doctorado, Centro de Investigación en Química Aplicada]. Repositorio Institucional CIQA. https://ciqa.repositorioinstitucional.mx/jspui/bitstream/1025/93/1/Tesis%20doctorado%20Sagrario%20Montemayor.pdf
