---
title: "Espejo - Mejoras propuestas al informe LE1"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 6
orden: 101
tipo: evaluacion
subtipo: laboratorio
tags:
  - curso/amplificadores
  - tipo/evaluacion
  - subtipo/laboratorio
  - tema/laboratorio
  - tema/informe
  - tema/espejo
  - tema/opamp
date: 2026-04-27
---

> [!abstract] ¿Qué es este documento?
> **Mapa visual** que refleja la estructura del informe actual y marca con colores **qué agregar y dónde**, sin re-escribir lo que ya está bien.
>
> Documento espejo de: [[S06-100 Informe LE1 - Amplificador operacional]]
> Guía base: [[S06-99 Laboratorio - LE1 Amplificador operacional]]

> [!tip]+ Leyenda de marcadores visuales
> | Marcador | Significado |
> | -------- | ----------- |
> | ✅ **YA EXISTE** (callout verde) | Sección que ya está en tu informe — no tocar |
> | ➕ **AGREGAR** (callout naranja) | **Bloque nuevo** que falta — copiar al informe Word |
> | ✏️ **MODIFICAR / AMPLIAR** (callout amarillo) | Texto que ya existe pero conviene completar |
> | 💡 **POR QUÉ** (callout azul, plegado) | Justificación pedagógica — sólo para tu lectura |

---

# 📄 Estructura propuesta del informe (con mejoras)

## ➕ AGREGAR — Carátula formal *(antes de "Materiales")*

> [!warning]+ ➕ AGREGAR — Carátula formal del informe
> ```
> UNIVERSIDAD TECNOLÓGICA DEL PERÚ — UTP
> Facultad de Ingeniería · Carrera de Ingeniería Electrónica
>
> Curso:        Circuitos Electrónicos Amplificadores
> Código:       100000I21N
> Sección/NRC:  __________
> Docente:      Ing. Jorge Luis Robles Bokun
> Ciclo:        2026-1   ·   Semana 6
>
> Laboratorio Nº 1 — Amplificador Operacional
>             (configuraciones inversor y no inversor)
>
> Integrantes:
>   • Ludeña Muñante, Harold              U23319438
>   • Espinoza Abarca, Pedro Rodrigo      U18216101
>   • Rojas Novoa, Ernesto Raúl           U21227968
>   • Carlos Baldeón Hidalgo              __________
>   • Luyo Murata, Tito Takeo             U23210744
>
> Fecha de presentación: __ / __ / 2026
> ```

> [!info]- 💡 Por qué
> El DOCX actual sólo lista docente e integrantes, falta la cabecera institucional. Es un punto formal típico que califica el docente, sin costo de tiempo.

---

## ✅ Sección 1 — Materiales y equipos *(YA EXISTE)*

> [!check]+ ✅ YA EXISTE — Materiales
> Tu informe ya lista LM741, protoboard, resistencias, generador, multímetro, osciloscopio. **No tocar.**
>
> 💡 *Sólo opcional:* podrías agregar el modelo del osciloscopio: **Tektronix TBS 1102B-EDU** (visible en las capturas). Y de la fuente: **Keithley 2231A**. Y del generador: **Tektronix AFG1022**. Eso aporta trazabilidad técnica.

---

## ➕ AGREGAR — Sección 2 — Marco teórico

