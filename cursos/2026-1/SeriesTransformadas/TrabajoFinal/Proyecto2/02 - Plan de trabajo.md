---
title: "Proyecto 2 (Laplace) — Plan de trabajo"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
  - tema/transformada-de-laplace
  - tema/circuito-rlc
date: 2026-07-13
---

# Proyecto 2 — Transformada de Laplace · Plan de trabajo

> [!info] Alcance de esta nota
> Plan detallado para desarrollar el **Proyecto 2** (voltaje del capacitor $V_o(t)$ por Laplace) del [[Trabajo Final - SyT MOC|Trabajo Final]]. Aquí **no se desarrolla** la solución: se planifica qué, cómo y cuándo. Consigna y rúbrica: [[S18-98 PROY Indicaciones]] · [[S16-98 APF Indicaciones]].

> [!danger] Calendario real — el plan original ya no aplica
> El prompt pedía "aprovechar la semana 16 para el APF", pero **hoy es lunes 13 de julio (inicio de semana 17)** y el **APF vence HOY 13 jul, 11:59 p.m.** El PROY abre el lun 20 jul y vence el **mar 21 jul, 11:59 p.m.** (1 solo intento). El cronograma de abajo está comprimido a los **9 días reales disponibles**, con una ruta de emergencia para el APF si aún no se entregó.

## 1. Objetivos

**Objetivo general:** determinar analíticamente el voltaje del capacitor $V_o(t)$ de un circuito RLC serie mediante la Transformada de Laplace, validarlo contra una simulación numérica y cuantificar el error entre ambos, documentando el proceso en un informe APA (10–20 pág) y un video ≤ 5 min.

**Objetivos específicos:**
1. Plantear la ecuación diferencial del circuito con condiciones iniciales mediante la ley de voltajes de Kirchhoff.
2. Resolver $V_o(s)$ vía Laplace, antitransformar por fracciones parciales y graficar $V_o(t)$ teórico.
3. Simular el mismo circuito en **GNU Octave** y obtener $V_o(t)$ simulado.
4. Comparar teoría vs. simulación punto a punto y calcular el error (absoluto, relativo y/o cuadrático medio).
5. Redactar el documento cubriendo los 7 criterios de la rúbrica (20 pts) y producir el video.

## 2. Definición del caso: circuito propuesto

> [!example] Circuito propuesto (a validar antes de la Etapa B)
> **RLC serie** alimentado por **fuente escalón** (interruptor que cierra en $t=0$), salida = voltaje en el capacitor.
>
> | Parámetro | Valor | Consecuencia |
> | --------- | ----- | ------------ |
> | $L$ | $1\ \text{H}$ | coeficientes limpios al dividir |
> | $R$ | $6\ \Omega$ | $R/L = 6$ |
> | $C$ | $0{,}04\ \text{F}$ | $1/LC = 25$ |
> | $E$ | $100\ \text{V}$ (escalón) | $V_o(\infty) = 100\ \text{V}$ |
>
> Ecuación característica $s^2 + 6s + 25 = (s+3)^2 + 4^2$ → **subamortiguado**, polos $-3 \pm 4j$.

**Justificación de la elección:**
- **Topología RLC serie + escalón** es exactamente la familia de problemas del curso ([[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|Ejercicio 2]] y [[S14-4 Tema 01 - Ejercicio 3 - Circuito RLC II|Ejercicio 3]]), por lo que el desarrollo analítico está respaldado por las notas y es defendible en el video.
- Los **valores son distintos** a los dos ejercicios resueltos en clase (polos $-4\pm3j$ y $-10\pm10j$), evitando entregar un problema copiado, pero producen números igual de limpios: se espera $V_o(t) = 100\left[1 - e^{-3t}\left(\cos 4t + \tfrac{3}{4}\sin 4t\right)\right]$ V (a verificar en la Etapa B).
- El caso **subamortiguado** es el más rico para la discusión: hay sobreimpulso y oscilación visibles en la gráfica, lo que da material real para el criterio "Discusión y conclusiones" (4 pts).
- Diferencia clave vs. los ejercicios del curso: aquí la incógnita es **$V_o = q/C$** (no la carga), lo que aporta un paso propio de conversión y evita que sea idéntico a las notas.
- Condiciones iniciales: $v_C(0)=0$, $i(0)=0$ (capacitor descargado, interruptor abierto antes de $t=0$) — las mismas hipótesis físicas estándar de la consigna.

**Simulador: GNU Octave** (no LTSPICE). Razones: ya hay nota de soporte [[S16-5 Tema 02 - Programa Octave|Programa Octave]] del curso, no requiere instalación con licencia/aprendizaje de esquemáticos, y permite en el **mismo script** resolver numéricamente la EDO (`lsode`/`ode45`), superponer la curva teórica y calcular el error punto a punto — que es justo lo que pide la rúbrica. LTSPICE queda como plan B solo si el docente lo exigiera explícitamente.

