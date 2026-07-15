---
title: PC2 - Práctica Calificada 2 (AC-S09) - Semana 09
curso: "[[Motores MOC]]"
unidad: 2
semana: 9
orden: 99
tipo: evaluacion
subtipo: pc
tags:
  - curso/motores
  - tipo/evaluacion
  - subtipo/pc
  - tema/transformador-real
  - tema/transformador-trifasico
  - tema/ensayos
  - tema/circuito-equivalente
date: 2026-05-22
---

## Datos

| Campo | Valor |
| ----- | ----- |
| Nombre | 🔴 (AC-S09) Semana 09: Examen - Práctica Calificada 2 (PC2) |
| Tipo | **Evaluación calificada** — Práctica Calificada 2 (segunda de 3) |
| Modalidad | Individual, plataforma virtual |
| Duración | **90 minutos** (1 intento) |
| Total | **20 puntos** (4 + 4 + 8 + 4) |
| Ventana | Viernes 22 de mayo — Domingo 24 de mayo de 2026 a las 11:59 p.m. |
| Peso en el ciclo | **10 %** |
| Total de preguntas (portal) | 1 grupo con sub-preguntas |
| Estado al momento de extracción | **POR ENTREGAR** — 34 min restantes hasta el cierre |

## Indicaciones (resumen)

Ver detalle completo en [[S09-98 Indicaciones - Práctica Calificada 2]].

**Estructura** (4 preguntas + 1 caso de desarrollo):

| Caso | Tema | Puntos |
| ---- | ---- | ------ |
| **Caso 1 — preguntas cerradas** | Circuito equivalente (cobre, núcleo, reducción al primario) | 4 |
| **Caso 1 — preguntas cerradas** | Ensayos básicos (vacío, cortocircuito, interpretación) | 4 |
| **Caso de desarrollo** (manuscrito + foto) | Transformador en carga: caída de tensión, pérdidas, eficiencia, índice de carga, diagrama fasorial | **8** |
| **Caso 2 — preguntas cerradas** | Transformadores trifásicos (tensiones/intensidades, S, η, tipo de conexión) | 4 |

> [!warning] Caso de desarrollo manuscrito
> La pregunta de desarrollo debe responderse **manuscrita** y adjuntarse como imagen. Es la pregunta de mayor peso (8 pts).

## Antes de iniciar — checklist mental

- [ ] Calculadora científica lista.
- [ ] Papel y lapicero/lápiz para el caso de desarrollo.
- [ ] Celular o cámara para fotografiar la respuesta manuscrita.
- [ ] Conexión a internet estable.
- [ ] Repasar fórmulas clave (ver [[Formulario - Motores Eléctricos Estáticos y Rotativos|formulario]] §17 a §23).

## Fórmulas más probables (de la semana 7 a la 9)

### Relaciones del trifásico
$$S = \sqrt{3} \cdot V_L \cdot I_L \hspace{0.5cm};\hspace{0.5cm} V_L = \sqrt{3}\,V_\phi \text{ (Y)} \hspace{0.5cm};\hspace{0.5cm} I_L = \sqrt{3}\,I_\phi \text{ (Δ)}$$

### Parámetros del trafo real
$$Z_{cc} = \frac{V_{cc}}{I_{cc}} \hspace{0.5cm};\hspace{0.5cm} R_{cc} = \frac{P_{cc}}{I_{cc}^{\,2}} \hspace{0.5cm};\hspace{0.5cm} X_{cc} = \sqrt{Z_{cc}^{\,2} - R_{cc}^{\,2}}$$

$$R_{Fe} = \frac{V_0^{\,2}}{P_0} \hspace{0.5cm};\hspace{0.5cm} \text{o usando admitancia: }\mathbf{Y}_E = \frac{I_0}{V_0}\angle\!-\!\cos^{-1}\!\frac{P_0}{V_0 I_0}$$

### Caída de tensión y eficiencia
$$RV = \frac{V_P/a - V_S}{V_S} \cdot 100\,\% \hspace{0.5cm};\hspace{0.5cm} \eta = \frac{V_S I_S \cos\theta}{V_S I_S \cos\theta + P_{Cu} + P_{Fe}} \cdot 100\,\%$$

### Índice de carga
$$C = \frac{I_S}{I_{Sn}} \hspace{0.5cm}\text{(0 a 1, expresa el porcentaje de plena carga)}$$

Las pérdidas en el cobre escalan con $C^2$:
$$P_{Cu} = C^2 \cdot P_{Cu,n}$$

### Reflexión de impedancias
$$\mathbf{Z}'_L = a^2 \cdot \mathbf{Z}_L$$

### Relación de transformación trifásica por conexión
| Conexión | $V_{LP}/V_{LS}$ |
| -------- | ---------------- |
| Y–Y | $a$ |
| Δ–Δ | $a$ |
| Y–Δ | $\sqrt{3} \cdot a$ |
| Δ–Y | $a/\sqrt{3}$ |

## Notas relacionadas (material de estudio)

- Teoría monofásico real: [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real]] · [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real]] · [[S08-1 Tema 01 - Determinación de los parámetros del transformador]] · [[S08-2 Tema 02 - Eficiencia y regulación del transformador real]] · [[S08-4 Tema 03 - Diagrama fasorial]]
- Teoría trifásico: [[S09-1 Tema 01 - El transformador trifásico]] · [[S09-3 Tema 02 - Circuito equivalente aproximado del transformador trifásico]]
- Ejercicios resueltos: [[S07-2 Ejercicio resuelto - Circuito equivalente del transformador real (Video)]] · [[S07-4 Ejercicio resuelto - Ensayos del transformador (Video)]] · [[S08-3 Ejercicio resuelto - Eficiencia y regulación (Video)]] · [[S09-2 Ejercicio resuelto - Transformador trifásico (Video)]] · [[S09-4 Ejercicio resuelto - Circuito equivalente trifásico (Video)]]
- Indicaciones y rúbrica: [[S09-98 Indicaciones - Práctica Calificada 2]]

## Después de la evaluación

> [!info] Espacio para enunciados y desarrollo
> Una vez rendida la PC2, copia o transcribe aquí los **enunciados específicos** y el **desarrollo de cada pregunta** (en particular el caso de desarrollo manuscrito). Esto te servirá para preparar la PC3 (semana 14) y el EXFN (semana 18) — los temas se reciclan.
> 
> Estructura sugerida:
> 1. **Caso 1 — Circuito equivalente** (4 preguntas)
>    - Enunciados, alternativas, respuesta elegida + verificación de las otras alternativas (regla de evaluaciones).
> 2. **Caso 1 — Ensayos** (4 preguntas)
> 3. **Caso de desarrollo** (transformador en carga)
>    - Datos, esquema, desarrollo paso a paso, diagrama fasorial.
> 4. **Caso 2 — Trifásico** (4 preguntas)

(pendiente de completar después de rendir el examen)