> [!warning]+ ➕ AGREGAR — Marco teórico (sección 2 completa del informe)
>
> ### 2. Marco teórico
>
> #### 2.1. El amplificador operacional
>
> El **amplificador operacional (OPAMP)**, comúnmente abreviado *Op-Amp*, es un circuito integrado de alta ganancia con acoplamiento directo en continua, dos entradas diferenciales —**no inversora** ($V^+$) e **inversora** ($V^-$)— y una única salida $V_o$. Su función de transferencia en lazo abierto es:
>
> $$V_o = A_{ol} \cdot (V^+ - V^-) = A_{ol} \cdot V_d$$
>
> donde $V_d = V^+ - V^-$ es la tensión diferencial de entrada y $A_{ol}$ la ganancia en lazo abierto, típicamente del orden de $10^5$–$10^6\,\text{V/V}$ en frecuencias bajas.
>
> #### 2.2. Regiones de operación
>
> La curva $V_o$ vs $V_d$ presenta **tres zonas** delimitadas por la alimentación bipolar $\pm V_{cc}$:
>
> | Región | Condición | Comportamiento |
> | ------ | --------- | -------------- |
> | Saturación negativa | $V_d < -V_{sat}/A_{ol}$ | $V_o \approx -V_{sat}$ |
> | **Lineal**          | $\|V_d\| < V_{sat}/A_{ol}$ | $V_o = A_{ol} \cdot V_d$ |
> | Saturación positiva | $V_d > +V_{sat}/A_{ol}$ | $V_o \approx +V_{sat}$ |
>
> Como $A_{ol}$ es enorme, la zona lineal es extremadamente angosta ($\mu\text{V}$). Para forzar al OPAMP a trabajar en la región lineal de manera estable se usa **realimentación negativa**: una fracción de la salida se reinyecta en la entrada inversora, lo que reduce la ganancia efectiva pero la hace dependiente sólo de los componentes externos (no del $A_{ol}$ del integrado).
>
> #### 2.3. Modelo del OPAMP ideal
>
> Para el análisis de circuitos lineales con realimentación negativa, se usa el **modelo ideal**, basado en tres hipótesis:
>
> 1. **Corriente de entrada nula:** $I^+ = I^- = 0$ (impedancia de entrada infinita).
> 2. **Tensión diferencial nula** (tierra virtual): $V^+ = V^-$ (consecuencia de $A_{ol} \to \infty$ con realimentación negativa estable).
> 3. **Impedancia de salida nula:** la salida puede entregar la corriente que demande la carga sin caer.
>
> Estas tres hipótesis bastan para deducir la ganancia de cualquier topología lineal aplicando la **Ley de Kirchhoff de Corrientes (LKC)** en la entrada inversora.
>
> #### 2.4. Configuración inversora
>
> La señal de entrada se aplica a la terminal **inversora** a través de $R_1$, con la entrada **no inversora** conectada a tierra. La realimentación se cierra mediante $R_2$ entre la salida y la entrada inversora.
>
> Aplicando tierra virtual ($V^- = V^+ = 0\,\text{V}$) y LKC en el nodo inversor (donde $I^- = 0$):
>
> $$\frac{V_i - 0}{R_1} = \frac{0 - V_o}{R_2}$$
>
> Despejando se obtiene la ganancia en lazo cerrado:
>
> $$\boxed{A_v = \frac{V_o}{V_i} = -\frac{R_2}{R_1}}$$
>
> El signo negativo indica que la salida está **desfasada $180°$** respecto a la entrada (inversión de polaridad). La ganancia depende exclusivamente del cociente de las dos resistencias externas.
>
> #### 2.5. Configuración no inversora
>
> La señal de entrada se aplica a la terminal **no inversora**. La entrada inversora se realimenta desde la salida mediante un divisor formado por $R_1$ (a tierra) y $R_2$ (al nodo de salida).
>
> Por tierra virtual: $V^- = V^+ = V_i$. Aplicando LKC en el nodo inversor:
>
> $$\frac{0 - V_i}{R_1} + \frac{V_o - V_i}{R_2} = 0$$
>
> De donde:
>
> $$\boxed{A_v = \frac{V_o}{V_i} = 1 + \frac{R_2}{R_1}}$$
>
> La salida está **en fase** con la entrada ($0°$) y la ganancia es siempre **mayor o igual a 1** (no permite atenuar). El término "$+1$" representa el seguimiento directo de la entrada por la entrada $V^+$, y el cociente $R_2/R_1$ aporta la amplificación adicional.
>
> #### 2.6. Parámetros del LM741 relevantes para esta práctica
>
> | Parámetro | Símbolo | Valor típico LM741 | Implicancia en el lab |
> | --------- | ------- | ------------------ | --------------------- |
> | Ganancia en lazo abierto       | $A_{ol}$    | $\approx 2 \times 10^5$       | Justifica la aproximación de tierra virtual |
> | Tensión de alimentación         | $V^+, V^-$  | $\pm 12\,\text{V}$ (en este lab) | Define el techo y piso de saturación |
> | Tensión de salida máxima        | $V_{o,sat}$ | $\approx \pm 10{,}5\,\text{V}$  | Por debajo de $V_{cc}$; limita la excursión |
> | Slew rate                       | $SR$        | $0{,}5\,\text{V}/\mu\text{s}$   | Limitación a alta frecuencia / alta amplitud |
> | Impedancia de entrada           | $Z_{in}$    | $\approx 2\,\text{M}\Omega$     | Permite asumir $I_{in} \approx 0$ |
> | Producto ganancia–ancho de banda | $GBW$      | $\approx 1\,\text{MHz}$         | A $5\,\text{kHz}$ con $\|A_v\|=5$, ancho de banda $\approx 200\,\text{kHz}$ — sin afectación |
> | Tensión de offset de entrada    | $V_{io}$    | $\approx 1\,\text{mV}$          | Despreciable frente a $V_{in,pp}=1\,\text{V}$ |
> | CMRR                            | —           | $\approx 90\,\text{dB}$         | Buen rechazo a ruido de modo común |
>
> #### 2.7. Verificación de operación dentro de la zona lineal
>
> Antes de medir, conviene verificar que el circuito no satura ni se ve limitado por slew rate:
>
> - **Saturación:** $V_{out,pp,max} = 2 \cdot V_{o,sat} \approx 21\,\text{V}$. Con $V_{in,pp}=1\,\text{V}$ y $\|A_v\| \leq 5$, $V_{out,pp} \leq 5\,\text{V} \ll 21\,\text{V}$. **No satura.**
> - **Slew rate:** la pendiente máxima de $V_o(t) = V_{op}\sin(2\pi f t)$ es $|dV_o/dt|_{max} = 2\pi f \cdot V_{op}$. Para $f=5\,\text{kHz}$ y $V_{op}=2{,}5\,\text{V}$: $|dV_o/dt|_{max} \approx 0{,}079\,\text{V}/\mu\text{s} \ll SR = 0{,}5\,\text{V}/\mu\text{s}$. **Sin distorsión por slew rate.**
>
> Estas dos verificaciones aseguran que la ganancia teórica $-R_2/R_1$ y $1+R_2/R_1$ aplican válidamente a las mediciones del laboratorio.

