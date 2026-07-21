---
title: "Avance de Proyecto Final — Análisis de una señal senoidal rectificada de media onda mediante Series de Fourier"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
  - tema/series-de-fourier
  - tema/octave
date: 2026-07-13
---

<!--
====================================================================
CONTENIDO del Avance de Proyecto Final (APF) - Proyecto 1 (Fourier).
Este .md contiene SOLO el CONTENIDO exigido por la consigna
(Introduccion, Marco teorico, Dominio de simulacion, Dominio teorico,
Referencias). NO incluye el formato de Word (Arial 12, interlineado,
paginado, indice con paginas): eso se aplica con el prompt
"APF - Prompt para Word (formato).md".
Alcance APF = SOLO Series de Fourier (Proyecto 1). El PROY desarrolla el
Proyecto 2 (Laplace) en documento aparte, por indicacion del docente
(cruce intencional APF/PROY): ver TrabajoFinal/Proyecto2-v2/.
====================================================================
-->

# Análisis de una señal senoidal rectificada de media onda mediante Series de Fourier y su aproximación en GNU Octave

**Avance de Proyecto Final (APF) — Series y Transformadas**
UTP · Ciclo 2026-1 · Docente: J. F. Torres
Modalidad: _(individual / grupal — completar)_
Integrante(s): _(nombres y códigos)_
Julio de 2026

---

## Contenido

1. Introducción
2. Marco teórico
   - 2.1. Serie de Fourier: definición y conceptos
   - 2.2. Propiedades utilizadas
   - 2.3. El simulador: GNU Octave
   - 2.4. Ecuaciones aplicadas
3. Dominio de simulación de la Serie de Fourier
   - 3.1. Desarrollo del programa
   - 3.2. Resultados de la simulación
   - 3.3. Análisis de los resultados del simulador
4. Dominio teórico de la Serie de Fourier
   - 4.1. Solución teórica
   - 4.2. Resultados teóricos
   - 4.3. Análisis de los resultados teóricos
5. Referencias bibliográficas

> **Lista de figuras.** Figura 1: señal senoidal rectificada de media onda. Figura 2: aproximación de Fourier $S_N(t)$ para $N=1,2,4,10$. Figura 3: error cuadrático medio $E_k$ frente al número de armónicos.
>
> **Lista de tablas.** Tabla 1: error cuadrático medio simulado. Tabla 2: coeficientes de Fourier no nulos. Tabla 3: error cuadrático medio teórico. Tabla 4: comparación teórico vs. simulado.

---

## 1. Introducción

La conversión de corriente alterna en corriente continua es una de las operaciones más frecuentes de la electrónica: prácticamente todo equipo alimentado desde la red eléctrica requiere una etapa de **rectificación** que transforme la señal senoidal de entrada en una señal de un solo signo. El **rectificador de media onda**, el más simple de estos circuitos —construido con un único diodo—, deja pasar solamente el semiciclo positivo de la senoide y bloquea el negativo (Boylestad & Nashelsky, 2009). El resultado es una señal periódica pero **fuertemente no senoidal**, con un valor promedio (componente continua) aprovechable y un **rizado** que debe caracterizarse para diseñar el filtrado posterior.

Como antecedente general, cualquier señal periódica —por muy alejada que esté de una senoide pura— puede representarse como una suma de senoides armónicamente relacionadas mediante la **Serie de Fourier** (Hsu, 1973). Esta herramienta, nacida del estudio de la conducción del calor en el siglo XIX, es hoy la base del análisis de señales y sistemas en ingeniería eléctrica y electrónica (Oppenheim & Willsky, 1998). Como antecedente específico, la empresa *Electronics S.A.* necesita generar una señal senoidal rectificada de media onda para una aplicación concreta y requiere conocer su descomposición en frecuencia para dimensionar el sistema; además, dispone de **GNU Octave** como entorno de cálculo numérico para aproximar y validar la señal.

