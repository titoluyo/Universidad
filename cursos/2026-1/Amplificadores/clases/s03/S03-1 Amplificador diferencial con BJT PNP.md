---
title: "Amplificador diferencial con BJT PNP"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 3
orden: 1
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/amplificador-diferencial
  - tema/modo-diferencial
  - tema/modo-comun
  - tema/cmrr
  - tema/parametros-h
date: 2026-04-07
---

## Concepto

El amplificador diferencial es el **bloque fundamental** de los amplificadores operacionales. Usa un **par de transistores identicos** con sus emisores conectados a una fuente de corriente comun.

## Circuito basico con PNP

```
        GND (o -Vcc)
         |       |
        RC1     RC2
         |       |
  Vo1 ---+       +--- Vo2
         |       |
        (C)     (C)
   Q1  PNP     PNP  Q2
        (E)     (E)
         |       |
  V1 ---(B)   (B)--- V2
         |       |
         +---+---+
             |
            REE (o fuente de corriente)
             |
           +Vcc
```

> [!note] PNP vs NPN
> Con PNP la fuente de corriente va a **+Vcc** (al reves que con NPN donde va a $-V_{EE}$). La corriente "baja" desde los emisores hacia los colectores.

## Principio de funcionamiento

La fuente de corriente $I_{EE}$ se **reparte** entre los dos transistores:

$$I_{EE} = I_{E1} + I_{E2}$$

- Si $V_1 = V_2$ → corriente dividida equitativamente: $I_{E1} = I_{E2} = I_{EE}/2$
- Si $V_1 \neq V_2$ → un transistor conduce mas que el otro, desbalanceando las salidas

---

## Tensiones de entrada

Cualquier par de entradas $V_1$, $V_2$ se descompone en dos componentes:

**Tension diferencial** (senal util):

$$\boxed{V_{id} = V_1 - V_2}$$

**Tension en modo comun** (ruido/interferencia):

$$\boxed{V_{ic} = \frac{V_1 + V_2}{2}}$$

### Relacion inversa

A partir de $V_{id}$ y $V_{ic}$ se recuperan las entradas originales:

$$V_1 = V_{ic} + \frac{V_{id}}{2}$$

$$V_2 = V_{ic} - \frac{V_{id}}{2}$$

### Salida total del amplificador

$$\boxed{V_o = A_d \cdot V_{id} + A_{cm} \cdot V_{ic}}$$

Donde:
- $A_d$ = ganancia diferencial → debe ser **alta**
- $A_{cm}$ = ganancia en modo comun → debe ser **~0**

---

## Modelo de parametros h (simplificado)

Para el analisis en pequena senal del amplificador diferencial se usa el **modelo hibrido** del BJT. En la practica se aplican dos simplificaciones:

$$h_{oe} = 0 \qquad h_{re} = 0$$

| Parametro | Nombre | Significado | Simplificacion ($= 0$) |
| --------- | ------ | ----------- | ---------------------- |
| $h_{ie}$ | Resistencia de entrada | Resistencia vista en la base | **Se usa** |
| $h_{re}$ | Realimentacion inversa de voltaje | Efecto de $V_{CE}$ sobre la entrada | No hay realimentacion interna del colector a la base |
| $h_{fe}$ ($\beta$) | Ganancia de corriente | $I_C = h_{fe} \cdot I_B$ | **Se usa** |
| $h_{oe}$ | Conductancia de salida | $1/r_o$ (admitancia colector-emisor) | Impedancia de salida $\to \infty$ (fuente de corriente ideal) |

### Modelo equivalente simplificado

```
    B ----[h_ie]----+---- E
                    |
               h_fe·I_B (↓)
                    |
    C --------------+
```

Con $h_{oe} = h_{re} = 0$, el transistor se reduce a:
- Una **resistencia** $h_{ie}$ entre base y emisor
- Una **fuente de corriente** $h_{fe} \cdot I_B$ entre colector y emisor

### Relaciones utiles

$$h_{ie} = \beta \cdot r_e = \frac{\beta \cdot V_T}{I_C}$$

$$r_e = \frac{V_T}{I_E} \approx \frac{26\,mV}{I_E}$$

$$g_m = \frac{I_C}{V_T} = \frac{\beta}{h_{ie}} = \frac{1}{r_e}$$

