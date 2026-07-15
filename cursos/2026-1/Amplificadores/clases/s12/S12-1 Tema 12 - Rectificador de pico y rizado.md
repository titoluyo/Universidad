---
title: "Rectificador de pico y voltaje de rizado"
curso: "[[Amplificadores MOC]]"
unidad: 2
semana: 12
orden: 1
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/rectificador-de-pico
  - tema/detector-de-envolvente
  - tema/rizado
  - tema/diodo
date: 2026-06-08
---

## Contexto

El **rectificador de pico** (o *detector de envolvente*) es un diodo seguido de un condensador $C$ en paralelo con la carga $R$. El condensador se carga al valor de pico $V_p$ de la entrada y, mientras el diodo no conduce, se **descarga** lentamente sobre $R$. Esto produce una salida casi continua con una pequeña ondulación: el **voltaje de rizado** $V_r$.

> [!info] Toma de notas en clase
> Desarrollo del análisis del intervalo de descarga y la obtención de $V_r$ bajo la aproximación $CR \gg T$.

---

## 1. Intervalo en que el diodo conduce

El diodo conduce solo durante un breve intervalo cerca del **pico** de la entrada, recargando el condensador hasta $V_p$. Durante el **resto del periodo** el diodo está en corte y el condensador entrega su carga a la resistencia $R$.

## 2. Ecuación de descarga del condensador

Con el diodo en corte, el condensador se descarga sobre $R$ siguiendo una exponencial con constante de tiempo $\tau = CR$:

$$v_O = V_p\, e^{-t/CR}$$

- $v_O$ = tensión de salida durante la descarga
- $V_p$ = tensión de pico (valor al que se cargó $C$)
- $C$ = capacitancia del condensador
- $R$ = resistencia de carga
- $t$ = tiempo medido desde el pico

## 3. Caída al final del intervalo de descarga

Si el intervalo de descarga dura prácticamente todo el periodo $T$ (el de conducción es muy corto), al finalizar la salida ha caído desde $V_p$ hasta $V_p - V_r$:

$$V_p - V_r = V_p\, e^{-T/CR}$$

donde $V_r$ es el **voltaje de rizado** (la amplitud pico-a-pico de la ondulación).

## 4. Aproximación $CR \gg T$

Para que el rizado sea pequeño se diseña con $CR \gg T$, es decir $\dfrac{T}{CR} \ll 1$. Entonces la exponencial se aproxima por los dos primeros términos de su serie de Taylor:

$$e^{-T/CR} \approx 1 - \frac{T}{CR}$$

### Demostración de la aproximación

> [!note] Es una aproximación ($\approx$), no una igualdad
> Se justifica con la **serie de Maclaurin** de la exponencial y la condición de diseño $CR \gg T$.

**1. Serie de Maclaurin de la exponencial.** Para todo número real $x$:

$$e^{x} = \sum_{n=0}^{\infty}\frac{x^{n}}{n!} = 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \cdots$$

**2. Sustituir** $x = -\dfrac{T}{CR}$:

$$e^{-T/CR} = 1 - \frac{T}{CR} + \frac{1}{2!}\left(\frac{T}{CR}\right)^{2} - \frac{1}{3!}\left(\frac{T}{CR}\right)^{3} + \cdots$$

**3. Aplicar la condición** $CR \gg T$, esto es $u \equiv \dfrac{T}{CR} \ll 1$. Elevar al cuadrado un número mucho menor que 1 lo hace aún más pequeño, así que los términos de orden superior son **despreciables**:

$$u \ll 1 \;\Rightarrow\; u^{2} \lll u \;\Rightarrow\; \frac{u^{2}}{2!}, \frac{u^{3}}{3!}, \dots \approx 0$$

**4. Quedándonos con los dos primeros términos** (aproximación lineal):

$$\boxed{\,e^{-T/CR} \approx 1 - \frac{T}{CR}\,}$$

Equivale a confundir la exponencial con su **recta tangente** en el origen: como $\frac{d}{dx}e^{x}\big|_{0} = 1$, se tiene $e^{x}\approx 1 + x$ cerca de $x = 0$.

> [!example] Tamaño del error
> El primer término despreciado es $\tfrac{1}{2}\left(\tfrac{T}{CR}\right)^2$. Con el caso de la gráfica ($CR = 10\,T \Rightarrow u = 0.1$):
> - Aproximación: $1 - 0.1 = 0.9$
> - Valor exacto: $e^{-0.1} = 0.904837\ldots$
> - Error: $\approx 0.0048$ (**0.5 %**), del orden de $\tfrac{1}{2}u^2 = 0.005$. ✓

Sustituyendo en la ecuación anterior:

$$V_p - V_r = V_p\left(1 - \frac{T}{CR}\right) = V_p - V_p\frac{T}{CR}$$

## 5. Voltaje de rizado

Cancelando $V_p$ a ambos lados se obtiene la expresión final:

$$\boxed{\,V_r = V_p\,\dfrac{T}{CR}\,}$$

> [!note] Interpretación
> El rizado crece con $V_p$ y con el periodo $T$ (menor frecuencia → más rizado), y **disminuye** al aumentar $C$ o $R$. Como $T = 1/f$, también se escribe $V_r = \dfrac{V_p}{f\,C\,R}$.

---

## 6. Gráfica

Simulación del detector de envolvente con $V_p = 10\ \text{V}$, $f = 60\ \text{Hz}$ y $CR = 10\,T$ (rizado del 10 %). La salida $v_O$ sigue al pico de la entrada y luego se descarga exponencialmente hasta el siguiente pico.

![[rectificador_pico_rizado.png]]

> [!example] Verificación numérica
> Con $V_p = 10\ \text{V}$, $T = 1/60\ \text{s}$ y $CR = 10\,T$:
> $$V_r = V_p\frac{T}{CR} = 10 \cdot \frac{T}{10\,T} = 1\ \text{V} \quad (10\%\ \text{de } V_p)$$
> que coincide con la amplitud de la ondulación de la salida en la gráfica.

Script: [`plot_rizado.py`](plot_rizado.py) — ejecutar con `uv run --with matplotlib python plot_rizado.py`.
