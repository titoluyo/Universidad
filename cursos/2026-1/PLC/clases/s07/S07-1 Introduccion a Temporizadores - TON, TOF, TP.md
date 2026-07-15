---
title: "Introducción a Temporizadores: TON, TOF, TP"
curso: "[[PLC MOC]]"
unidad: 2
semana: 7
orden: 1
tipo: clase
tags:
  - curso/plc
  - tipo/clase
  - tema/temporizadores
  - tema/ton
  - tema/tof
  - tema/tp
  - tema/iec-61131-3
date: 2026-05-04
---

## Concepto: ¿qué es un temporizador en un PLC?

Un **temporizador** (timer) es un bloque funcional que introduce un retardo controlado entre un evento de entrada y la activación o desactivación de una salida. Reemplaza a los antiguos relés temporizados electromecánicos y es uno de los bloques más usados en automatización industrial: arranque escalonado de motores, ventilación residual, generación de pulsos para electroválvulas, vigilancia de tiempos de proceso (timeouts), etc.

La norma **IEC 61131-3** (estándar internacional para lenguajes de programación de PLCs) define **tres temporizadores estándar**: `TON`, `TOF` y `TP`. Estos tres bloques están disponibles —con la misma semántica— en CODESYS, Siemens TIA Portal (S7-1200/1500), Schneider Unity, Beckhoff TwinCAT, y prácticamente cualquier PLC moderno.

> [!info] Nota histórica
> Antes de IEC 61131-3 cada fabricante usaba su propia nomenclatura (Allen-Bradley: `TON`/`TOF`/`RTO`; Siemens S5/S7-300: `S_ODT`/`S_OFFDT`/`S_PULSE`/`SD`/`SE`/`SF`/`SS`). La estandarización en `TON`/`TOF`/`TP` permite portabilidad entre marcas.

## Parámetros comunes (IEC 61131-3)

Los tres bloques comparten la misma firma de E/S:

| Parámetro | Dirección | Tipo de dato | Descripción                                                |
| --------- | --------- | ------------ | ---------------------------------------------------------- |
| `IN`      | Entrada   | `BOOL`       | Señal lógica que dispara/controla el temporizador          |
| `PT`      | Entrada   | `TIME`       | **Preset Time** — duración programada del retardo o pulso  |
| `Q`       | Salida    | `BOOL`       | Salida lógica del temporizador (su significado depende del tipo) |
| `ET`      | Salida    | `TIME`       | **Elapsed Time** — tiempo transcurrido desde el disparo    |

Donde:

- $\text{IN}$ = entrada de control (señal de disparo).
- $\text{PT}$ = tiempo preestablecido, en formato `T#<duración>`. Internamente se almacena como entero de 32 bits en milisegundos.
- $\text{Q}$ = salida booleana; su transición depende del tipo de temporizador.
- $\text{ET}$ = tiempo acumulado; siempre cumple $0 \leq \text{ET} \leq \text{PT}$.

> [!example] Sintaxis del literal `TIME`
> En IEC 61131-3 se escribe con prefijo `T#` y unidades concatenadas sin espacios:
> - `T#5s` → 5 segundos
> - `T#500ms` → 500 milisegundos
> - `T#1h30m15s` → 1 hora 30 minutos 15 segundos
> - `T#2d4h` → 2 días 4 horas

## TON — Timer On Delay (retardo a la conexión)

### Comportamiento

`TON` **retarda la activación** de su salida `Q` respecto al flanco de subida de `IN`. Es decir: la señal `IN` debe permanecer en TRUE de manera **continua** durante al menos `PT` para que `Q` se active.

| Evento en `IN`                              | Acción en `ET`                  | Acción en `Q`             |
| ------------------------------------------- | ------------------------------- | ------------------------- |
| `IN` sube (0→1)                             | `ET` empieza a contar desde 0   | `Q` permanece en 0        |
| `IN` se mantiene en 1 y `ET` alcanza `PT`   | `ET` se congela en `PT`         | `Q` pasa a 1              |
| `IN` baja (1→0) **antes** de cumplir `PT`   | `ET` se resetea a `T#0s`        | `Q` permanece en 0        |
| `IN` baja (1→0) **después** de cumplir `PT` | `ET` se resetea a `T#0s`        | `Q` cae a 0 inmediatamente |