> [!tip] ¿Cuando es valida esta simplificacion?
> Cuando la resistencia de carga $R_C \ll \frac{1}{h_{oe}}$ (tipicamente $\frac{1}{h_{oe}} > 40\,k\Omega$). Para la mayoria de circuitos con $R_C < 10\,k\Omega$, la simplificacion introduce un error menor al 5%.

---

## Modos de operacion

### Modo diferencial

Responde a la **diferencia** entre las entradas ($V_{id}$):

$$V_{id} = V_1 - V_2$$

Ganancia diferencial (salida diferencial):

$$\boxed{A_d = \frac{V_{o1} - V_{o2}}{V_1 - V_2} = g_m \cdot R_C}$$

Donde:
- $g_m = \dfrac{I_C}{V_T}$ = transconductancia
- $V_T \approx 26\,mV$ a temperatura ambiente

Para salida single-ended (tomada de un solo colector):

$$A_d = \frac{g_m \cdot R_C}{2}$$

### Modo comun

Responde a la **senal igual** en ambas entradas ($V_{ic}$):

$$V_{ic} = \frac{V_1 + V_2}{2}$$

$$\boxed{A_{cm} = \frac{-R_C}{2R_{EE}}}$$

La ganancia en modo comun es **muy pequena** si $R_{EE}$ es grande. Idealmente, con una fuente de corriente perfecta ($R_{EE} \to \infty$), $A_{cm} \to 0$.

---

## CMRR (Factor de Rechazo en Modo Comun)

Mide que tan bien el amplificador rechaza senales comunes y amplifica solo la diferencia:

$$\boxed{CMRR = \frac{|A_d|}{|A_{cm}|} = g_m \cdot R_{EE}}$$

En decibeles:

$$CMRR_{dB} = 20 \log\left(\frac{|A_d|}{|A_{cm}|}\right)$$

> [!success] CMRR alto = buen amplificador
> Un buen amplificador diferencial tiene $CMRR > 60\,dB$. Esto significa que rechaza eficazmente el ruido (que aparece igual en ambas entradas) y amplifica solo la senal util.

---

## Demostracion: recta de carga DC del par diferencial

Para el circuito con fuente simetrica $\pm V_{CC}$ y resistencia de cola $R_E$:

**Malla KVL** desde $+V_{CC}$, bajando por $R_C$, a traves de Q ($V_{CE}$), por $R_E$ hasta $-V_{CC}$:

$$+V_{CC} - I_C R_C - V_{CE} - (2I_C)R_E - (-V_{CC}) = 0$$

El factor $2I_C$ aparece porque por $R_E$ circula la corriente de **ambos transistores**: $I_{R_E} = I_{E1} + I_{E2} = 2I_E \approx 2I_C$.

$$V_{CC} + V_{CC} = I_C R_C + V_{CE} + 2I_C R_E$$

$$\boxed{2V_{CC} = V_{CE} + I_C(R_C + 2R_E)}$$

> [!tip] Comparacion con emisor comun
> En un emisor comun con un solo transistor: $V_{CC} = V_{CE} + I_C(R_C + R_E)$. El $2V_{CC}$ y el $2R_E$ son consecuencia directa de la **simetria del par diferencial**.

---

## ¿Por que PNP en la entrada?

En circuitos integrados se usan ambos tipos (NPN y PNP) en el mismo op-amp:

- El par PNP permite que el **rango de entrada incluya el voltaje de alimentacion positivo** (o GND en fuente simple)
- Ejemplo: el **LM324** y **LM358** usan par diferencial PNP, permitiendo operar con entradas hasta $V^-$ (GND)
- Con NPN, el rango de entrada llega mas cerca de $V^+$ pero no de $V^-$

## Relacion con el amplificador operacional

El par diferencial es la **primera etapa** de un op-amp. La estructura tipica es:

1. **Etapa diferencial** (par PNP o NPN) → alta impedancia de entrada, ganancia diferencial
2. **Etapa de ganancia** (emisor comun) → ganancia de voltaje alta
3. **Etapa de salida** ([[S02-6 Amplificador Push-Pull Clase B|Push-Pull]] clase AB) → baja impedancia de salida

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
