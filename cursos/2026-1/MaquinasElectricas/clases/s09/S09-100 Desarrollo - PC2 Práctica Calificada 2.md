---
title: "Desarrollo PC2 - Práctica Calificada 2"
curso: "[[Motores MOC]]"
unidad: 2
semana: 9
orden: 100
tipo: evaluacion
subtipo: pc
tags:
  - curso/motores
  - tipo/evaluacion
  - subtipo/pc
  - tema/transformador-real
  - tema/ensayos
  - tema/transformador-trifasico
  - tema/circuito-equivalente
date: 2026-05-24
---

> [!info] Sobre este documento
> Desarrollo de la **PC2 — Práctica Calificada 2** (semana 9). Documento fuente: `attachments/s09_EXAMEN_DE_MAQUINAS_ELECTRICAS_2_SQOPWZ.docx`. Modalidad: subir el PDF resuelto en **Evaluaciones** y **Tareas**.
>
> Notas relacionadas: [[S09-99 Evaluación Semana 09 - PC2 Práctica Calificada 2|Metadatos PC2]] · [[S09-98 Indicaciones - Práctica Calificada 2|Indicaciones y rúbrica]].

## Datos de la evaluación

| Campo               | Valor                                                          |
| ------------------- | -------------------------------------------------------------- |
| Tipo                | Calificada — PC2 (10 % del ciclo)                              |
| Total de preguntas  | 4 (4 + 4 + 4 + 8 = 20 pts)                                    |
| Modalidad           | Subir PDF con desarrollo                                       |
| Trabajo             | Individual                                                     |
| Fecha límite        | Domingo 24 de mayo de 2026 — 23:59                            |

## Indicación del docente (encabezado)

> NOTA: Recuerda que el documento con la solución debe ser subido en **ambas secciones (el mismo documento)**, "Evaluaciones" y "Tareas", en formato **PDF**.

---

## Pregunta 1 — Material magnético para alta frecuencia (4 pts)

### Enunciado

¿Cuál de los siguientes materiales magnéticos se utilizaría si se quisiera fabricar un **transformador de alta frecuencia**?

- a) Ferroxcube
- b) Aceros Amorfos
- c) Núcleos de Ferrita
- d) Níquel-Hierro (Ni-Fe o Permalloy)
- e) Hierro-Silicio (Fe-Si)

### Referencia teórica

Ver [[S06-2 Tema 01 - Materiales magnéticos]] · [[S06-3 Tema 01 - Curvas experimentales de los materiales magnéticos]].

### Desarrollo

(por completar)

### Resultado

$$\boxed{\text{respuesta }}$$

---

## Pregunta 2 — Ensayos para determinar los parámetros del transformador (4 pts)

### Enunciado

¿Cuáles son los **ensayos esenciales** empleados en la práctica para establecer los **parámetros del circuito** de un transformador?

- a) Ensayo de vacío y ensayo de cortocircuito
- b) Ensayo de magnetismo y ensayo de eficiencia
- c) Ensayo de vacío, ensayo de cortocircuito y ensayo de magnetismo
- d) Ensayo de magnetismo y ensayo de cortocircuito
- e) Ensayo de magnetismo, ensayo de eficiencia y ensayo de vacío

### Referencia teórica

Ver [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real]] · [[S08-1 Tema 01 - Determinación de los parámetros del transformador]].

### Desarrollo

(por completar)

### Resultado

$$\boxed{\text{respuesta }}$$

---

## Pregunta 3 — Conexión incorrecta en banco trifásico (4 pts)

### Enunciado

¿Cuál es la opción de **conexión incorrecta** en un banco de un transformador trifásico?

- a) Estrella - Ye
- b) Ye - Delta
- c) Delta - Ye
- d) Ye – Ye – Ye
- e) Delta - Delta

### Referencia teórica

Ver [[S09-1 Tema 01 - El transformador trifásico]] · [[S09-3 Tema 02 - Circuito equivalente aproximado del transformador trifásico]].

### Desarrollo

(por completar)

### Resultado

$$\boxed{\text{respuesta }}$$

---

## Pregunta 4 — Transformador 15 kVA, 2300/230 V (8 pts)

### Enunciado

