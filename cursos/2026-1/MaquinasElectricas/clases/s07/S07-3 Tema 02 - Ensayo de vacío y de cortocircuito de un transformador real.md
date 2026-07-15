---
title: Ensayo de vacío y de cortocircuito de un transformador real
curso: "[[Motores MOC]]"
unidad: 2
semana: 7
orden: 3
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/ensayo-vacio
  - tema/ensayo-cortocircuito
  - tema/parametros-transformador
  - tema/perdidas-hierro
  - tema/perdidas-cobre
  - tema/impedancia-cortocircuito
  - tema/tension-cortocircuito-porcentual
date: 2026-05-04
---

![[s07-t02-banner.png]]

## ¿Por qué se hacen ensayos?

Los **ensayos de un transformador** son los diversos procedimientos necesarios para evaluar el rendimiento de la máquina. En la práctica, llevar a cabo pruebas directas reales presenta dificultades por dos razones fundamentales:

1. La **considerable cantidad de energía** que debe ser disipada durante dichas pruebas.
2. La **práctica imposibilidad** de contar con cargas lo bastante elevadas, sobre todo cuando la potencia del transformador es grande, para realizar ensayos en condiciones reales.

La predicción precisa del rendimiento de un transformador en cualquier situación laboral es posible cuando se tienen los **parámetros del circuito equivalente** (ver [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real|circuito equivalente exacto y aproximado]]).

> [!summary] Los dos ensayos esenciales
> 1. **Ensayo de vacío** — entrega $R_{Fe}$ y $X_\mu$ (rama paralela) + las pérdidas en el hierro.
> 2. **Ensayo de cortocircuito** — entrega $R_{cc}$ y $X_{cc}$ (rama serie) + las pérdidas en el cobre.

## Ensayo de vacío

Esta prueba consiste en aplicar al **primario** del transformador la **tensión asignada**, estando el **secundario en circuito abierto**. Al mismo tiempo, deben medirse:

- $P_0$ — potencia absorbida
- $I_0$ — corriente de vacío
- $V_{20}$ — tensión secundaria (en vacío)

![[s07-t02-fig1-ensayo-vacio-esquema.png]]
*Figura 1. Esquema eléctrico del ensayo de vacío con los instrumentos de medida.*

### Interpretación con el circuito equivalente

Dado que las pérdidas $R_1 \cdot I_0^{\,2}$ en vacío son **insignificantes** debido al bajo valor de $I_0$, la **potencia absorbida en vacío prácticamente coincide con las pérdidas en el hierro**:

$$P_0 \approx P_{Fe}$$

Este hecho concuerda con el circuito equivalente aproximado donde $I_2 = 0$:

![[s07-t02-fig2-equivalente-vacio.png]]
*Figura 2. Circuito equivalente en vacío.*

### Factor de potencia en vacío

$$\boxed{\;P_0 = V_{1n} \, I_0 \, \cos\varphi_0 = P_{Fe}\;}$$

![[s07-t02-fig3-fasorial-vacio.png]]
*Figura 3. Diagrama fasorial en vacío.*

Debido a la baja magnitud de la caída de tensión en el lado primario, se puede afirmar que $V_{1n} \approx E_1$. Los componentes de $I_0$ son:

$$I_{Fe} = I_0 \, \cos\varphi_0 \hspace{0.5cm};\hspace{0.5cm} I_\mu = I_0 \, \sin\varphi_0$$

### Cálculo de los parámetros $R_{Fe}$ y $X_\mu$

$$\boxed{\;R_{Fe} = \frac{V_1}{I_{Fe}} \hspace{0.5cm};\hspace{0.5cm} X_\mu = \frac{V_1}{I_\mu}\;}$$

> [!note] Conclusión del ensayo de vacío
> Permite determinar **las pérdidas en el hierro** del transformador y los **parámetros de la rama paralela** del circuito equivalente.

### Relación de transformación a partir del ensayo de vacío

Como $V_{1n} \approx E_1$ y $E_2 = V_{20}$ (no hay caída en el secundario porque está abierto):

$$a = \frac{N_1}{N_2} = \frac{E_1}{E_2} = \frac{V_{1n}}{V_{20}}$$

## Ensayo de cortocircuito

En este ensayo, **se cortocircuita el devanado secundario** y se aplica al primario una tensión que se va elevando gradualmente desde cero hasta que circula la **corriente asignada de plena carga** por los devanados.

![[s07-t02-fig4-ensayo-cc-esquema.png]]
*Figura 4. Circuito eléctrico del ensayo de cortocircuito con los instrumentos de medida.*

![[s07-t02-fig5-equivalente-cc.png]]
*Figura 5. Circuito equivalente de cortocircuito.*

> [!summary] Idea clave del ensayo de cortocircuito
> La **potencia absorbida en cortocircuito coincide con las pérdidas en el cobre**, en concordancia con el circuito equivalente aproximado:
> 
> $$P_{cc} \approx P_{Cu}$$

Del esquema en la figura 6 se **desprecia la rama en paralelo**, como consecuencia del pequeño valor de la corriente $I_0$ frente a $I_{1n}$ al aplicar una tensión $V_1$ reducida:

![[s07-t02-fig6-aproximado-primario.png]]
*Figura 6. Circuito equivalente aproximado del transformador reducido al primario.*

### Factor de potencia en cortocircuito

