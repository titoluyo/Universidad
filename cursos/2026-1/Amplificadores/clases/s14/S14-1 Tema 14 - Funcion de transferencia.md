---
title: "Función de transferencia"
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 14
orden: 1
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/funcion-de-transferencia
  - tema/respuesta-en-frecuencia
  - tema/respuesta-al-impulso
  - tema/convolucion
  - tema/decibelio
  - tema/sistema-lineal
date: 2026-06-22
---

## Contexto

La **función de transferencia** $H(f)$ describe, con un solo objeto matemático, **qué le hace un sistema a una señal**: cuánto amplifica o atenúa cada frecuencia y cuánto la desfasa. Es la relación entre lo que entra y lo que sale, vista en el **dominio de la frecuencia**.

Es el concepto que **abre la Unidad 3** (respuesta y análisis de respuesta en frecuencia de amplificadores y filtros). Todo lo que sigue —filtros pasa bajo / pasa alto / pasa banda, diagramas de Bode, criterios de estabilidad— se construye sobre esta idea: caracterizar un circuito por su $H(f)$. También retoma la "función de transferencia" que ya apareció en realimentación ([[S08-1 Amplificadores realimentados|S08-1]]), ahora generalizada a la frecuencia.

> [!info] Toma de notas en clase
> Semana 14 — Sesión 27. Introducción a la **respuesta en frecuencia**: qué es la función de transferencia, su definición $\text{F.T} = Y/X$, su relación con la respuesta al impulso $h(t)$ (la convolución en el tiempo se vuelve producto en frecuencia) y la lectura de la ganancia y la potencia en **decibelios**. Los tipos de filtro (pasa bajo, pasa alto, pasa banda, supresor de banda, pasa todo) se desarrollan en las notas siguientes.

> [!note] Notación de la pizarra
> El docente etiquetó las cajas como **F.T** (*Función de Transferencia*) y escribió todo "en función de $f$". Con rigor, la **respuesta al impulso vive en el tiempo**, $h(t)$, y su transformada de Fourier es $H(f)$. Por eso aquí se usa $h(t)$ para la respuesta al impulso y $H(f)$ para la función de transferencia; es la misma información vista en dos dominios.

---

## 1. Definición: $\text{F.T} = \dfrac{Y}{X}$

Un sistema (un amplificador, un filtro) recibe una entrada y entrega una salida. La **función de transferencia** es el **cociente** entre la salida y la entrada en el dominio de la frecuencia:

```
        ┌─────────┐
 X(f) ──►│   F.T   │──► Y(f)
        │  H(f)   │
        └─────────┘

        Y(f)
 H(f) = ────
        X(f)
```

$$\boxed{\,H(f) = \dfrac{Y(f)}{X(f)}\,}$$

- $X(f)$ = transformada de Fourier de la **entrada** $x(t)$
- $Y(f)$ = transformada de Fourier de la **salida** $y(t)$
- $H(f)$ = **función de transferencia** del sistema

> [!note] Idea central
> $H(f)$ es una propiedad del **sistema**, no de la señal. Mide *por cuánto* multiplica el circuito a cada frecuencia que le entra. Si conoces $H(f)$, sabes cómo responderá el circuito a **cualquier** entrada.

## 2. Dos dominios, dos descripciones del mismo sistema

El mismo sistema se puede describir de dos maneras equivalentes:

| Dominio | Descripción del sistema | Operación entrada→salida |
|---------|------------------------|--------------------------|
| **Tiempo** | respuesta al impulso $h(t)$ | **convolución** $y(t)=x(t)*h(t)$ |
| **Frecuencia** | función de transferencia $H(f)$ | **producto** $Y(f)=X(f)\,H(f)$ |

```
 x(t) ──►[ h(t) ]──► y(t)        y(t) = x(t) * h(t)   (convolución)
                                        ⇕  (Transformada de Fourier)
 X(f) ──►[ H(f) ]──► Y(f)        Y(f) = X(f) · H(f)   (producto)
```

### 2.1 La respuesta al impulso $h(t)$

$h(t)$ es **lo que sale del sistema cuando le entra un impulso** (un golpe instantáneo, $\delta(t)$). Caracteriza por completo a un sistema lineal e invariante en el tiempo (LTI): conociendo $h(t)$ se obtiene la salida para cualquier entrada mediante la convolución.

### 2.2 La convolución se vuelve producto

Este es el resultado clave que justifica trabajar en frecuencia. En el tiempo, la salida es la **convolución** de la entrada con la respuesta al impulso:

$$y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau$$

