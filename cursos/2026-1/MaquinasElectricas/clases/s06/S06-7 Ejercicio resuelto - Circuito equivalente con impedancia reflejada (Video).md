---
title: Ejercicio resuelto - Circuito equivalente con impedancia reflejada
curso: "[[Motores MOC]]"
unidad: 2
semana: 6
orden: 7
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/transformador-ideal
  - tema/impedancia-reflejada
  - tema/circuito-equivalente
  - tema/potencia-aparente
date: 2026-04-27
---

> [!info] Fuente
> Video "Desarrollo de un ejercicio de circuito equivalente" (Semana 06, Tema 02). Transcripción completa en [[#Guion del video|el Guion]] adjunto al final.

## Enunciado

Un transformador ideal de **relación de intensidades** $I_P/I_S = 250$ alimenta a unos aparatos de medida con una intensidad en el secundario $I_S = 5\,\text{A}$ y una **impedancia total** $\mathbf{Z}_L = 0{,}4\,\Omega$. Calcular:

- **a)** Intensidad del primario $I_P$.
- **b)** La potencia aparente en la carga $S$.

## Datos

| Magnitud | Símbolo | Valor |
| -------- | ------- | ----- |
| Relación de corrientes | $I_P/I_S$ | $250$ |
| Corriente en el secundario | $I_S$ | $5\,\text{A}$ |
| Impedancia en la carga | $Z_L$ | $0{,}4\,\Omega$ |

## Desarrollo

### a) Intensidad del primario $I_P$

Recordemos las [[S06-4 Tema 02 - El transformador monofásico ideal#Relación de transformación|relaciones de transformación]]:

$$\frac{V_P}{V_S} = \frac{N_P}{N_S} = a \hspace{0.5cm}\text{y}\hspace{0.5cm} \frac{I_S}{I_P} = \frac{V_P}{V_S} = a$$

La relación entre las corrientes en el primario y el secundario es **inversamente proporcional** a la relación de voltajes:

$$\frac{I_P}{I_S} = \frac{1}{a} = \frac{V_S}{V_P}$$

Como dato, nos dicen que la corriente en el primario sobre la corriente en el secundario es igual a $250$. Despejamos $I_P$:

$$I_P = 250 \cdot I_S = 250 \cdot 5\,\text{A}$$

$$\boxed{I_P = 1\,250\,\text{A}}$$

> [!note] Lectura
> Esta relación tan alta ($I_P/I_S = 250$) corresponde a un transformador **elevador de tensión** muy fuerte: el secundario tendría $V_S/V_P = 250$. La alta corriente del primario lo confirma — toda la potencia entra por el lado de baja tensión.

### b) Potencia aparente en la carga $S$

La potencia aparente es:

$$S = V_S \cdot I_S$$

Como $V_S = I_S \cdot Z_L$ (la carga es la impedancia $Z_L$):

$$S = (I_S \cdot Z_L) \cdot I_S = I_S^{\,2} \cdot Z_L$$

Reemplazando:

$$S = (5\,\text{A})^2 \cdot 0{,}4\,\Omega = 25 \cdot 0{,}4$$

$$\boxed{S = 10\,\text{VA}}$$

## Resumen de resultados

| Magnitud | Valor |
| -------- | ----- |
| Corriente en el primario $I_P$ | $1\,250\,\text{A}$ |
| Potencia aparente en la carga $S$ | $10\,\text{VA}$ |

> [!tip] Por qué este ejercicio se llama "de circuito equivalente"
> Aunque el desarrollo numérico es directo, el ejercicio ilustra el concepto detrás del **circuito equivalente**: el secundario, con su carga $Z_L = 0{,}4\,\Omega$, se puede ver "reflejado" al primario como una impedancia equivalente $\mathbf{Z}_L^{\prime} = a^2 \cdot \mathbf{Z}_L$ (ver [[S06-6 Tema 02 - Polaridad y conversión de impedancias#Impedancia reflejada al primario|conversión de impedancias]]). Esto evita tener que trabajar con dos circuitos separados.

## Guion del video

![[s06-t02-ej2-guion-circuito-equivalente.pdf]]

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