La pregunta de ingeniería que articula este avance es, por tanto, **cómo se descompone en frecuencia una señal senoidal rectificada de media onda y cuántos armónicos son necesarios para reproducirla con fidelidad suficiente**. El **objetivo principal** del proyecto es *obtener, por vía analítica y por simulación en GNU Octave, la Serie de Fourier de una señal senoidal rectificada de media onda, presentando y analizando los resultados por ambos métodos.* Como objetivos específicos se plantean: (i) definir la señal con parámetros de ingeniería realistas; (ii) calcular sus coeficientes de Fourier resolviendo las integrales paso a paso; y (iii) reconstruir la señal en Octave con un número creciente de términos y evaluar la calidad de la aproximación.

## 2. Marco teórico

### 2.1. Serie de Fourier: definición y conceptos

Una función $f(t)$ **periódica** de periodo $T$ puede desarrollarse como una suma infinita de senos y cosenos, denominada **Serie de Fourier** (Hsu, 1973):

$$f(t) = \frac{1}{2}a_0 + \sum_{n=1}^{\infty}\bigl(a_n\cos n\omega_0 t + b_n\sin n\omega_0 t\bigr)$$

donde $\omega_0 = 2\pi/T$ es la **frecuencia angular fundamental**, $n$ el número de armónico, y $a_0$, $a_n$, $b_n$ los **coeficientes de Fourier**. El término $\tfrac{1}{2}a_0$ es el **valor promedio** o componente continua (DC) de la señal sobre un periodo. Cada par $(a_n, b_n)$ describe la contribución del armónico de frecuencia $n\omega_0$.

### 2.2. Propiedades utilizadas

**Ortogonalidad.** Las funciones $\{\cos n\omega_0 t,\ \sin n\omega_0 t\}$ forman un conjunto **ortogonal** en un periodo: la integral del producto de dos de ellas se anula salvo que sean idénticas. Gracias a esta propiedad, al multiplicar la serie por una función base e integrar, sobrevive un único término, lo que permite **despejar** cada coeficiente (Hsu, 1973).

**Simetría (paridad).** Si $f$ es **par** ($f(-t)=f(t)$), todos los $b_n=0$ y la serie es de cosenos; si es **impar**, $a_0=a_n=0$ y la serie es de senos. La señal de este proyecto **no posee simetría** —al anularse durante medio periodo no es ni par ni impar—, por lo que deben calcularse los tres coeficientes.

**Identidades producto→suma.** Para resolver las integrales de los coeficientes se emplean:
$$\sin\alpha\cos\beta = \tfrac{1}{2}[\sin(\alpha+\beta)+\sin(\alpha-\beta)], \qquad \sin\alpha\sin\beta = \tfrac{1}{2}[\cos(\alpha-\beta)-\cos(\alpha+\beta)]$$

### 2.3. El simulador: GNU Octave

**GNU Octave** es un lenguaje interpretado de alto nivel para cálculo numérico, de código abierto y ampliamente compatible con MATLAB (Eaton et al., 2024). Permite definir vectores de tiempo, evaluar funciones elementales (`sin`, `cos`, `abs`), programar sumatorias mediante bucles `for`, integrar numéricamente (`trapz`) y **graficar** señales (`plot`, `semilogy`, con `title`, `xlabel`, `grid on`). Estas capacidades bastan para reconstruir una Serie de Fourier término a término y cuantificar el error de la aproximación, razón por la cual se adopta como simulador en este proyecto.

### 2.4. Ecuaciones aplicadas

Los coeficientes se obtienen por las fórmulas de proyección (Hsu, 1973):

$$a_0 = \frac{2}{T}\int_{T} f(t)\,dt, \qquad a_n = \frac{2}{T}\int_{T} f(t)\cos n\omega_0 t\,dt, \qquad b_n = \frac{2}{T}\int_{T} f(t)\sin n\omega_0 t\,dt$$

La calidad de la aproximación truncada a $k$ armónicos, $S_k(t)$, se mide con el **error cuadrático medio**, que mediante la ortogonalidad se reduce a la forma de **Parseval truncada**:

$$E_k = \frac{1}{T}\int_{T}\bigl[f(t)-S_k(t)\bigr]^2 dt = \frac{1}{T}\int_{T}[f(t)]^2 dt - \frac{a_0^2}{4} - \frac{1}{2}\sum_{n=1}^{k}\bigl(a_n^2+b_n^2\bigr)$$

