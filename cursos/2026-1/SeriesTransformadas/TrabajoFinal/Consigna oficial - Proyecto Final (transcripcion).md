---
title: "Consigna oficial — Proyecto Final (transcripción)"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
date: 2026-07-20
aliases:
  - Consigna PROY (transcripcion)
  - Semana 18 - Ind
---

# Consigna para Proyecto Final (Evaluación flexible)

> [!note] Origen
> Transcripción **literal** del PDF oficial `Semana+18+-+Ind.pdf` (`.materiales/2026-1/SeriesTransformadas/s18/`). Se respetan las expresiones y erratas del original (p. ej. "capacitador", "especifico", "Titulo"). Documento par del [[Consigna oficial - Avance Proyecto Final (transcripcion)|APF (semana 16)]]. Resumen operativo y rúbrica mapeada: [[S18-98 PROY Indicaciones]].

> [!danger] Contradicción interna del documento — leer antes de desarrollar
> Este PDF **se contradice a sí mismo**. En la *Indicación general* (§ 2) define **PROYECTO 1 = Serie de Fourier** y **PROYECTO 2 = Laplace/Vo**. Pero en las *Indicaciones específicas* (§ 3) los entregables aparecen **intercambiados**: bajo *"Si eligieron el proyecto 1"* pide $V_o(t)$ con Laplace, y bajo *"Si eligieron el proyecto 2"* pide la serie de Fourier.
> El PDF del APF ([[Consigna oficial - Avance Proyecto Final (transcripcion)|semana 16]]) **no** tiene ese cruce: ahí proyecto 1 → Fourier y proyecto 2 → Laplace, coherente con la indicación general de ambos documentos. La conclusión es que el cruce del § 3 de la semana 18 es un **error de copiado del profesor**.
> **Ninguna lectura pide ambas transformadas:** cada viñeta lista un documento autocontenido (Introducción, Marco teórico, **una** línea analítica, Referencias). La rúbrica lo confirma — todos los criterios dicen "Laplace **o** Serie de Fourier". Ver [[#Nota sobre el cruce de etiquetas]].

## 1. Logro a evaluar

Al finalizar la unidad, el estudiante resuelve ejercicios de aplicación mediante las transformadas.

## 2. Indicación general

En la empresa de Electronics S.A. se ha presentado dos situaciones importantes:

- **PROYECTO 1:** La señal de onda que se desea para una aplicación especifica debe ser una señal senoidal rectificada cuadrática, lo cual han visto necesario utilizar la teoría de Serie de Fourier para realizar el análisis y para buscar la aproximación a la señal requerida realizaran un programa en Octave.
- **PROYECTO 2:** Necesitan determinar el voltaje de un capacitador para un circuito especifico, sin embargo, han visto necesario usar un programa para realizar la simulación y al mismo tiempo usar la Teoría de las Transformadas de Laplace.

La empresa optó por aplicar estas dos Técnicas, ya que son muy eficientes y económicas. Por lo tanto, como parte del personal capacitado para llevar a cabo estas acciones, deberán **escoger uno de los casos** para desarrollar un proyecto, que luego explicarán a través de un video.

## 3. Indicaciones específicas

- El documento debe presentar citaciones bibliográficas en el texto como en las imágenes utilizadas
- El documento deberá utilizar la fuente Arial, tamaño 12 y un interlineado de 1.5.
- La tablas y figuras utilizadas deben estar enumeradas con una breve definición y colocadas en el índice.
- Además, se debe entregar en formato PDF a través de la plataforma virtual,
- La extensión del proyecto deberá ser de un mínimo de 10 páginas y un máximo de 20 páginas.
- El video presentado no debe exceder los 5 minutos, debe subirlo en un drive o YouTube, para evitar perdida de información.
- Se enviará al Canvas durante en la semana, para su revisión.
- Para este proyecto final, deberás incluir los siguientes aspectos:
	- **Si eligieron el proyecto 1:**
		- Introducción
		- Marco teórico
		- Analíticamente, halla Vo y la gráfica Vo(t) del circuito, aplicando la transformada de Laplace por simulación y por teoría
		- Referencia Bibliográfica
	- **Si eligieron el proyecto 2:**
		- Introducción
		- Marco teórico
		- Analíticamente, encuentra la serie de Fourier para la señal senoidal rectificada de media onda por simulación y por teoría
		- Referencia bibliográfica

Además, **independientemente al proyecto elegido**, se deben tener en cuenta los siguientes puntos:

- Comparación de los datos obtenidos de forma tanto simulada como teórica, **mostrando el error**.
- Desarrollo de conclusiones acordes a los objetivos, indicando los datos obtenidos.
- Un video explicativo en el que debe especificar lo siguiente:
	- Titulo
	- Objetivos
	- Metodología
	- análisis de los resultados
	- Conclusiones
- Todos los integrantes deben aparecer en el video explicando su proyecto.
- El simulador por utilizar será el software GNU-OCTAVE o el simulador LTSPICE.

## 4. Recomendaciones

- Revisa los materiales del curso y la bibliografía que se encuentra en el sílabo.
- Presta atención a tu redacción y ortografía al desarrollar el documento.

## 5. Criterios de evaluación

Revisa la rúbrica de evaluación que se utilizará para evaluar tu desempeño en esta actividad.

---

## Rúbrica de evaluación Proyecto Final

Escala por criterio: **Estándar esperado · En proceso 2 · En proceso 1 · Inicial**.

| Criterio | Estándar esperado | EP2 | EP1 | Inicial |
| -------- | ----------------- | --- | --- | ------- |
| **Introducción** | 2 | 1,5 | 1 | 0,5 |
| **Marco Teórico** | 2 | 1,5 | 1 | 0,5 |
| **Dominio de simulación de la Transformada de Laplace o Serie Fourier** | 3 | 2 | 1 | 0,5 |
| **Dominio Teórico de la Transformada de Laplace o Serie de Fourier** | 3 | 2 | 1 | 0,5 |
| **Discusión y Conclusiones** | 4 | 3 | 2 | 1 |
| **Referencia Bibliográfica** | 3 | 2 | 1 | 0,5 |
| **Dominio del Tema (video)** | 3 | 2 | 1 | 0,5 |
| **Total** | **20** | | | |

### Criterios del estándar esperado (texto literal)

**Introducción (2)** — Desarrolla la introducción con los siguientes criterios:
- Redactado en prosa.
- Antecedentes generales y específicos
- Objetivo principal del proyecto.

**Marco Teórico (2)** — Desarrolla el marco teórico con los siguientes criterios:
- La definición y/o conceptos sobre **Serie de Fourier o Transformada de Laplace**.
- Según el tema presenta las propiedades utilizadas en el proyecto.
- Define el simulador que usará.
- Plantea las ecuaciones aplicadas según el tema del proyecto.

**Dominio de simulación de la Transformada de Laplace o Serie Fourier (3)** — Desarrolla el proyecto utilizando los siguientes criterios:
- Muestra el desarrollo del programa (simulación).
- Presenta los resultados.
- Analiza los resultados obtenidos por el simulador.

**Dominio Teórico de la Transformada de Laplace o Serie de Fourier (3)** — Desarrolla el proyecto utilizando los siguientes criterios:
- Muestra la solución teórica de la **Transformada de Laplace en el circuito o teórica de las Serie de Fourier de la función**.
- Presenta los resultados.
- Analiza los resultados obtenidos de forma teórica.

**Discusión y Conclusiones (4)** — Presenta los siguientes criterios:
- Discusión de los resultados simulados y teóricos, **incluyendo su error**.
- Conclusión de los resultados simulados.
- Conclusión de los resultados teóricos.
- Conclusión de la discusión de los resultados simulados y teóricos con su error.

**Referencia Bibliográfica (3)** — Redacta el proyecto siguiendo los siguientes criterios:
- Cita las referencias en el texto.
- Cita las referencias de las imágenes.
- Presenta las referencias en formato APA.

**Dominio del Tema (video) (3)** — Exposición del tema mediante un video con los siguientes criterios:
- Titulo
- Objetivos
- Metodología
- Análisis de los resultados
- Conclusiones
- Tiempo de exposición 5 minutos

> [!info] Degradación de la escala
> **Discusión y Conclusiones** degrada por número de criterios cubiertos (4 → 3 → 2 → 1 de los 4 sub-ítems). El **video** degrada 6 criterios → 4 → 2 → 1. El resto degrada 3-4 criterios → 2 → 1 → 0.

---

## Nota sobre el cruce de etiquetas

Comparación de las *Indicaciones específicas* de ambos documentos oficiales:

| Documento | "proyecto 1" pide… | "proyecto 2" pide… | ¿Coherente con su § 2? |
| --------- | ------------------ | ------------------ | ---------------------- |
| [[Consigna oficial - Avance Proyecto Final (transcripcion)\|APF — semana 16]] | Serie de Fourier (media onda) | $V_o(t)$ con Laplace | ✅ Sí |
| **PROY — semana 18** (este) | $V_o(t)$ con Laplace | Serie de Fourier (media onda) | ❌ **No — invertido** |

**Lecturas posibles y qué implican:**

1. **Errata de copiado (lectura sostenida).** Las viñetas del § 3 se intercambiaron por error. Proyecto 1 = **Fourier**, como en el § 2 de este mismo PDF, como en todo el APF, y como en el PRONTER del profesor. → El proyecto ya entregado en el APF continúa tal cual.
2. **Lectura literal del § 3.** Habría que desarrollar **Laplace en lugar de Fourier**, descartando por completo el APF entregado — y contradiciendo el § 2 de la propia página anterior.

> [!important] Bajo ninguna lectura se piden las dos transformadas
> Cada viñeta describe un documento **autocontenido** (Introducción → Marco teórico → **una** línea analítica → Referencias), de 10 a 20 páginas. El § 2 dice "escoger **uno** de los casos". La rúbrica tiene **un solo** criterio de simulación y **un solo** criterio teórico, ambos definidos con "**o**". Sumar Laplace a un proyecto de Fourier **no aporta puntos** y arriesga el límite de 20 páginas.

## Delta APF → PROY

Lo que el Proyecto Final añade sobre el avance de la semana 16 (todo del bloque "independientemente al proyecto elegido"):

| Añadido | Criterio de rúbrica | pts |
| ------- | ------------------- | --- |
| Comparación simulado vs. teórico **mostrando el error** | Discusión y Conclusiones | 4 |
| Conclusiones acordes a los objetivos | Discusión y Conclusiones | (mismo) |
| Video explicativo ≤ 5 min | Dominio del Tema (video) | 3 |

Además, la rúbrica **rebalancea** los criterios ya presentes en el APF: Introducción y Marco teórico bajan de 4 a **2** pts cada uno; Dominio de simulación y Dominio teórico bajan de 4 a **3**; Referencias baja de 4 a **3**.

## Enlaces

- Resumen operativo y material de soporte: [[S18-98 PROY Indicaciones]].
- Fechas, intentos y formato de entrega: [[S18-99 PROY sem 18]].
- Consigna del avance: [[Consigna oficial - Avance Proyecto Final (transcripcion)]].
- Espacio de trabajo: [[Trabajo Final - SyT MOC]].