La convolución es una operación pesada. Pero al aplicar la **transformada de Fourier**, se convierte en una simple **multiplicación**:

$$\boxed{\,Y(f) = X(f)\cdot H(f)\,}$$

> [!tip] Por qué importa
> La convolución integral del tiempo se reduce a **multiplicar números** en frecuencia. Por eso el análisis de amplificadores y filtros se hace casi siempre en el dominio de la frecuencia: es donde las cuentas son fáciles. Y de ahí sale directo la definición $H(f)=Y(f)/X(f)$ (despejar de $Y=X\,H$).

## 3. $H(f)$ es un número complejo: magnitud y fase

Para cada frecuencia $f$, $H(f)$ es un **número complejo**. Se separa en dos informaciones:

$$H(f) = |H(f)|\;\angle\,\phi(f)$$

- $|H(f)|$ = **magnitud** → cuánto **amplifica o atenúa** esa frecuencia (la *ganancia*).
- $\phi(f) = \angle H(f)$ = **fase** → cuánto **desfasa** (retrasa/adelanta) esa frecuencia.

La gráfica de $|H(f)|$ frente a $f$ es la **respuesta en amplitud**; la de $\phi(f)$ frente a $f$, la **respuesta en fase**. Juntas forman la **respuesta en frecuencia** del sistema.

## 4. La salida en decibelios: ganancia y potencia

En la pizarra, la caja recibe una frecuencia $f$ y entrega su **ganancia** $G$ y su **potencia** $P$ expresadas en **decibelios (dB)**:

```
 f ──►[ F.T ]──► P (dB)   (potencia)
              └─► G (dB)   (ganancia)
```

El decibelio es una escala **logarítmica**. Se usa porque las ganancias de los amplificadores abarcan muchos órdenes de magnitud y porque, en escala log, las **etapas en cascada se suman** en vez de multiplicarse.

**Ganancia en dB** (cociente de amplitudes — tensiones o corrientes):

$$\boxed{\,G_{\text{dB}} = 20\,\log_{10}\!\big|H(f)\big| = 20\,\log_{10}\dfrac{V_o}{V_i}\,}$$

**Potencia en dB** (cociente de potencias):

$$\boxed{\,P_{\text{dB}} = 10\,\log_{10}\dfrac{P_o}{P_i}\,}$$

> [!note] Por qué un factor es 20 y el otro 10
> La potencia va con el **cuadrado** de la amplitud ($P\propto V^2$). Al meter ese cuadrado en el logaritmo aparece un factor 2: $10\log_{10}(V_o/V_i)^2 = 20\log_{10}(V_o/V_i)$. Por eso la **ganancia de tensión** usa **20** y la de **potencia** usa **10**.

> [!example] Valores de referencia útiles
> - $0\ \text{dB}$ → ganancia $=1$ (ni amplifica ni atenúa).
> - $+20\ \text{dB}$ → amplifica $\times 10$ (en tensión).
> - $-3\ \text{dB}$ → la potencia cae a la **mitad** ($|H|\approx 0{,}707$). Es el criterio que define la **frecuencia de corte** de un filtro y el **ancho de banda** de un amplificador.

## 5. Para qué sirve: respuesta en frecuencia y filtros

Como $|H(f)|$ dice cuánto pasa cada frecuencia, **eligiendo la forma de $H(f)$ se diseña un filtro**:

- **Pasa bajo:** $|H(f)|\approx 1$ a bajas frecuencias y cae a alta → deja pasar lo lento, bloquea lo rápido.
- **Pasa alto:** lo contrario.
- **Pasa banda / supresor de banda:** deja pasar (o bloquea) una franja de frecuencias.
- **Pasa todo:** $|H(f)|=1$ en todas las frecuencias, solo cambia la **fase**.

En un amplificador real, $H(f)$ no es plana: cae en bajas y altas frecuencias, y la zona donde la ganancia se mantiene (hasta los puntos de $-3\ \text{dB}$) define su **ancho de banda**. Todo esto se representa con los **diagramas de Bode** (semana 15).

> [!tip] Hilo de la unidad
> Hoy: *qué es* $H(f)$. Sesiones 27–28: darle forma para construir **filtros**. Semana 15: graficar $|H(f)|$ y $\phi(f)$ con **Bode** y analizar **estabilidad**. Todo cuelga de $H(f)=Y/X$.

---

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson — cap. de respuesta en frecuencia y decibelios.
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press — funciones de transferencia y diagramas de Bode.
- Oppenheim, A. & Willsky, S. *Señales y Sistemas*. Prentice Hall — sistemas LTI, respuesta al impulso y convolución.