$E_k$ representa la **potencia residual** no capturada por los primeros $k$ términos. Aplicando estas ecuaciones a la señal senoidal rectificada de media onda —definida en la sección 4— se obtiene su Serie de Fourier, que resulta ser:

$$f(t) = \frac{A}{\pi} + \frac{A}{2}\sin(\omega_0 t) - \frac{2A}{\pi}\sum_{k=1}^{\infty}\frac{\cos(2k\,\omega_0 t)}{4k^2-1}$$

Esta expresión es la que se implementa en el simulador (sección 3) y se deduce paso a paso de forma teórica (sección 4).

## 3. Dominio de simulación de la Serie de Fourier

### 3.1. Desarrollo del programa

Se implementó el script `proyecto1_fourier.m` en GNU Octave. El programa: (1) define los parámetros de la señal ($A=12\sqrt2\ \text{V}$, $T=1/60\ \text{s}$, $\omega_0=2\pi/T$); (2) genera la señal original de media onda con una máscara lógica; (3) reconstruye la suma parcial $S_N(t)$ en un bucle `for` con los coeficientes de la Serie de Fourier; y (4) calcula el error cuadrático medio integrando numéricamente con `trapz`. El núcleo del código es:

```octave
% Parametros de la senal
A  = 12*sqrt(2);   T = 1/60;   w0 = 2*pi/T;     % A = 16.97 V, 60 Hz

% Coeficientes de Fourier (media onda)
a_coef = @(n) (n==0).*(2*A/pi) + (n>=2 & mod(n,2)==0).*(-2*A./(pi*(n.^2-1)));
b_coef = @(n) (n==1).*(A/2);

% Senal original de media onda (deja pasar solo el semiciclo positivo)
f_orig = @(t) A*sin(w0*t) .* (sin(w0*t) >= 0);

% Reconstruccion con N armonicos
function y = S_N(t, N, A, w0, a_coef, b_coef)
  y = (a_coef(0)/2) * ones(size(t));            % componente DC = A/pi
  for n = 1:N
    y = y + a_coef(n)*cos(n*w0*t) + b_coef(n)*sin(n*w0*t);
  end
end

% Error cuadratico medio simulado (integracion numerica)
Ek_sim = trapz(tp, (fp - S_N(tp, k, A, w0, a_coef, b_coef)).^2) / T;
```

Se emplea un vector de tiempo de dos periodos con paso $\approx T/4000$, suficientemente fino para que la integración numérica sea precisa. El código completo se acompaña como archivo `proyecto1_fourier.m`.

### 3.2. Resultados de la simulación

La Figura 1 muestra la señal original generada por el programa: el rectificador de media onda conserva el semiciclo positivo de la senoide de 60 Hz y anula el negativo.

![**Figura 1.** Señal senoidal rectificada de media onda ($A=12\sqrt2$ V, $f=60$ Hz), generada en GNU Octave. Elaboración propia.](attachments/fig1_senal.png)

La Figura 2 superpone la señal original y su reconstrucción de Fourier para $N=1,2,4$ y $10$ armónicos.

![**Figura 2.** Aproximación de Fourier $S_N(t)$ frente a la señal original para $N=1,2,4,10$ armónicos. Elaboración propia en GNU Octave.](attachments/fig2_superposicion.png)

La Figura 3 presenta el error cuadrático medio simulado frente al número de armónicos, en escala semilogarítmica.

![**Figura 3.** Error cuadrático medio $E_k$ frente al número de armónicos $k$, calculado en la simulación. Elaboración propia en GNU Octave.](attachments/fig3_error.png)

Los valores numéricos del error obtenido por el simulador se resumen en la Tabla 1.

**Tabla 1.** Error cuadrático medio simulado (integración numérica con `trapz`).

| $k$ (armónicos) | $E_k$ simulado [V²] | Potencia residual $E_k/P$ |
| --------------- | ------------------- | ------------------------- |
| 1 | $6{,}8195$ | $9{,}47\%$ |
| 2 | $0{,}33494$ | $0{,}465\%$ |
| 4 | $0{,}075562$ | $0{,}105\%$ |
| 6 | $0{,}027920$ | $0{,}0388\%$ |
| 10 | $0{,}0072610$ | $0{,}0101\%$ |