## 3. Desglose: Etapas → Tareas → Subtareas

### Etapa A — Cierre de decisiones y fuentes
- **A1. Confirmar decisiones del hub** (bloqueante, ver [[Trabajo Final - SyT MOC|hub]]):
  - A1.1 Confirmar que el proyecto elegido es el **Proyecto 2 (Laplace)** y no el 1.
  - A1.2 Confirmar modalidad **individual o grupal** (afecta el video: todos los integrantes deben aparecer).
  - A1.3 Verificar si el **APF ya fue entregado hoy**; si no, activar la ruta de emergencia (§4).
- **A2. Bibliografía APA** (alimenta criterio 6, 3 pts) — según [[01 - Busqueda de fuentes (APA)]]:
  - A2.1 Buscar 4–6 fuentes candidatas: libro de texto de EDO/Laplace (p. ej. Zill; Spiegel), libro de circuitos (p. ej. Alexander & Sadiku; Hayt), documentación oficial de GNU Octave, y el material del curso. **Verificar cada fuente antes de citarla — no inventar citas.**
  - A2.2 Redactar las entradas APA 7 y decidir qué cita respalda cada sección (definición de Laplace, propiedades, modelo del circuito, simulador).

### Etapa B — Desarrollo analítico (criterio 4: Dominio teórico, 3 pts)
Trabajar en `03 - Desarrollo analitico` de esta carpeta, siguiendo el método de [[S14-1 Tema 01 - Transformadas de Laplace|S14-1]]:
- **B1. Planteamiento:** malla de Kirchhoff → $L\,i' + R\,i + v_C = E$, con $i = C\,v_C'$ → EDO de 2.º orden en $v_C$: $v_C'' + 6 v_C' + 25 v_C = 2500$, $v_C(0)=0$, $v_C'(0)=0$. Dibujar el circuito (figura numerada, hecha propia para no depender de citas de imagen ajenas).
- **B2. Transformada:** aplicar $\mathcal{L}$ con condiciones iniciales, despejar $V_o(s) = \dfrac{2500}{s\,(s^2+6s+25)}$.
- **B3. Fracciones parciales:** $\frac{A}{s} + \frac{Bs+C}{s^2+6s+25}$, completar cuadrados $(s+3)^2+16$.
- **B4. Antitransformada:** obtener $V_o(t)$ cerrado; verificar límites físicos ($V_o(0)=0$, $V_o(\infty)=100$ V) como autocomprobación.
- **B5. Gráfica teórica:** tabular/graficar $V_o(t)$ en $t \in [0, 2.5]$ s (≈ 5 constantes de tiempo del término $e^{-3t}$).
- **B6. Análisis teórico:** identificar régimen subamortiguado, sobreimpulso, frecuencia amortiguada ($\omega_d = 4$ rad/s), tiempo de establecimiento — la rúbrica pide **analizar** los resultados, no solo mostrarlos.

### Etapa C — Simulación en Octave (criterio 3: Dominio de simulación, 3 pts)
Trabajar en `04 - Simulacion`, apoyado en [[S16-5 Tema 02 - Programa Octave|S16-5]]:
- **C1. Script numérico:** resolver la EDO del circuito con `lsode`/`ode45` (sin usar la solución cerrada — debe ser una vía independiente para que la comparación tenga sentido).
- **C2. Gráfica simulada** de $V_o(t)$ con títulos, ejes etiquetados (V, s) y leyenda.
- **C3. Comparación:** superponer curva teórica y simulada en una misma figura.
- **C4. Error:** vector de error punto a punto $|v_{teo} - v_{sim}|$, error relativo porcentual y RMSE; tabla de error en 8–10 instantes representativos + gráfica del error. Comentar por qué el error es pequeño (precisión del integrador) — insumo directo del criterio 5.
- **C5. Guardar** el script `.m` y exportar las figuras en PNG a `attachments/`.

### Etapa D — Documento PDF (criterios 1, 2, 6)
Seguir el esqueleto de [[05 - Documento final (esqueleto)]]:
- **D1. Introducción (2 pts):** prosa con antecedentes generales (uso de Laplace en ingeniería) y específicos (análisis de transitorios en circuitos), y objetivo principal.
- **D2. Marco teórico (2 pts):** definición y propiedades usadas de la Transformada de Laplace (linealidad, derivadas, traslación), modelo del circuito RLC, definición del simulador (Octave) y las ecuaciones que se aplicarán. Todo con citas APA en texto.
- **D3. Cuerpo:** volcar Etapas B y C con figuras/tablas **numeradas y con definición breve**, listadas en el índice.
- **D4. Discusión y conclusiones (4 pts):** discusión simulado vs. teórico **incluyendo el error**, conclusión de resultados simulados, conclusión de resultados teóricos y conclusión de la discusión — la rúbrica desglosa exactamente esos 4 sub-ítems.
- **D5. Referencias (3 pts):** lista APA 7; verificar que **cada imagen** tenga su cita o "elaboración propia".
- **D6. Formato y export:** Arial 12, interlineado 1.5, índice con tablas y figuras, 10–20 páginas; exportar con [[exportar-docx|md_to_docx.py]] → revisar en Word → PDF.

