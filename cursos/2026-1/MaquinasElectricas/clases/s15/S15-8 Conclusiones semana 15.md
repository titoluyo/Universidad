---
title: Conclusiones semana 15 - Máquinas de corriente alterna
curso: "[[Motores MOC]]"
unidad: 4
semana: 15
orden: 8
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tipo/resumen
  - tema/campo-magnetico-giratorio
  - tema/velocidad-de-sincronismo
  - tema/deslizamiento
  - tema/maquina-sincrona
date: 2026-06-29
---

> [!info] Origen del material
> Guion del video de cierre del docente: [S15-Guion-Conclusiones.pdf](attachments/S15-Guion-Conclusiones.pdf).

¡Finalizaste la semana! Repasemos algunas **ideas clave** de lo que hemos aprendido en esta sesión de aprendizaje.

## Ideas clave de la semana

> [!summary] 1. El campo magnético es el corazón de la máquina asíncrona
> El **campo magnético** es esencial para el funcionamiento de una **máquina asíncrona de corriente alterna**, ya que **induce voltajes y corrientes en el rotor**. Este campo es generado principalmente por el **estator** y es el responsable de la operación del motor.
>
> Detalle en [[S15-1 Tema 01 - Máquinas de corriente alterna|Tema 01]].

> [!summary] 2. Campo rotativo del estator → par motor
> Una máquina asíncrona, como un **motor trifásico**, utiliza la energía eléctrica de corriente alterna para generar un **campo magnético rotativo en el estator**. Ese campo interactúa con el rotor **induciendo corrientes** que generan un **par motor** y hacen girar el rotor. No hay conexión eléctrica entre estator y rotor: todo ocurre por **inducción**.

> [!summary] 3. Velocidad de sincronismo
> La **velocidad de sincronismo** es la velocidad a la que giraría el campo magnético rotativo creado en el estator si no hubiera deslizamiento. Queda determinada por la **frecuencia** de la corriente alterna suministrada y el **número de pares de polos**:
>
> $$n_1 = \frac{60\,f_1}{p}$$
>
> - $n_1$ = velocidad de sincronismo (rpm).
> - $f_1$ = frecuencia de alimentación del estator (Hz).
> - $p$ = número de **pares** de polos (4 polos → $p = 2$).

> [!summary] 4. El deslizamiento es necesario, no un defecto
> El **deslizamiento** es la diferencia entre la velocidad de sincronismo y la velocidad real del rotor. Indica cuánto se "queda atrás" el rotor respecto del campo giratorio del estator:
>
> $$s = \frac{n_1 - n}{n_1} = \frac{f_2}{f_1} \qquad\qquad f_r = s\,f_e$$
>
> Un **deslizamiento no nulo es imprescindible**: sin velocidad relativa no habría FEM inducida, ni corriente en el rotor, ni par motor. De ahí el nombre **asíncrona**.
>
> Aplicación numérica en el [[S15-2 Ejercicio resuelto - Máquina asíncrona trifásica (Video)|ejercicio de la máquina asíncrona trifásica]].

> [!summary] 5. Máquina síncrona: sin deslizamiento
> En la **máquina síncrona** de corriente alterna el campo magnético se genera en el **rotor** (alimentado en CC) e induce voltajes y corrientes en el **estator**. La frecuencia del rotor depende de la frecuencia de la alimentación trifásica (el campo giratorio) y la frecuencia del estator **es la misma que la del rotor**, por lo que **no existe deslizamiento**.
>
> Comparativa completa en [[S15-1 Tema 01 - Máquinas de corriente alterna|Tema 01]].

¡No olvides estas ideas importantes sobre las máquinas de corriente alterna: te serán de mucha utilidad a lo largo de tu carrera!

## Conexión con la siguiente semana

Esta semana estableció el marco general de las **máquinas de corriente alterna** (campo giratorio, sincronismo y deslizamiento). La [[S16-0 Introducción - Motores asíncronos de inducción|semana 16]] profundiza en el **motor de inducción**: su **principio de funcionamiento**, su **circuito equivalente** (el motor como transformador giratorio) y el balance de **potencia y par**.

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Ideas clave de la semana 15* [Video – Guion]. UTP+class.