### 3.3. Análisis de los resultados del simulador

La simulación evidencia una **convergencia rápida**. Con un solo armónico ($N=1$: componente continua más fundamental) la aproximación es pobre —la senoide ni siquiera se anula durante el semiciclo bloqueado— y queda sin representar el 9,5 % de la potencia. Al incorporar el **segundo armónico** ($N=2$) la curva ya aplana el tramo cero y sigue la joroba positiva, reduciendo el error residual por debajo del 0,5 %. Para $N=4$ y $N=10$ la reconstrucción es visualmente indistinguible de la señal original.

En la Figura 3 el error decae describiendo una **escalera**: cada peldaño descendente corresponde a la incorporación de un armónico **par**, mientras que los armónicos **impares** (de coeficiente nulo, según se confirma teóricamente en la sección 4) producen las mesetas horizontales. Además, al tratarse de una señal **continua**, no se observa el sobreimpulso característico del fenómeno de Gibbs. Con solo diez armónicos el simulador reproduce la señal con una potencia residual del orden del 0,01 %, lo que confirma que la Serie de Fourier es una representación eficiente de esta señal.

## 4. Dominio teórico de la Serie de Fourier

### 4.1. Solución teórica

**Definición de la señal.** Se modela el secundario de un transformador que reduce la red peruana (220 V RMS, 60 Hz) a 12 V RMS, rectificado en media onda. La amplitud pico es $A=12\sqrt2\approx16{,}97$ V y el periodo $T=1/60$ s, de donde $\omega_0=2\pi/T=120\pi\approx376{,}99$ rad/s. En un periodo:

$$f(t) = \begin{cases} A\sin(\omega_0 t), & 0 \le t < T/2 \\ 0, & T/2 \le t < T \end{cases}$$

Como $f(t)=0$ en la segunda mitad del periodo, todas las integrales se reducen al intervalo $[0,\,T/2]$.

**Término constante.**
$$a_0 = \frac{2}{T}\int_0^{T/2} A\sin(\omega_0 t)\,dt = \frac{2A}{T\omega_0}\bigl[-\cos\omega_0 t\bigr]_0^{T/2} = \frac{4A}{T\omega_0} = \frac{2A}{\pi}$$
de modo que el valor promedio es $\tfrac{1}{2}a_0 = A/\pi \approx 5{,}40$ V.

**Coeficientes de cosenos.** Con la identidad $\sin\alpha\cos\beta$ y el resultado auxiliar $\int_0^{T/2}\sin(m\omega_0 t)\,dt = \frac{1-(-1)^m}{m\omega_0}$ (nulo si $m$ es par), y tratando **aparte** el caso $n=1$:

$$a_1 = 0; \qquad a_n = -\frac{2A}{\pi(n^2-1)}\ (n\ \text{par}); \qquad a_n = 0\ (n\ \text{impar}\ge 3)$$

**Coeficientes de senos.** Con la identidad $\sin\alpha\sin\beta$, el caso $n=1$ da $\int_0^{T/2}[1-\cos 2\omega_0 t]\,dt = T/2$, y para $n\ge2$ las integrales de cosenos enteros se anulan:

$$b_1 = \frac{A}{2}\approx 8{,}49\ \text{V}; \qquad b_n = 0\ (n\ge 2)$$

**Serie de Fourier resultante.** Reuniendo los términos no nulos y reindexando los pares como $n=2k$:

$$\boxed{\;f(t) = \frac{A}{\pi} + \frac{A}{2}\sin(\omega_0 t) - \frac{2A}{\pi}\sum_{k=1}^{\infty}\frac{\cos(2k\,\omega_0 t)}{4k^2-1}\;}$$

### 4.2. Resultados teóricos

Los coeficientes no nulos se resumen en la Tabla 2.

**Tabla 2.** Coeficientes de Fourier no nulos de la señal ($A=16{,}97$ V).

