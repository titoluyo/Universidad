---
title: "Cursos del ciclo 2026-1"
ciclo: 2026-1
tipo: ciclo
tags:
  - tipo/ciclo
  - ciclo/2026-1
date: 2026-03-23
---

# Cursos del ciclo 2026-1

Hub de datos del ciclo activo. Mapeo curso del portal UTP → carpeta del vault. Los UUIDs son estables durante el ciclo. Al cambiar de ciclo, regenerar este archivo navegando a la página de cursos del portal.

## Mapeo curso → carpeta

| Curso (portal)                            | Sigla | Modalidad    | Docente                       | Carpeta vault         | Course UUID                            | Section UUID                           |
| ----------------------------------------- | ----- | ------------ | ----------------------------- | --------------------- | -------------------------------------- | -------------------------------------- |
| Circuitos Electrónicos Amplificadores     | 29579 | Presencial   | jorge luis robles bokun       | [[Amplificadores MOC\|Amplificadores]]      | `08eb7f8d-ab62-53df-9b46-c0ca85f1f263` | `55733e4b-ebe4-5b86-8284-d0afbacba5cd` |
| Controlador Lógico Programable Plc        | 25286 | Presencial   | jorge luis guerrero cardenas  | [[PLC MOC\|PLC]]                            | `2bcfdc80-6c82-53f7-b910-4b4dd5ebaba6` | `8e09f862-b5fa-5106-8fdc-c7f9b2850c99` |
| Maquinas Eléctricas Estáticas y Rotativas | 14199 | Virtual 24/7 | charlton harley pretel diaz   | [[Motores MOC\|MaquinasElectricas]]         | `40ee9986-a006-5cb9-a550-2e82d236051d` | `70765508-9fb9-5029-aa08-d47e3b6ff0ff` |
| Series y Transformadas                    | 14081 | Virtual 24/7 | jose fernando torres diaz     | [[SeriesTransformadas MOC\|SeriesTransformadas]] | `0b1407f5-d982-5ee2-b893-1a1e0f3f02e7` | `a9dcc407-c04b-5d30-b7c4-fb698f891128` |

URL base por curso: `https://class.utp.edu.pe/student/courses/<course_uuid>/section/<section_uuid>/learnv2`

## Calendario

- Inicio del ciclo: lunes **23 de marzo de 2026** (Semana 01).
- Duración: **18 semanas** (cierra domingo 26 de julio de 2026).
- Convención Perú: las semanas empiezan **lunes** y terminan **domingo**.
- Para inferir la semana actual: `python utils/semana_actual.py [YYYY-MM-DD]`.

## Patrones de anuncios por docente

| Docente            | Curso         | Frecuencia              | Formato                                                                      |
| ------------------ | ------------- | ----------------------- | ---------------------------------------------------------------------------- |
| J. Robles Bokun    | Amplificadores | 1/semana, lunes 6:00 AM | Saludo template (texto, sin imágenes)                                        |
| J. Guerrero Cárdenas | PLC          | 1/semana, lunes 6:00 AM | Texto con temario de la semana                                               |
| Ch. Pretel Díaz    | Maquinas      | 2-3/semana, lun y jue 12:00 AM | 2 diapositivas-anuncio "BIENVENIDO(A) A LA SEMANA N" + comunicados puntuales |
| J. F. Torres Díaz  | SyT           | 3-5/semana, lun y vie 6:00 AM | 2 anuncios-tarjeta "Bienvenida"/"Cierre" + felicitaciones, invitaciones, indicaciones de PA |

## Cursos a IGNORAR en el portal

- `RUTA LABORAL - LIMA CENTRO 5` (40030, 2026-1)
- `Ruta Laboral` (10025, ciclo PRED-MARZO25)
- `English Discoveries Placement Test` (Período Predeterminado)

## Sigla de los códigos de Sílabo (para construir URL del PDF)

URL del PDF del Sílabo: `https://ms-utp-prd-silbiaback-cd.s3.amazonaws.com/pdfs/approved/complete/<ciclo>/<modalidad>/<codigo>_<NombreCursoSinEspacios>.pdf`

Códigos vistos en este ciclo:
- Amplificadores: `100000I21N`
- PLC: `100000I39M`

## Cómo actualizar este archivo al iniciar un nuevo ciclo

1. Navegar a `https://class.utp.edu.pe/student/courses` autenticado.
2. Para cada curso del nuevo ciclo: extraer `course_uuid` y `section_uuid` del href del enlace al curso.
3. Capturar nombre exacto del portal, sigla numérica, modalidad y docente.
4. Reemplazar la tabla "Mapeo curso → carpeta" arriba.
5. Actualizar la fecha de inicio en "Calendario" y agregar la entrada al diccionario `INICIOS_CICLO` de [utils/semana_actual.py](../../utils/semana_actual.py).
6. Renombrar el archivo y la carpeta del ciclo (e.g. `cursos/2026-2/Cursos.md`).
7. Resetear "Patrones de anuncios por docente" — los docentes pueden cambiar.