### Etapa E — Video ≤ 5 min (criterio 7, 3 pts)
Según [[06 - Guion del video]]:
- **E1. Guion** con los 5 bloques obligatorios: título, objetivos, metodología, análisis de resultados, conclusiones (~55 s por bloque).
- **E2. Grabación** (pantalla con las gráficas + cámara; **todos los integrantes** hablan si es grupal).
- **E3. Subida** a Drive/YouTube (no adjuntar el archivo pesado) y verificación del enlace en incógnito.

### Etapa F — Entrega PROY
- **F1.** Checklist final (§8) completo.
- **F2.** Subir PDF + enlace del video a Canvas **antes del mar 21 jul, 11:59 p.m.** — hay **1 solo intento**: subir solo cuando todo esté verificado, y no el último minuto.

## 4. Cronograma (fechas reales)

> [!warning] Ruta de emergencia APF — solo si NO se entregó aún
> Si el APF sigue pendiente **hoy lun 13 jul**, priorizar en el día: B1–B5 (analítico completo), C1–C3 (simulación con gráfica comparada), D1–D2 (introducción + marco teórico breves) y armar un PDF de ≥10 pág. El APF **no exige** discusión del error ni video, así que es alcanzable en una sesión larga. Entregar antes de las 11:59 p.m.

| Fecha | Sem | Tareas | Hito |
| ----- | --- | ------ | ---- |
| **Lun 13 jul** | 17 | A1 (decisiones) · ruta de emergencia APF si aplica | **APF vence 11:59 p.m.** |
| Mar 14 jul | 17 | A2 (fuentes APA) · B1–B3 | Circuito validado y $V_o(s)$ listo |
| Mié 15 jul | 17 | B4–B6 (antitransformada, gráfica, análisis) | Teoría cerrada |
| Jue 16 jul | 17 | C1–C3 (script Octave + comparación) | Simulación cerrada |
| Vie 17 jul | 17 | C4–C5 (error) · D1–D2 | Error cuantificado |
| Sáb 18 jul | 17 | D3–D5 (cuerpo, discusión, referencias) | Borrador completo del PDF |
| Dom 19 jul | 17 | D6 (formato/export) · E1 (guion) | PDF v1 + guion listos |
| **Lun 20 jul** | 18 | E2–E3 (grabar y subir video) · revisión cruzada del PDF contra rúbrica | PROY abre en Canvas |
| **Mar 21 jul** | 18 | F1–F2: checklist y **entrega** (mañana/tarde, no de noche) | **PROY vence 11:59 p.m.** |

**Qué quedó para el APF vs. qué añade el PROY:** el APF cubre introducción + marco teórico + desarrollo analítico + simulación (Etapas B, C1–C3, D1–D2). El PROY añade el **error cuantificado (C4)**, la **discusión y conclusiones (D4)** y el **video (E)** — coherente con [[S18-98 PROY Indicaciones]].

## 5. Entregables y definición de terminado (DoD)

| Etapa | Entregable | Definición de terminado |
| ----- | ---------- | ----------------------- |
| A | Decisiones cerradas + lista de fuentes | Modalidad y proyecto confirmados en el [[Trabajo Final - SyT MOC\|hub]]; 4–6 referencias APA verificadas (existen y son consultables) |
| B | Nota `03 - Desarrollo analitico` | $V_o(t)$ cerrado, verificado con $V_o(0)=0$ y $V_o(\infty)=E$; gráfica generada; análisis del régimen escrito |
| C | Script `.m` + figuras PNG | Script corre sin errores desde cero; figura comparativa teoría/simulación; tabla y gráfica de error; RMSE calculado |
| D | PDF final | 10–20 pág, Arial 12, interlineado 1.5; índice con tablas y figuras numeradas; todas las imágenes citadas; referencias APA; pasa una lectura contra los 7 criterios de la rúbrica |
| E | Video en Drive/YouTube | ≤ 5:00 min; contiene los 5 bloques exigidos; enlace accesible en ventana de incógnito; todos los integrantes aparecen |
| F | Entrega en Canvas | PDF + enlace subidos, confirmación de envío guardada (captura) |