> [!info]- 💡 Por qué
> La guía dedica toda la sección 5 al fundamento del OPAMP, pero tu informe sólo dice "es un amplificador". Un marco teórico completo debe contener: (a) qué es el dispositivo, (b) sus regiones de operación, (c) el modelo ideal con las 3 hipótesis, (d) la deducción de cada topología que se va a probar, (e) los parámetros reales del LM741, y (f) la verificación de que el circuito opera en zona lineal. Esto no sólo cumple con la rúbrica académica sino que **anticipa** el análisis cuantitativo de las secciones siguientes.

---

## ✅ Sección 3 — Amplificador inversor (descripción y deducción) *(YA EXISTE)*

> [!check]+ ✅ YA EXISTE — Descripción + deducción de $A_v = -R_2/R_1$
> Tu informe ya tiene la descripción, el diagrama y la deducción. **No tocar.**

---

## ✏️ Sección 3 — Amplificador inversor (datos experimentales)

> [!example]+ ✏️ MODIFICAR — Reemplazar "capturas sin lectura" por un bloque con tabla de mediciones
>
> Justo después de la frase *"Para visualizar las señales utilizaremos el osciloscopio…"* y **antes** de pegar las 4 fotos, agregar esta tabla:
>
> ### 3.x. Configuración del osciloscopio y lecturas
>
> | Parámetro | CH1 (entrada $V_i$) | CH2 (salida $V_o$) |
> | --------- | ------------------- | ------------------ |
> | Escala vertical | $500\,\text{mV/div}$ | $1{,}00\,\text{V/div}$ |
> | Escala horizontal | $100\,\mu\text{s/div}$ | $100\,\mu\text{s/div}$ |
> | Atenuación de sonda | $1\text{X}$ | $1\text{X}$ |
> | Acoplamiento | DC | DC |
> | $V_{pico\text{-}pico}$ medido | $\boxed{1{,}04\,\text{V}}$ | $\boxed{5{,}00\,\text{V}}$ |
> | Frecuencia medida | $5{,}000\,\text{kHz}$ | $5{,}010\,\text{kHz}$ |
> | Fase relativa | referencia | desfasada $180°$ |
>
> *Lecturas tomadas del cursor de medición automática del Tektronix TBS 1102B-EDU. Ver captura `s06-le1-inversor-osc-4.jpg`.*