| Componente | Símbolo | Expresión | Valor [V] |
| ---------- | ------- | --------- | --------- |
| Continua (DC) | $a_0/2$ | $A/\pi$ | $5{,}402$ |
| Fundamental (seno) | $b_1$ | $A/2$ | $8{,}485$ |
| Armónico 2 (coseno) | $a_2$ | $-2A/3\pi$ | $-3{,}601$ |
| Armónico 4 | $a_4$ | $-2A/15\pi$ | $-0{,}720$ |
| Armónico 6 | $a_6$ | $-2A/35\pi$ | $-0{,}309$ |
| Armónico 8 | $a_8$ | $-2A/63\pi$ | $-0{,}171$ |
| Armónico 10 | $a_{10}$ | $-2A/99\pi$ | $-0{,}109$ |

La potencia media teórica de la señal es $\tfrac{1}{T}\int_0^{T}f^2\,dt = A^2/4 = 72{,}0$ V². Sustituyendo los coeficientes en la fórmula de Parseval truncada se obtiene el error cuadrático medio teórico (Tabla 3).

**Tabla 3.** Error cuadrático medio teórico $E_k$ (relación de Parseval).

| $k$ (armónicos) | $E_k$ teórico [V²] | Potencia residual $E_k/P$ |
| --------------- | ------------------ | ------------------------- |
| 1 | $6{,}8195$ | $9{,}47\%$ |
| 2 | $0{,}33494$ | $0{,}465\%$ |
| 4 | $0{,}075561$ | $0{,}105\%$ |
| 6 | $0{,}027919$ | $0{,}0388\%$ |
| 10 | $0{,}0072607$ | $0{,}0101\%$ |

### 4.3. Análisis de los resultados teóricos

La solución teórica revela la estructura de la señal: un **nivel DC** de $A/\pi$, un **rizado fundamental** a 60 Hz de amplitud $A/2$ —el término dominante— y una cola de **armónicos pares** (120, 240, 360 Hz…) cuya amplitud decae como $1/(4k^2-1)$. La ausencia de armónicos impares superiores al primero explica la "escalera" observada en la simulación. El resultado es coherente con la física del rectificador: el término continuo de $5{,}40$ V es el valor medio que entregaría a una carga, y la fundamental de $8{,}49$ V constituye el rizado principal que un filtro debería atenuar.

Finalmente, la Tabla 4 confronta el error cuadrático medio obtenido por la fórmula teórica y por la simulación numérica, cerrando el objetivo del avance.

**Tabla 4.** Comparación del error cuadrático medio: teórico vs. simulado.

| $k$ | $E_k$ teórico [V²] | $E_k$ simulado [V²] | Diferencia relativa |
| --- | ------------------ | ------------------- | ------------------- |
| 1 | $6{,}81950$ | $6{,}81950$ | $<0{,}001\%$ |
| 2 | $0{,}334943$ | $0{,}334944$ | $<0{,}001\%$ |
| 4 | $0{,}0755611$ | $0{,}0755617$ | $0{,}001\%$ |
| 6 | $0{,}0279195$ | $0{,}0279199$ | $0{,}002\%$ |
| 10 | $0{,}00726069$ | $0{,}00726096$ | $0{,}004\%$ |

La coincidencia entre ambos métodos es **inferior al 0,01 %** en todo el rango analizado. Este acuerdo, obtenido por dos vías independientes —la integral simbólica de Parseval y la cuadratura numérica de Octave—, valida simultáneamente la corrección de la Serie de Fourier deducida analíticamente y de su implementación en el simulador, cumpliendo el objetivo principal del avance.

## 5. Referencias bibliográficas

Boylestad, R. L., & Nashelsky, L. (2009). *Electrónica: Teoría de circuitos y dispositivos electrónicos* (10.ª ed.). Pearson Educación.

Eaton, J. W., Bateman, D., Hauberg, S., & Wehbring, R. (2024). *GNU Octave: A high-level interactive language for numerical computations*. https://octave.org/doc/

Hsu, H. P. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano.

Oppenheim, A. V., & Willsky, A. S. (1998). *Señales y sistemas* (2.ª ed.). Prentice Hall.
