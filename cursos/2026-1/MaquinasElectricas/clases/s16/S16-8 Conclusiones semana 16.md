---
title: Conclusiones semana 16 - Motores asíncronos de inducción
curso: "[[Motores MOC]]"
unidad: 4
semana: 16
orden: 8
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tipo/resumen
  - tema/motor-de-induccion
  - tema/jaula-de-ardilla
  - tema/circuito-equivalente
  - tema/eficiencia
date: 2026-07-06
---

> [!info] Origen del material
> Infografía estática de cierre del docente: [S16-Conclusiones.pdf](attachments/S16-Conclusiones.pdf).

¡Finalizaste la semana! Revisa las **ideas clave** que cierran la sesión.

## Ideas clave de la semana

> [!summary] 1. Arranque del rotor devanado: resistencia extra
> Los **motores de inducción con rotor devanado** se pueden poner en marcha con **corrientes relativamente bajas** mediante la **inserción de una resistencia extra en el circuito del rotor** en el momento del arranque. Es la ventaja que justifica su mayor costo frente a la jaula de ardilla.
>
> Detalle en [[S16-1 Tema 01 - Principio de funcionamiento de las máquinas asíncronas trifásicas|Tema 01]].

> [!summary] 2. El motor de inducción es un transformador giratorio
> Un motor de inducción es básicamente un **transformador giratorio**: su **circuito equivalente** es similar al de un transformador, **excepto en los efectos de la variación de velocidad**. El estator hace de primario y el rotor de secundario, pero la frecuencia del secundario depende del deslizamiento ($f_r = s\,f_e$), lo que introduce la resistencia dependiente de la carga $R_2/s$.
>
> Desarrollo en [[S16-2 Tema 02 - Circuito equivalente de un motor de inducción|Tema 02]].

> [!summary] 3. Dos tipos de rotor: jaula y devanado
> Hay **dos tipos de rotores** de motores de inducción:
>
> - **Rotor de jaula de ardilla**: una serie de **barras paralelas** alrededor del rotor, conectadas entre sí **en cortocircuito** en cada extremo mediante anillos.
> - **Rotor devanado**: **devanados de rotor completos trifásicos**, cuyas fases se sacan del rotor mediante **anillos de deslizamiento y escobillas**.
>
> Aspectos constructivos en [[S16-1 Tema 01 - Principio de funcionamiento de las máquinas asíncronas trifásicas|Tema 01]].

> [!summary] 4. Eficiencia: salida mecánica sobre entrada eléctrica
> La **eficiencia** del motor de inducción es la relación entre la **potencia de salida mecánica** y la **potencia de entrada eléctrica**. La diferencia entre ambas son las distintas **pérdidas** del motor (cobre del estator, núcleo, cobre del rotor, fricción y rozamiento con el aire, y misceláneas):
>
> $$\eta = \frac{P_{sal}}{P_{ent}} \times 100\ \%$$
>
> Balance completo en [[S16-3 Tema 03 - Potencia y par en los motores de inducción|Tema 03]] y aplicación en el [[S16-4 Ejercicio resuelto - Ecuación de potencia (Video)|ejercicio de la ecuación de potencia]].

> [!summary] 5. Par de salida vs. par inducido
> El **par de salida** de un motor de inducción depende de la **potencia de salida** y de la **velocidad del motor**, mientras que el **par inducido interno** depende de la **potencia del entrehierro** y de la **velocidad síncrona**:
>
> $$\tau_{carga} = \frac{P_{sal}}{\omega_m} \qquad\qquad \tau_{ind} = \frac{P_{EH}}{\omega_{sinc}}$$
>
> Aplicación numérica en el [[S16-5 Ejercicio resuelto - Ecuación de torque (Video)|ejercicio de la ecuación de torque]].

## Conexión con la siguiente semana

Esta semana modeló el **motor de inducción** por dentro (circuito equivalente, potencia y par). La [[S17-0 Introducción - Curvas caracteristicas y maquina sincrona|semana 17]] cierra la **Unidad 4** mirando el comportamiento **externo** de las máquinas: las **curvas características del motor síncrono**, la lectura de la **placa de características** del motor asíncrono y el funcionamiento de la máquina síncrona **como generador**. La semana 18 corresponde únicamente al **Examen Final**.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas eléctricas* (5.ª ed.). McGraw-Hill.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Ideas clave de la semana 16* [Infografía estática]. UTP+class.