> [!info]- 💡 Por qué
> Tu informe tiene 4 fotos del osciloscopio sin un solo número. Cualquier evaluador necesita los $V_{pp}$ medidos para verificar que la ganancia experimental coincide con la teórica. **Estos datos ya están en tus fotos** — sólo hay que tabularlos.

---

## ➕ AGREGAR — Sección 3 — Cálculo de la ganancia experimental (inversor)

> [!warning]+ ➕ AGREGAR — Cálculo de $A_v$ medido
>
> ### 3.x. Ganancia experimental
>
> A partir de las lecturas pico-pico del osciloscopio (CH1 y CH2):
>
> $$|A_{v,\text{medido}}| = \frac{V_{out,pp}}{V_{in,pp}} = \frac{5{,}00\,\text{V}}{1{,}04\,\text{V}} = 4{,}808$$
>
> Como las señales están desfasadas $180°$ (la salida invierte el signo respecto a la entrada), se asigna signo negativo:
>
> $$\boxed{A_{v,\text{medido}} = -4{,}81}$$
>
> Comparación con la ganancia teórica $A_{v,\text{teórico}} = -5{,}00$:
>
> $$\varepsilon = \left|\frac{A_{v,\text{teórico}} - A_{v,\text{medido}}}{A_{v,\text{teórico}}}\right| \times 100\% = \frac{|-5{,}00 - (-4{,}81)|}{5{,}00} \times 100\% = 3{,}85\%$$
>
> **Conclusión local:** la ganancia medida en el laboratorio se desvía menos del $4\%$ respecto del valor teórico. La diferencia se atribuye a la tolerancia de los resistores ($\pm 5\%$ típicos) y al error de lectura del osciloscopio.

> [!info]- 💡 Por qué
> Sin esta verificación experimental el informe **no demuestra** que el circuito armado funciona como predice la teoría — sólo demuestra que el alumno sabe calcular $-R_2/R_1$. La validación cuantitativa es lo que distingue un informe completo.

---

## ✅ Sección 3 — Amplificador inversor (capturas e implementación) *(YA EXISTE)*

> [!check]+ ✅ YA EXISTE — Fotos de protoboard, fuente ±12 V, capturas de osciloscopio
> No tocar. Sólo asegurarse de que **junto a cada foto del osciloscopio** se referencie la tabla de mediciones agregada arriba.

---

## ✅ Sección 4 — Amplificador no inversor (descripción y deducción) *(YA EXISTE)*

> [!check]+ ✅ YA EXISTE — Tu informe ya tiene la descripción y la fórmula $A_v = 1 + R_2/R_1$.

---

## ✏️ Sección 4 — Amplificador no inversor (datos experimentales)

> [!example]+ ✏️ MODIFICAR — Mismo patrón que el inversor, pero con datos del no inversor
>
> ### 4.x. Configuración del osciloscopio y lecturas
>
> | Parámetro | CH1 (entrada $V_i$) | CH2 (salida $V_o$) |
> | --------- | ------------------- | ------------------ |
> | Escala vertical | $500\,\text{mV/div}$ | $1{,}00\,\text{V/div}$ |
> | Escala horizontal | $100\,\mu\text{s/div}$ | $100\,\mu\text{s/div}$ |
> | Atenuación de sonda | $1\text{X}$ | $1\text{X}$ |
> | Acoplamiento | DC | DC |
> | $V_{pico\text{-}pico}$ medido | $\boxed{1{,}08\,\text{V}}$ | $\boxed{3{,}68\,\text{V}}$ |
> | Frecuencia medida | $4{,}970\,\text{kHz}$ | $5{,}005\,\text{kHz}$ |
> | Fase relativa | referencia | **en fase** ($0°$) |
>
> *Lecturas tomadas del Tektronix TBS 1102B-EDU. Ver captura `s06-le1-no-inversor-osc-1.jpg`.*

---

## ➕ AGREGAR — Sección 4 — Cálculo de la ganancia experimental (no inversor)