## 6. Mapa Tarea → criterio de rúbrica → puntos (20 pts)

| Criterio | pts | Tareas que lo producen |
| -------- | --- | ---------------------- |
| 1. Introducción | 2 | D1 |
| 2. Marco teórico | 2 | A2 + D2 |
| 3. Dominio de simulación | 3 | C1–C3 (+ análisis en D3) |
| 4. Dominio teórico | 3 | B1–B6 (+ presentación en D3) |
| 5. Discusión y conclusiones con error | 4 | C4 + D4 |
| 6. Referencias APA | 3 | A2 + D5 |
| 7. Video | 3 | E1–E3 |
| **Total** | **20** | — |

## 7. Recursos y materiales

- **Teoría del vault:** [[S14-1 Tema 01 - Transformadas de Laplace]] (método general), [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente]] y [[S14-4 Tema 01 - Ejercicio 3 - Circuito RLC II]] (patrón de desarrollo RLC), [[S16-5 Tema 02 - Programa Octave]] (base del script).
- **Consignas:** [[S18-98 PROY Indicaciones]] (rúbrica 20 pts, erratas del portal ya documentadas), [[S16-98 APF Indicaciones]].
- **Simulador:** GNU Octave — verificar instalación local con `octave --version`; si falta, instalar vía `winget install GNU.Octave` (con autorización). No se requiere LTSPICE.
- **Bibliografía candidata a verificar** (no citar sin confirmar edición/año): Zill, *Ecuaciones diferenciales con aplicaciones de modelado*; Spiegel, *Transformadas de Laplace* (Schaum); Alexander & Sadiku, *Fundamentos de circuitos eléctricos*; Eaton et al., documentación oficial de GNU Octave.
- **Export:** [[exportar-docx|utils/md_to_docx.py]] (Pandoc + APA 7 + LaTeX) para generar el Word/PDF.

## 8. Riesgos y mitigaciones

| Riesgo | Impacto | Mitigación |
| ------ | ------- | ---------- |
| APF no entregado hoy | Pierde 15% directo | Ruta de emergencia del §4, prioridad absoluta hoy |
| Condiciones iniciales mal planteadas (p. ej. olvidar $v_C'(0) = i(0)/C$) | Solución teórica errada → criterios 4 y 5 caen | Autocomprobación B4: verificar $V_o(0)$ y $V_o(\infty)$ contra la física del circuito |
| Desajuste teórico vs. simulado (EDO distinta en el script) | El "error" sale enorme y la discusión no cierra | C1 usa la **misma EDO** de B1; si el error > 1% investigar antes de redactar |
| Confusión carga $q(t)$ vs. voltaje $V_o(t)$ (los ejercicios del curso resuelven $q$) | Entregar la variable equivocada | B1 plantea la EDO directamente en $v_C$; revisar unidades (V) en todas las gráficas |
| Erratas de la consigna del portal (etiquetas de proyectos cruzadas) | Desarrollar el entregable del proyecto equivocado | Ya documentado en [[S18-98 PROY Indicaciones]]: Proyecto 2 = **Laplace** |
| PDF fuera de rango (<10 o >20 pág) tras exportar | Penalización de formato | Revisar conteo tras D6 con margen (apuntar a 14–16 pág) |
| Video > 5 min o enlace con permisos cerrados | Criterio 7 (3 pts) en riesgo | Guion cronometrado en E1; probar el enlace en incógnito (E3) |
| Un solo intento de entrega en Canvas | Envío incompleto irrecuperable | F1 checklist completo antes de subir; entregar el 21 con horas de margen |

## 9. Checklist final de entrega

- [ ] PDF entre 10 y 20 páginas, Arial 12, interlineado 1.5
- [ ] Índice incluye lista de tablas y figuras, todas numeradas y con definición breve
- [ ] Circuito dibujado (figura propia) con valores R, L, C, E rotulados
- [ ] Desarrollo teórico completo: EDO → $V_o(s)$ → fracciones parciales → $V_o(t)$ → gráfica
- [ ] Simulación Octave: código visible en el doc + gráfica simulada + comparación superpuesta
- [ ] Error mostrado: tabla + gráfica + RMSE, discutido en la sección de discusión
- [ ] Conclusiones alineadas a los objetivos, con datos numéricos obtenidos
- [ ] Citas APA en texto **y en cada imagen**; lista de referencias APA verificadas (ninguna inventada)
- [ ] Video ≤ 5 min con título, objetivos, metodología, análisis y conclusiones; todos los integrantes aparecen
- [ ] Enlace del video (Drive/YouTube) probado en incógnito y pegado en el documento/entrega
- [ ] PDF + enlace subidos a Canvas antes del **mar 21 jul, 11:59 p.m.** (1 solo intento) y captura de confirmación guardada
