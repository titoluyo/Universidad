---
title: "Proyecto 1 (Fourier) — Plan de trabajo"
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

# Proyecto 1 — Serie de Fourier · Plan de trabajo

> [!info] Alcance de esta nota
> Plan detallado para desarrollar el **Proyecto 1** (serie de Fourier del seno rectificado de media onda + simulación en Octave). Generado a partir de [[Proyecto1/00 - Brief y alcance|el brief]], la consigna [[S18-98 PROY Indicaciones|PROY]] y el avance [[S16-98 APF Indicaciones|APF]]. **Solo planifica**: el desarrollo se ejecuta en las etapas indicadas abajo.

> [!warning] Contexto de calendario al 13 jul 2026
> Hoy **lunes 13 de julio** vence el **APF (15%, 11:59 p.m.)**. El **PROY (30%)** abre el lun 20 jul y cierra el **mar 21 jul, 11:59 p.m., con 1 solo intento**. El cronograma de este plan parte de hoy.

## 1. Objetivos

**Objetivo general:** obtener la serie de Fourier de una señal senoidal rectificada de **media onda** por vía **analítica** y por **simulación en GNU Octave**, comparando ambos resultados mediante el **error cuadrático medio**, y comunicar el proceso en un documento PDF (10–20 pág, APA 7) y un video ≤ 5 min, cubriendo los 20 pts de la rúbrica.

**Objetivos específicos:**

1. Definir matemáticamente la señal $f(t)$ (seno rectificado de media onda) con valores concretos de $A$ y $T$, y graficarla.
2. Calcular analíticamente $a_0$, $a_n$ y $b_n$ resolviendo las integrales paso a paso, y escribir la serie de Fourier resultante.
3. Implementar en Octave la reconstrucción de la señal con $N$ términos y graficar aproximación vs. señal original para varios $N$.
4. Calcular el error cuadrático medio $E_k$ por teoría (fórmula reducida) y por simulación (numérico), y compararlos.
5. Redactar el documento final según el [[05 - Documento final (esqueleto)|esqueleto]] y producir el video según el [[06 - Guion del video|guion]].

## 2. Definición concreta del caso

**Señal** (un periodo):

$$f(t) = \begin{cases} A\sin(\omega_0 t), & 0 \le t < T/2 \\[4pt] 0, & T/2 \le t < T \end{cases} \qquad \omega_0 = \frac{2\pi}{T}$$

**Valores propuestos:** $A = 12\sqrt{2} \approx 16{,}97\ \text{V}$ y $T = 1/60\ \text{s} \approx 16{,}67\ \text{ms}$ ($f = 60\ \text{Hz}$, $\omega_0 = 120\pi \approx 376{,}99\ \text{rad/s}$).

> [!note] Justificación
> El contexto de *Electronics S.A.* sugiere una etapa de **rectificación de media onda en una fuente de alimentación**: un transformador reduce la red peruana (220 V RMS, **60 Hz**) a un secundario típico de **12 V RMS**, cuya amplitud pico es $A = 12\sqrt{2}$. Usar la frecuencia real de la red (60 Hz en Perú) da verosimilitud de ingeniería y aporta material para la introducción/antecedentes. El desarrollo analítico se hará **simbólico en $A$ y $\omega_0$** (resultado general) y los valores numéricos se usan solo en gráficas y tablas — así un cambio de valores no invalida la teoría.

**Resultado analítico esperado** (referencia de control para validar el desarrollo):

$$f(t) = \frac{A}{\pi} + \frac{A}{2}\sin(\omega_0 t) - \frac{2A}{\pi}\sum_{k=1}^{\infty}\frac{\cos(2k\,\omega_0 t)}{4k^2 - 1}$$

## 3. Desglose de etapas → tareas → subtareas

### Etapa T — Desarrollo analítico (teoría) → [[03 - Desarrollo analitico (teoria)]]

- **T1. Definir y graficar la señal**
	- T1.1 Escribir $f(t)$ por tramos, identificar $T$, $\omega_0$ y verificar que **no** hay paridad aprovechable completa (la media onda no es par ni impar — a diferencia de la onda completa de [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|S12-3]]).
	- T1.2 Graficar 2–3 periodos (Octave) para la figura 1 del documento.