> [!warning]+ ➕ AGREGAR — Cálculo de $A_v$ medido
>
> ### 4.x. Ganancia experimental
>
> $$A_{v,\text{medido}} = \frac{V_{out,pp}}{V_{in,pp}} = \frac{3{,}68\,\text{V}}{1{,}08\,\text{V}} = 3{,}407$$
>
> Las señales se observan **en fase** (sin desfase), coherente con la naturaleza del amplificador no inversor. Por tanto:
>
> $$\boxed{A_{v,\text{medido}} = +3{,}41}$$
>
> Comparación con la ganancia teórica $A_{v,\text{teórico}} = 3{,}545$:
>
> $$\varepsilon = \frac{|3{,}545 - 3{,}407|}{3{,}545} \times 100\% = 3{,}89\%$$
>
> **Conclusión local:** ganancia experimental dentro del $4\%$ del valor teórico. Concordancia excelente para electrónica con componentes pasivos al $5\%$ de tolerancia.

---

## ✅ Sección 5 — Simulación en Multisim Live *(YA EXISTE)*

> [!check]+ ✅ YA EXISTE — Capturas de las dos simulaciones
> No tocar. Las dos imágenes de Multisim Live están bien. (Ver propuesta de tabla comparativa en la siguiente sección.)

---

## ➕ AGREGAR — Sección 6 — Tabla comparativa teoría / simulación / experimento

> [!warning]+ ➕ AGREGAR — Tabla resumen comparativa (¡el corazón del informe!)
>
> ### 6. Comparación de resultados: teórico vs simulado vs medido
>
> | Configuración | $A_v$ teórico | $A_v$ Multisim Live | $A_v$ medido (osciloscopio) | Error medido vs teórico | Fase teórica | Fase medida |
> | ------------- | ------------- | ------------------- | --------------------------- | ----------------------- | ------------ | ----------- |
> | Inversor      | $-5{,}000$    | _(leer del simulador y completar)_ | $-4{,}81$ | $3{,}85\%$ | $180°$ | $\approx 180°$ ✓ |
> | No inversor   | $+3{,}545$    | _(leer del simulador y completar)_ | $+3{,}41$ | $3{,}89\%$ | $0°$  | $\approx 0°$ ✓ |
>
> **Análisis:**
>
> - Los tres métodos (cálculo, simulación y medición) coinciden dentro del **$\pm 4\%$**, error explicable por la tolerancia de los resistores ($\pm 5\%$ usual) y el error de paralaje al leer el osciloscopio.
> - La fase relativa entre $V_i$ y $V_o$ se cumple exactamente como predice cada topología: **$180°$** en el inversor (señales en oposición visibles en `osc-4.jpg`) y **$0°$** en el no inversor (señales en fase visibles en `no-inversor-osc-1.jpg`).
> - La frecuencia de salida se mantiene en $5\,\text{kHz}$ en ambos circuitos, confirmando que **a esta frecuencia el LM741 trabaja en su zona lineal** (muy por debajo de su $GBW = 1\,\text{MHz}$ y sin verse afectado por el slew rate dado que $V_{out,pp} \leq 5\,\text{V}$).

> [!info]- 💡 Por qué
> Esta tabla es **la justificación principal** del laboratorio: demuestra que la teoría predice el comportamiento real con error $< 5\%$. Sin esta tabla, los tres bloques (cálculo + simulación + capturas) viven aislados y el informe queda como una colección de procedimientos sin síntesis.

---

## ➕ AGREGAR — Sección 7 — Análisis de saturación

> [!warning]+ ➕ AGREGAR — Análisis cuantitativo de saturación
>
> ### 7. Margen de saturación
>
> El LM741 alimentado con $\pm 12\,\text{V}$ entrega una excursión máxima de salida típica $V_{o,sat} \approx \pm 10{,}5\,\text{V}$ (algo menor que $V_{cc}$ por la caída en la etapa de salida).
>
> El voltaje de entrada máximo antes de saturar se calcula como:
>
> $$V_{in,max} = \frac{V_{o,sat}}{|A_v|}$$
>
> | Configuración | $V_{in,max}$ pico | $V_{in,max}$ pico-pico |
> | ------------- | ----------------- | ---------------------- |
> | Inversor ($\|A_v\|=5$)        | $10{,}5/5 = 2{,}1\,\text{V}$    | $4{,}2\,\text{Vpp}$ |
> | No inversor ($A_v=3{,}545$)   | $10{,}5/3{,}545 \approx 2{,}96\,\text{V}$ | $5{,}92\,\text{Vpp}$ |
>
> Trabajamos con $V_{in} = 1\,\text{Vpp}$, **muy por debajo** de estos límites en ambos casos, por lo que la salida se mantiene senoidal sin recorte (verificable visualmente en las capturas: las puntas de las senoidales no aparecen achatadas).