> [!warning] Punto crítico
> Si `IN` se interrumpe aunque sea brevemente antes de cumplir `PT`, el conteo se **reinicia** desde cero. `TON` **no es retentivo**. (Para conteo retentivo —que recuerda lo acumulado tras una interrupción— existe `TONR`, una extensión Siemens/Allen-Bradley fuera del estándar IEC.)

### Diagrama de tiempos

```
        ┌─────────────┐         ┌──┐
IN  ────┘             └─────────┘  └──────
        │             │         │  │
        │◄────PT─────►│         │  │
        │             ┌─────────┘  │
Q   ────────────────┘             └──────
                                  │
        ┌────PT      ┌─PT (reinicia, no llega)
ET  ────┘    \      │   \
              ─0    │    ─0
                    └─0
```

Lectura del diagrama: en el primer pulso de `IN`, este se mantiene lo suficiente y `Q` se activa al cumplir `PT`. En el segundo pulso, `IN` cae antes de `PT`, así que `ET` se resetea y `Q` nunca llega a activarse.

### Casos de uso típicos

- **Anti-rebote / filtrado de señal**: ignorar pulsos cortos de un sensor (e.g., un final de carrera que vibra).
- **Pre-lubricación**: esperar 5 s después del comando de marcha antes de arrancar el motor principal.
- **Confirmación de presencia**: activar un sistema solo si una persona permanece en una zona durante N segundos.
- **Timeout de proceso**: si una válvula no llega a posición en `PT`, disparar alarma.

### Ejemplo en Lenguaje Estructurado (ST)

```pascal
VAR
    Timer1     : TON;
    bArranque  : BOOL;
    bMotor     : BOOL;
END_VAR

Timer1(IN := bArranque, PT := T#5s);
bMotor := Timer1.Q;
```

Si `bArranque` se mantiene en TRUE durante 5 segundos seguidos, `bMotor` se activa.

### Ejemplo en Ladder (LD)

```
                          ┌──────TON──────┐
   bArranque              │               │
─────┤ ├──────────────────┤IN            Q├─────────────( bMotor )
                          │               │
              T#5s ───────┤PT           ET├─── tiempoTranscurrido
                          └───────────────┘
```

## TOF — Timer Off Delay (retardo a la desconexión)

### Comportamiento

`TOF` **retarda la desactivación** de su salida `Q` respecto al flanco de bajada de `IN`. Mientras `IN` esté en 1, `Q` también está en 1 (instantáneamente). Al caer `IN` a 0, `Q` se mantiene en 1 durante `PT` y luego cae.

| Evento en `IN`                                | Acción en `ET`                  | Acción en `Q`        |
| --------------------------------------------- | ------------------------------- | -------------------- |
| `IN` sube (0→1)                               | `ET` se resetea a `T#0s`        | `Q` pasa a 1 inmediato |
| `IN` baja (1→0)                               | `ET` empieza a contar desde 0   | `Q` permanece en 1   |
| `ET` alcanza `PT` con `IN` aún en 0           | `ET` se congela en `PT`         | `Q` cae a 0          |
| `IN` vuelve a 1 **durante** el conteo         | `ET` se resetea a `T#0s`        | `Q` se mantiene en 1 |

> [!tip] Regla mnemotécnica
> `TON`: el **0** del nombre simboliza que la **salida se enciende** después del retardo (delayed ON).  
> `TOF`: la **F** simboliza **OFF** retrasado — la salida se apaga después del retardo.

### Diagrama de tiempos

```
        ┌─────────────────┐
IN  ────┘                 └────────────────────
        │                 │
        ┌─────────────────────────┐
Q   ────┘                         └────────────
                          │       │
                          │◄─PT──►│
                          ┌───────┐
ET  ──────────────────────┘       └────0───────
```