- **T2. Calcular los coeficientes** con las fórmulas de [[S11-2 Tema 02 - Series de Fourier|S11-2]] (integrando solo en $[0, T/2]$ porque $f=0$ en el resto):
	- T2.1 $a_0 = \frac{2}{T}\int_0^{T/2} A\sin(\omega_0 t)\,dt = \frac{2A}{\pi}$ → valor DC $\frac{a_0}{2} = \frac{A}{\pi}$.
	- T2.2 $a_n$ vía identidad producto→suma ($\sin\alpha\cos\beta$): tratar **aparte el caso $n=1$** (la fórmula general divide por $n^2-1$); resultado: $a_1 = 0$, $a_n = -\frac{2A}{\pi(n^2-1)}$ para $n$ par, $0$ para $n$ impar $\ge 3$.
	- T2.3 $b_n$ vía identidad $\sin\alpha\sin\beta$: tratar **aparte $n=1$** → $b_1 = \frac{A}{2}$, $b_n = 0$ para $n \ge 2$.
	- T2.4 Escribir la serie final (caja de resultado) y contrastar con la referencia de § 2.
- **T3. Error cuadrático teórico** con la fórmula reducida de [[S12-0 Tema 01 - Analisis de las series de Fourier|S12-0]]:
	- T3.1 Potencia media: $\frac{1}{T}\int_0^{T}[f(t)]^2 dt = \frac{A^2}{4}$.
	- T3.2 Evaluar $E_k = \frac{A^2}{4} - \frac{a_0^2}{4} - \frac{1}{2}\sum_{n=1}^{k}(a_n^2 + b_n^2)$ para $k = 1, 2, 4, 6, 10$ (tabla).
	- T3.3 Comentar la convergencia (señal continua → sin [[S12-0 Tema 01 - Analisis de las series de Fourier#3. Fenómeno de Gibbs|Gibbs]], error decae rápido), reutilizando el método de [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|S12-3]].

### Etapa S — Simulación en Octave → [[04 - Simulacion (Octave o LTSPICE)]]

- **S1. Script base** (`proyecto1_fourier.m`):
	- S1.1 Definir `A`, `T`, `w0`, vector `t` (≥ 2 periodos, paso fino p. ej. `T/2000`).
	- S1.2 Señal original por tramos: `f = A*sin(w0*t).*(sin(w0*t)>=0)` (equivalente a media onda).
	- S1.3 Reconstrucción $S_N(t)$ con bucle `for` sumando DC + $b_1$ + armónicos pares (coeficientes **teóricos**).
- **S2. Gráficas** (todas numeradas, con título, ejes y `grid on`):
	- S2.1 Señal original (Figura 1).
	- S2.2 Superposición $f(t)$ vs. $S_N(t)$ para $N = 1, 2, 4, 10$ (subplots o figuras separadas).
	- S2.3 Curva $E_k$ vs. $k$ (escala semilogarítmica) — insumo clave de la discusión.
- **S3. Error simulado:**
	- S3.1 Error numérico: $E_k^{sim} = \frac{1}{T}\int_0^T [f - S_k]^2 dt$ con `trapz`.
	- S3.2 Tabla comparativa $E_k$ teórico vs. $E_k^{sim}$ y diferencia relativa (%).
- **S4. Empaquetar evidencia:** capturas del script + consola + figuras exportadas (`print -dpng`) hacia `attachments/` de la carpeta del proyecto; código completo al anexo.

### Etapa D — Documento PDF → [[05 - Documento final (esqueleto)]]

- **D1. Marco previo:** introducción en prosa (antecedentes de rectificación/Fourier + objetivo principal) y marco teórico (serie de Fourier, coeficientes, error cuadrático, qué es Octave) con citas de [[01 - Busqueda de fuentes (APA)]].
- **D2. Desarrollo:** volcar Etapa T (solución teórica) y Etapa S (simulación) con figuras y tablas numeradas y definidas en el índice.
- **D3. Discusión y conclusiones:** comparación teórico vs. simulado **con el error** (tabla S3.2 + curva S2.3); conclusión de resultados simulados, de resultados teóricos y de la discusión global — los 4 sub-ítems del criterio 5 de la rúbrica.
- **D4. Formato:** exportar con [[../../../utils/md_to_docx.py|md_to_docx]] (Arial 12, interlineado 1.5), verificar 10–20 páginas, índice con lista de tablas/figuras, citas APA en texto **y en cada imagen**, referencias APA 7.

### Etapa V — Video ≤ 5 min → [[06 - Guion del video]]

- V1. Completar el guion por bloques (título → objetivos → metodología → análisis → conclusiones) con los resultados reales.
- V2. Grabar compartiendo pantalla (gráficas de S2 + ecuaciones de T2); **todos los integrantes** aparecen si es grupal.
- V3. Editar a ≤ 5:00, subir a Drive/YouTube (enlace público o con acceso), pegar el enlace en el documento y en la entrega.

### Etapa E — Entrega

- E1. **APF (hoy 13 jul):** PDF con introducción + marco teórico + desarrollo teórico y simulación base (sin exigir discusión del error ni video).
- E2. **PROY (21 jul):** PDF completo + enlace del video, subido en el único intento; verificar tipos de archivo admitidos y ≤ 500 MB.

## 4. Cronograma (fechas reales)

| Fecha      | Día     | Tareas                                                                                  | Hito                   |
| ---------- | ------- | --------------------------------------------------------------------------------------- | ---------------------- |
| **13 jul** | lun     | Cerrar T1–T2 + S1–S2 básicos; ensamblar y **entregar APF**                              | 🔴 **APF 11:59 p.m.**  |
| 14–15 jul  | mar–mié | T3 completo (tabla $E_k$ teórico); S3 (error simulado + comparativa)                    | Núcleo técnico cerrado |
| 16–17 jul  | jue–vie | D1–D3: redacción completa de discusión y conclusiones; pulir figuras/tablas             | Borrador PDF completo  |
| 18 jul     | sáb     | D4: formato, índice, APA en texto e imágenes; export a PDF; V1 (guion con datos reales) | PDF candidato          |
| 19 jul     | dom     | V2–V3: grabar, editar y subir el video; revisión cruzada con la rúbrica                 | Video en línea         |
| 20 jul     | lun     | Abre PROY: revisión final (checklist § 9), correcciones menores                         | Todo listo             |
| **21 jul** | mar     | E2: subir PDF + enlace del video (colchón: subir en la mañana, no al filo)              | 🔴 **PROY 11:59 p.m.** |

> [!tip] Qué queda listo en el APF y qué añade el PROY
> **APF (hoy):** introducción, marco teórico, desarrollo analítico (T1–T2), simulación con gráficas (S1–S2), referencias APA.
> **PROY (21 jul) añade:** error teórico vs. simulado (T3 + S3), **discusión y conclusiones** (D3) y **video** (Etapa V). Es exactamente el delta que señala la [[S18-98 PROY Indicaciones|consigna PROY]].

## 5. Entregables y definición de terminado (DoD)

| Etapa | Entregable | Definición de terminado |
| ----- | ---------- | ----------------------- |
| T | Nota [[03 - Desarrollo analitico (teoria)]] completa | Integrales paso a paso; casos $n=1$ tratados aparte; serie final en caja coincide con la referencia de § 2; tabla $E_k$ para $k=1,2,4,6,10$ |
| S | Script `.m` + figuras exportadas | Script corre sin errores en Octave; figuras con título/ejes/leyenda; $E_k^{sim}$ difiere del teórico < 1 % (paso de integración fino) |
| D | PDF 10–20 pág | Cumple Arial 12 / 1.5; índice con tablas y figuras; cada sección de la rúbrica presente; APA en texto e imágenes; sin citas inventadas |
| V | Enlace de video | ≤ 5:00 min; contiene los 5 bloques exigidos; enlace accesible probado en ventana de incógnito |
| E | Entrega en Canvas | APF entregado el 13 jul; PROY subido el 21 jul con PDF + enlace, confirmación de envío guardada |

## 6. Mapa tarea → criterio de rúbrica → puntos (20 pts)

| Criterio | pts | Tareas que lo cubren |
| -------- | --- | -------------------- |
| 1. Introducción | 2 | D1 (prosa, antecedentes, objetivo principal — § 1 de este plan) |
| 2. Marco teórico | 2 | D1 (definiciones de Fourier + propiedades usadas + **define Octave** + ecuaciones de coeficientes y error) |
| 3. Dominio de simulación | 3 | S1–S4 + D2 (mostrar el programa, presentar resultados, **analizar** resultados del simulador) |
| 4. Dominio teórico | 3 | T1–T3 + D2 (solución teórica completa, resultados, análisis) |
| 5. Discusión y conclusiones | 4 | T3 + S3 + D3 (comparación **con el error** + 3 conclusiones: simulado, teórico, discusión) |
| 6. Referencias APA | 3 | D4 + [[01 - Busqueda de fuentes (APA)]] (cita en texto, cita en imágenes, formato APA) |
| 7. Video | 3 | V1–V3 (título, objetivos, metodología, análisis, conclusiones, ≤ 5 min) |
| **Total** | **20** | |

## 7. Recursos y materiales

- **Teoría del vault:** [[S11-2 Tema 02 - Series de Fourier|S11-2 coeficientes]], [[S12-0 Tema 01 - Analisis de las series de Fourier|S12-0 error cuadrático y Gibbs]], [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|S12-3 método del error (onda completa)]].
- **Octave:** [[S16-5 Tema 02 - Programa Octave|S16-5 instalación y uso]]; instalar desde [octave.org](https://octave.org/download) si aún no está.
- **Consignas:** [[S18-98 PROY Indicaciones]] · [[S16-98 APF Indicaciones]].
- **Esqueleto y guion:** [[05 - Documento final (esqueleto)]] · [[06 - Guion del video]].
- **Bibliografía candidata a verificar** (no citar sin confirmar datos de edición):
	- Hsu, H. P. — *Análisis de Fourier* (ya citado en las notas del curso; confirmar edición/año).
	- Oppenheim, A. V. & Willsky, A. S. — *Señales y sistemas* (capítulo de series de Fourier).
	- Boylestad, R. / Sedra-Smith — capítulo de rectificación de media onda (para antecedentes de la introducción).
	- Documentación oficial de GNU Octave (para citar el simulador en el marco teórico).

## 8. Riesgos y mitigaciones

| Riesgo | Impacto | Mitigación |
| ------ | ------- | ---------- |
| **Confundir media onda con onda completa** ([[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|S12-3]] es onda completa: solo cosenos, $T=\pi$) | Serie incorrecta → pierde criterio 4 (3 pts) | La media onda tiene $T$ = periodo del seno original y término $b_1 = A/2$; validar contra la referencia de § 2 |
| **Caso $n=1$ mal tratado** (fórmulas generales dividen por $n^2-1$) | $a_1$, $b_1$ erróneos | Calcular $n=1$ con integral aparte antes de aplicar la fórmula general |
| **Errata de la consigna** (portal cruza los entregables de Proyecto 1 y 2; además dice "rectificada cuadrática" en el contexto) | Desarrollar el proyecto equivocado | Ya aclarado en [[S18-98 PROY Indicaciones]]: Proyecto 1 = **Fourier, media onda** |
| Error numérico en Octave (paso de `t` grueso, `trapz` impreciso) | $E_k^{sim}$ no cuadra con teoría | Paso ≤ $T/2000$; verificar convergencia duplicando la resolución |
| Documento fuera de rango (< 10 o > 20 pág) | Penalización de formato | Medir páginas al cierre de cada día de redacción; anexos para el código si falta espacio |
| Video > 5 min o enlace sin permisos | Pierde hasta 3 pts | Guion cronometrado (§ [[06 - Guion del video]]); probar enlace en incógnito |
| Ventana PROY de 1 solo intento (20–21 jul) | Entrega fallida sin reintento | Tener PDF y video listos el 19 jul; subir el 21 jul por la mañana |
| Modalidad aún sin cerrar (individual/grupal) | Afecta video (todos deben aparecer) y reparto | Cerrar hoy en [[00 - Brainstorming y eleccion]]; si grupal, asignar responsables en la tabla de [[02 - Planificacion y cronograma]] |

## 9. Checklist final de entrega (PROY)

- [ ] PDF en Arial 12, interlineado 1.5, **10–20 páginas**.
- [ ] Portada + índice con **lista de tablas y figuras numeradas** (cada una con breve definición).
- [ ] Introducción en prosa con antecedentes y objetivo principal.
- [ ] Marco teórico: Fourier + propiedades + **definición del simulador (Octave)** + ecuaciones.
- [ ] Desarrollo teórico completo ($a_0$, $a_n$, $b_n$, serie final) y simulación con código y gráficas.
- [ ] Comparación teórico vs. simulado **mostrando el error** + 3 conclusiones (criterio 5).
- [ ] Citas APA **en el texto y en cada imagen**; lista de referencias APA 7 verificadas (sin fuentes inventadas).
- [ ] Video ≤ 5 min con título, objetivos, metodología, análisis y conclusiones; todos los integrantes aparecen.
- [ ] Video subido a Drive/YouTube, enlace probado y pegado en el documento y en la entrega.
- [ ] PDF + enlace subidos a Canvas **antes** del mar 21 jul 11:59 p.m. (único intento); confirmación guardada.