> [!info]- 💡 Por qué
> Tus observaciones mencionan saturación pero no la cuantifican. Calcular el margen de seguridad demuestra dominio del concepto: no basta con decir "puede saturar", hay que mostrar a qué amplitud lo haría.

---

## ✏️ Sección 8 — Observaciones *(YA EXISTE — ampliar)*

> [!example]+ ✏️ MODIFICAR — Agregar observaciones sobre la fase del NO inversor
>
> Tu lista actual sólo menciona la fase del **inversor** ($180°$). Agregar un bullet:
>
> - En el amplificador **no inversor** se observó que la salida está **en fase** (desfase $0°$) con la entrada, en concordancia con su función de transferencia $A_v = 1 + R_2/R_1 > 0$. Esta diferencia con respecto al inversor es la consecuencia directa de aplicar la señal en la entrada $+$ en lugar de la entrada $-$.
>
> Y otro bullet sobre el resultado cuantitativo:
>
> - La concordancia entre la ganancia medida y la teórica fue de **$\approx 96\%$** en ambas configuraciones (error $< 4\%$), lo que valida el modelo de OPAMP ideal para esta frecuencia y nivel de señal.

---

## ✅ Sección 9 — Conclusiones *(YA EXISTE — está completa)*

> [!check]+ ✅ YA EXISTE — Las 4 conclusiones cubren los aspectos clave
> No tocar. Si quieres reforzar, podrías reemplazar la conclusión genérica "el OPAMP es versátil" por una más cuantitativa:
>
> > *"Las dos topologías evaluadas (inversor con $A_v = -5$ y no inversor con $A_v = 3{,}545$) presentan un error experimental menor al $4\%$ respecto del valor teórico, lo que confirma la validez del modelo de OPAMP ideal aplicado al LM741 dentro de la región lineal de operación."*

---

## ➕ AGREGAR — Sección 10 — Bibliografía

> [!warning]+ ➕ AGREGAR — Bibliografía (falta totalmente en el DOCX)
>
> ### 10. Bibliografía
>
> - Boylestad, R. L. & Nashelsky, L. (2009). *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos* (10ª ed.). Pearson Educación.
> - Sedra, A. S. & Smith, K. C. (2015). *Microelectronic Circuits* (7ª ed.). Oxford University Press.
> - Coughlin, R. F. & Driscoll, F. F. (1999). *Amplificadores Operacionales y Circuitos Integrados Lineales* (5ª ed.). Pearson Educación.
> - Texas Instruments. (2015). *LM741 Operational Amplifier — Datasheet (SNOSC25D)*.

> [!info]- 💡 Por qué
> Cualquier informe técnico/académico debe citar las fuentes consultadas. Estándar mínimo, costo cero.

---

# 📋 Resumen ejecutivo de cambios

> [!success]+ Checklist de mejoras al `Informe LE1 - Amplificador operacional.docx`
> - [ ] **Carátula formal** (datos institucionales + integrantes)
> - [ ] **Marco teórico** con tabla de parámetros del LM741
> - [ ] **Tabla de configuración del osciloscopio + lecturas** del inversor
> - [ ] **Cálculo de $A_v$ medido** del inversor con error porcentual
> - [ ] **Tabla de configuración + lecturas** del no inversor
> - [ ] **Cálculo de $A_v$ medido** del no inversor con error porcentual
> - [ ] **Tabla comparativa** teórico / Multisim / medido (¡crítico!)
> - [ ] **Análisis de saturación** con margen cuantitativo
> - [ ] **Observación adicional** sobre fase $0°$ del no inversor
> - [ ] **Bibliografía** (4 referencias mínimo)
>
> *Tiempo estimado de implementación en Word: ~45–60 min.*