### Casos de uso típicos

- **Ventilación residual**: mantener un ventilador encendido 30 s después de apagar la resistencia/horno para enfriar.
- **Iluminación temporizada**: pasillo que sigue iluminado 1 minuto después de cerrar la puerta.
- **Bomba de drenaje**: continuar bombeando 10 s después de que el sensor de nivel deje de detectar líquido (asegura vaciado completo).
- **Filtrado de señales intermitentes**: tratar como continua una señal con pequeños cortes menores a `PT`.

### Ejemplo en ST

```pascal
VAR
    TOF_Vent   : TOF;
    bHorno     : BOOL;
    bVent      : BOOL;
END_VAR

TOF_Vent(IN := bHorno, PT := T#30s);
bVent := TOF_Vent.Q;
```

`bVent` se activa apenas `bHorno` se enciende y se mantiene 30 s tras apagarlo.

## TP — Timer Pulse (generador de pulso)

### Comportamiento

`TP` genera un **pulso de duración fija `PT`** ante el flanco de subida de `IN`. Una vez iniciado el pulso, `Q` permanece en 1 exactamente `PT`, **sin importar qué le pase a `IN` mientras tanto**.

| Evento en `IN`                                | Acción en `ET`                  | Acción en `Q`           |
| --------------------------------------------- | ------------------------------- | ----------------------- |
| `IN` sube (0→1) con `Q` en 0                  | `ET` empieza a contar desde 0   | `Q` pasa a 1            |
| `IN` cambia (sube o baja) **durante** el pulso | sin efecto                      | sin efecto              |
| `ET` alcanza `PT`                             | `ET` se congela en `PT`         | `Q` cae a 0             |
| `IN` está en 0 después del pulso              | `ET` se resetea a `T#0s`        | `Q` permanece en 0      |
| Nuevo flanco de subida en `IN` (con pulso ya terminado) | `ET` reinicia desde 0   | `Q` vuelve a 1 (nuevo pulso) |

> [!warning] No re-triggereable durante el pulso
> A diferencia de un monoestable re-disparable, `TP` **ignora** flancos adicionales de `IN` mientras el pulso está activo. Si necesitas extender el pulso al re-disparar, hay que combinar varios bloques o usar un `TOF` (que sí se re-dispara con cada subida).

### Diagrama de tiempos

```
        ┌──┐           ┌──┐  ┌──┐
IN  ────┘  └───────────┘  └──┘  └────────
        │              │
        ┌──────┐       ┌──────┐
Q   ────┘      └───────┘      └──────────
        │      │       │      │
        │◄─PT─►│       │◄─PT─►│
```

Observa que en el segundo grupo dos pulsos cortos consecutivos de `IN` solo generan **un** pulso de `Q`: el segundo flanco llega durante el pulso activo y es ignorado.

### Casos de uso típicos

- **Activación de electroválvulas / solenoides** durante un tiempo fijo (e.g., dosificación).
- **Pulsos de alarma** (sirena que suena 3 s ante cualquier evento, sin importar duración del evento).
- **Pulso de reset** a otros bloques.
- **Acondicionamiento de pulsador**: convertir un pulsador con duración variable en un pulso normalizado.
- **Generadores de onda cuadrada** (combinando `TP` con `TON` en realimentación).

### Ejemplo en ST

```pascal
VAR
    TP_Sirena  : TP;
    bAlarma    : BOOL;
    bSirena    : BOOL;
END_VAR

TP_Sirena(IN := bAlarma, PT := T#3s);
bSirena := TP_Sirena.Q;
```

Cualquier flanco de subida en `bAlarma` enciende la sirena exactamente 3 s.

## Comparativa rápida