$$\boxed{\;P_{cc} = V_{1cc} \, I_{1n} \, \cos\varphi_{cc}\;}$$

### Diagrama vectorial y caídas de tensión

Del circuito equivalente en cortocircuito se toma la corriente como referencia:

![[s07-t02-fig7-diagrama-vectorial-cc.png]]
*Figura 7. Diagrama vectorial en cortocircuito.*

$$V_{R_{cc}} = R_{cc} \, I_{1n} = V_{1cc} \, \cos\varphi_{cc}$$

$$V_{X_{cc}} = X_{cc} \, I_{1n} = V_{1cc} \, \sin\varphi_{cc}$$

### Cálculo de los parámetros de cortocircuito

El ensayo determina la **impedancia de cortocircuito total** del transformador. Los valores totales (suma de primario y secundario reducido) son:

$$\boxed{\;R_{cc} = R_1 + R'_2 \hspace{0.5cm};\hspace{0.5cm} X_{cc} = X_1 + X'_2\;}$$

Para separar primario y secundario, se aplica la hipótesis de que **resistencias y reactancias son iguales en ambos lados** (reducidos al mismo nivel):

$$R_1 = R'_2 = \frac{R_{cc}}{2} \hspace{0.5cm};\hspace{0.5cm} X_1 = X'_2 = \frac{X_{cc}}{2}$$

### Aclaración: ensayo con corriente nominal vs. parcial

Cuando el ensayo **se hace con la corriente asignada** $I_{1cc} = I_{1n}$, los datos son:

$$V_{1cc} \hspace{0.4cm};\hspace{0.4cm} I_{1cc} = I_{1n} \hspace{0.4cm};\hspace{0.4cm} P_{cc}$$

Si el ensayo **no está hecho con la corriente nominal**, se usan los subíndices "corto":

$$V_{1corto} \hspace{0.4cm};\hspace{0.4cm} I_{1corto} \hspace{0.4cm};\hspace{0.4cm} P_{corto}$$

Las relaciones entre ambos:

$$Z_{cc} = \frac{V_{1cc}}{I_{1cc}} = \frac{V_{1corto}}{I_{1corto}} \hspace{0.4cm};\hspace{0.4cm} P_{cc} = R_{cc} \, I_{1n}^{\,2} \hspace{0.4cm};\hspace{0.4cm} P_{corto} = R_{cc} \, I_{1corto}^{\,2}$$

Para escalar al valor nominal:

$$V_{1cc} = V_{1corto} \cdot \frac{I_{1n}}{I_{1corto}} \hspace{0.4cm};\hspace{0.4cm} P_{cc} = P_{corto} \cdot \frac{I_{1n}^{\,2}}{I_{1corto}^{\,2}}$$

## Tensión de cortocircuito porcentual ($\varepsilon_{cc}$)

Normalmente la tensión aplicada en el ensayo de cortocircuito y sus dos componentes se expresan en **porcentaje respecto a la tensión asignada**:

$$\boxed{\;\varepsilon_{cc} = \frac{V_{1cc}}{V_{1n}} \cdot 100\;}$$

$$\varepsilon_{R_{cc}} = \frac{V_{R_{cc}}}{V_{1n}} \cdot 100 \hspace{0.5cm};\hspace{0.5cm} \varepsilon_{X_{cc}} = \frac{V_{X_{cc}}}{V_{1n}} \cdot 100$$

### Cortocircuito de ensayo vs. cortocircuito accidental

El ensayo de cortocircuito se diferencia del **cortocircuito accidental** (cuando los terminales del secundario se cortocircuitan mientras el primario está alimentado con $V_{1n}$). En ese caso aparece una **corriente intensa de falta** $I_{1falta}$:

$$I_{1falta} = \frac{V_{1n}}{Z_{cc}}$$

Esta corriente es **altamente peligrosa** para la integridad de la máquina por sus efectos térmicos y electrodinámicos.

Del diagrama vectorial:

$$I_{1n} = \frac{V_{1cc}}{Z_{cc}}$$

De ambas:

$$\boxed{\;I_{1falta} = \frac{100}{\varepsilon_{cc}} \, I_{1n}\;}$$

> [!warning] Valores típicos de $\varepsilon_{cc}$
> - **Transformadores < 1000 kVA** (distribución): $\varepsilon_{cc}$ oscila entre **1 % y 6 %**.
> - **Potencias mayores:** este valor aumenta hasta **6 %–13 %**.
> 
> $\varepsilon_{cc}$ también juega un papel significativo en la **conexión en paralelo** de transformadores.
> 
> Por lo general, $\varepsilon_{X_{cc}} > \varepsilon_{R_{cc}}$ porque $X_{cc} \gg R_{cc}$.

## Resumen — qué entrega cada ensayo

| Ensayo | Condición | Mide | Entrega |
| ------ | --------- | ---- | ------- |
| **Vacío** | Primario a $V_{1n}$, secundario abierto | $P_0$, $I_0$, $V_{20}$ | $R_{Fe}$, $X_\mu$, $P_{Fe}$, $a$ |
| **Cortocircuito** | Secundario cortocircuitado, $V_1$ reducido hasta $I_{1n}$ | $V_{1cc}$, $I_{1cc}$, $P_{cc}$ | $R_{cc}$, $X_{cc}$, $Z_{cc}$, $P_{Cu}$, $\varepsilon_{cc}$ |

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