Se va a probar un transformador de **15 kVA** y **2300 V / 230 V** para determinar los componentes de la **rama de la excitación**, sus **impedancias en serie** y su **regulación de voltaje**. Se obtuvieron los siguientes datos de las pruebas realizadas al transformador:

| PRUEBA EN VACÍO        | PRUEBA EN CORTOCIRCUITO (medido en el primario) |
| ---------------------- | ----------------------------------------------- |
| $V_0 = 230\ \text{V}$  | $V_{cc} = 47\ \text{V}$                         |
| $I_0 = 2{,}1\ \text{A}$ | $I_{cc} = 6\ \text{A}$                          |
| $P_0 = 50\ \text{W}$   | $P_{cc} = 160\ \text{W}$                        |

- **a)** Encontrar el circuito equivalente de este transformador referido al **lado de alto voltaje**.
- **b)** Encontrar el circuito equivalente de este transformador referido al **lado de bajo voltaje**.

> [!note] Observación de la transcripción
> El enunciado del problema menciona la **regulación de voltaje** como uno de los objetivos, pero los sub-ítems literales del documento `.docx` solo piden a) y b) (circuitos equivalentes referidos a AT y BT). Conviene verificar contigo si:
> 1. El examen efectivamente termina aquí, o
> 2. Existen sub-ítems adicionales (c, d, …) en el portal/PDF original que pidan calcular la regulación de voltaje (RV), eficiencia, índice de carga o diagrama fasorial — tal como anticipa la rúbrica de las [[S09-98 Indicaciones - Práctica Calificada 2|indicaciones]] (5 variables del caso de desarrollo).

### Datos clave

- $S_n = 15\ \text{kVA}$
- $V_{1n}/V_{2n} = 2300\ \text{V} / 230\ \text{V}$ → $a = V_{1n}/V_{2n} = 10$
- $I_{1n} = S_n/V_{1n} = 15000/2300 \approx 6{,}52\ \text{A}$
- $I_{2n} = S_n/V_{2n} = 15000/230 \approx 65{,}22\ \text{A}$

**Ensayo en vacío** (alimentado por el lado BT → mide $R_{Fe}$ y $X_\mu$ referidos a BT):
- $V_0 = 230\ \text{V}$, $I_0 = 2{,}1\ \text{A}$, $P_0 = 50\ \text{W}$

**Ensayo en cortocircuito** (alimentado por el lado AT/primario → mide $R_{cc}$ y $X_{cc}$ referidos a AT):
- $V_{cc} = 47\ \text{V}$, $I_{cc} = 6\ \text{A}$, $P_{cc} = 160\ \text{W}$

### Referencia teórica

Ver [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real]] · [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real]] · [[S08-1 Tema 01 - Determinación de los parámetros del transformador]] · [[S08-2 Tema 02 - Eficiencia y regulación del transformador real]] · [[Formulario - Motores Eléctricos Estáticos y Rotativos|Formulario §17–§22]].

### Desarrollo

(por completar)

### Resultado

(por completar)

---

## Resumen de respuestas

| #  | Tema                                | Puntos | Respuesta |
| -- | ----------------------------------- | ------ | --------- |
| 1  | Material magnético alta frecuencia  | 4      |           |
| 2  | Ensayos esenciales del transformador| 4      |           |
| 3  | Conexión incorrecta trifásica       | 4      |           |
| 4  | Transformador 15 kVA — circuitos eq.| 8      |           |
| —  | **Total**                           | **20** |           |

## Material de soporte

- Consigna PDF: [[s09-pc2-indicaciones-rubrica.pdf|Indicaciones y rúbrica de la PC2]]
- Documento de preguntas (origen): `attachments/s09_EXAMEN_DE_MAQUINAS_ELECTRICAS_2_SQOPWZ.docx`
- Teoría: [[S06-2 Tema 01 - Materiales magnéticos]] · [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real]] · [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real]] · [[S08-1 Tema 01 - Determinación de los parámetros del transformador]] · [[S08-2 Tema 02 - Eficiencia y regulación del transformador real]] · [[S09-1 Tema 01 - El transformador trifásico]]
- Ejercicios resueltos: [[S07-4 Ejercicio resuelto - Ensayos del transformador (Video)]] · [[S08-3 Ejercicio resuelto - Eficiencia y regulación (Video)]]
- Formulario: [[Formulario - Motores Eléctricos Estáticos y Rotativos|§17–§22]]