| Característica                  | `TON`                       | `TOF`                       | `TP`                          |
| ------------------------------- | --------------------------- | --------------------------- | ----------------------------- |
| Disparo                         | Flanco subida de `IN`       | Flanco bajada de `IN`       | Flanco subida de `IN`         |
| `Q` activo cuando…              | `IN`=1 y `ET`=`PT`          | `IN`=1, **o** contando       | Pulso en curso (`ET`<`PT`)    |
| Duración de `Q` activo          | Mientras `IN`=1 tras retardo | `PT` después de caer `IN`   | Exactamente `PT`              |
| ¿Re-disparable durante el conteo? | Reset (no)                | Reset del conteo (sí)        | No (ignora)                   |
| Caso clásico                    | Arranque retardado          | Apagado diferido             | Pulso de duración fija        |

## Notas de implementación

### En Siemens TIA Portal (S7-1200/1500)

- Los bloques se llaman **IEC Timers**: `TON`, `TOF`, `TP` (y la extensión `TONR` para conteo retentivo).
- Cada instancia requiere un **DB de instancia** (Data Block) o puede declararse `STATIC` dentro de un FB.
- La entrada `PT` acepta literales `T#5s` o variables tipo `TIME` (`DInt` en ms internamente).
- Resolución típica: 1 ms.
- En SCL: `"miTimer".TON(IN := bSensor, PT := T#5s, Q => bResultado, ET => tElapsed);`

### En CODESYS / Beckhoff TwinCAT

- Pertenecen a la librería estándar (`Standard.lib` / `Tc2_Standard`).
- Se declaran como instancia de FB y se invocan ciclo a ciclo.
- Misma semántica IEC 61131-3.

### En Allen-Bradley (Studio 5000)

- La nomenclatura tradicional usa `TON` (idéntico al IEC), `TOF` (idéntico al IEC) y `RTO` (Retentive Timer On — equivale a `TONR`, no a `TP`).
- Para `TP` se utiliza la instrucción `TONR` configurada apropiadamente o una combinación de bloques.

> [!important] Buenas prácticas
> 1. **Nombrar las instancias** describiendo su función, no su tipo: `TON_PreLubMotor` mejor que `T1`.
> 2. **Documentar el `PT`** con comentario indicando el porqué del valor (basado en hoja de datos del actuador, requisito de seguridad, etc.).
> 3. **Cuidado con timers en bucles condicionales**: si el bloque deja de ejecutarse en un ciclo, el conteo se congela. Mejor invocarlos siempre y controlar con `IN`.
> 4. **Para timeouts críticos** (seguridad, watchdog), preferir `TON` con verificación posterior de `Q` antes de actuar.

## Bibliografía

- International Electrotechnical Commission. (2013). *IEC 61131-3:2013 — Programmable controllers — Part 3: Programming languages* (3.ª ed.). IEC. (Tablas 46.2a, 46.3a, 46.4a — especificación formal de `TON`, `TOF`, `TP`.)
- Siemens AG. (2026). *SIMATIC S7-1200/1500 — Timer instructions (IEC timers)*. TIA Portal Information System. https://docs.tia.siemens.cloud/r/simatic_s7_1200_manual_collection_eses_20/basic-instructions/timer-operations/timer-instructions-iec-timers
- Fernhill Software. (s.f.). *On Delay Timer (TON) — IEC 61131-3 Function Block*. https://www.fernhillsoftware.com/help/iec-61131/common-elements/standard-function-blocks/on-delay-timer.html
- Fernhill Software. (s.f.). *Off Delay Timer (TOF) — IEC 61131-3 Function Block*. https://www.fernhillsoftware.com/help/iec-61131/common-elements/standard-function-blocks/off-delay-timer.html
- Fernhill Software. (s.f.). *Pulse Timer (TP) — IEC 61131-3 Function Block*. https://www.fernhillsoftware.com/help/iec-61131/common-elements/standard-function-blocks/timer-pulse.html
- Controlbyte. (2026). *Timers in CODESYS: Complete Guide to TON, TOF, and TP Timer Blocks*. https://controlbyte.tech/blog/codesys-timers-ton-tof-tp-guide/
