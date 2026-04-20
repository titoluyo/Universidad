---
title: Funciones analiticas, holomorfas, armonicas y armonicas conjugadas
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 4
orden: 1
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/funcion-analitica
  - tema/funcion-holomorfa
  - tema/funcion-armonica
  - tema/conjuntos-plano-complejo
  - tema/cauchy-riemann
date: 2026-04-19
---

## Introduccion

En esta sesion se aborda el conjunto de numeros complejos, donde a cada $z$ se le asigna un numero complejo $w$ mediante una funcion $f$. Antes de caracterizar una **funcion de una variable compleja**, se revisan las nociones topologicas basicas en el plano complejo (conjunto abierto, cerrado, conexo, puntos interior/frontera/exterior, region) porque sobre ellas se definen las propiedades de analiticidad, holomorfia y armonicidad.

> [!summary] Contenido de la sesion
> 1. Conceptos topologicos en el plano complejo (conjuntos, puntos, regiones, entornos)
> 2. **Funcion analitica** — derivable en todo punto de un conjunto abierto
> 3. **Funcion holomorfa** — sinonimo de analitica, destaca la existencia de la derivada
> 4. **Funcion armonica** — satisface la ecuacion de Laplace
> 5. **Funcion armonica conjugada** — $u$ y $v$ armonicas que cumplen Cauchy-Riemann
> 6. Propiedades, aplicaciones y transformaciones conformes

## 1. Conceptos topologicos en el plano complejo

### Vecindad o entorno

Dado un punto $z_0 \in \mathbb{C}$ y un numero real $\rho > 0$, se definen:

| Region | Desigualdad | Descripcion |
| --- | --- | --- |
| Disco abierto (vecindad) | $\|z - z_0\| < \rho$ | Interior de la circunferencia sin la frontera |
| Disco cerrado | $\|z - z_0\| \leq \rho$ | Interior + frontera |
| Circunferencia | $\|z - z_0\| = \rho$ | Solo la frontera |
| Exterior | $\|z - z_0\| > \rho$ | Complemento del disco cerrado |
| Anillo circular abierto | $\rho_1 < \|z - z_0\| < \rho_2$ | Region entre dos circunferencias concentricas |

### Conjunto abierto

Un conjunto $S \subseteq \mathbb{C}$ se dice **abierto** si para cada punto $z_0 \in S$ existe un numero real positivo $r$ tal que el disco $|z - z_0| < r$ esta contenido completamente en $S$.

> [!example] Ejemplo
> El conjunto $\{z \in \mathbb{C} : |z| < 1\}$ (disco unitario abierto) es un conjunto abierto.

### Conjunto cerrado

Un conjunto $S$ es **cerrado** si su complemento es abierto. Equivalentemente, $S$ es cerrado si contiene a todos sus puntos limites.

> [!example] Ejemplo
> El conjunto $\{z \in \mathbb{C} : |z| \leq 1\}$ (disco unitario cerrado) es un conjunto cerrado.

### Conjunto conexo

Un conjunto abierto $S$ es **conexo** si cualquier par de puntos del conjunto puede unirse por un camino formado por segmentos de recta (camino poligonal) contenidos en $S$.

### Region (dominio)

Una **region** o **dominio** es un conjunto **abierto y conexo**. Muchas definiciones posteriores (analiticidad, holomorfia, armonicidad) se formulan sobre un dominio $D$.

### Clasificacion de puntos

Sea $z_0$ un punto del plano complejo y $S$ un conjunto:

- **Punto interior:** $z_0$ es punto interior de $S$ si podemos encontrar una vecindad de $z_0$ cuyos puntos pertenecen todos a $S$. Es decir, existe $r > 0$ tal que $|z - z_0| < r \subseteq S$.
- **Punto exterior:** $z_0$ es punto exterior de $S$ si existe $r > 0$ tal que el disco $|z - z_0| < r$ no intersecta a $S$.
- **Punto frontera:** si cada vecindad de $z_0$ contiene puntos que pertenecen a $S$ y tambien puntos que no pertenecen a $S$, entonces $z_0$ es un punto frontera.
- **Punto de acumulacion (o punto limite):** $z_0$ es punto de acumulacion de $S$ si toda vecindad de $z_0$ contiene al menos un punto de $S$ distinto de $z_0$.

> [!info] Relacion
> Todo punto interior es punto de acumulacion, pero no todo punto de acumulacion es interior (puede ser frontera).

> [!example] Clasificacion sobre $C = \{z \in \mathbb{C} : 0 < |z| < 1\}$
> - $|z| = 1$ → punto frontera (no pertenece a $C$, pero todo disco centrado en $z$ contiene puntos de $C$ y fuera de $C$)
> - $0 < |z| < 1$ → punto interior (pertenece a $C$ y existe vecindad totalmente contenida en $C$)
> - $|z| = 0$ → punto frontera / punto de acumulacion (no pertenece a $C$ pero esta "pegado" al conjunto)

## 2. Funcion analitica

### Definicion

Una funcion $f$ de una variable compleja $z$ es **analitica** en un punto $z_0 \in \mathbb{C}$ si la derivada $f'(z)$ existe en $z_0$ y en todo punto de alguna vecindad de $z_0$.

Si $f(z)$ es analitica en todos los puntos de un dominio $D \subset \mathbb{C}$, se dice que $f(z)$ es **analitica en $D$**.

> [!info] Terminologia equivalente
> En variable compleja, los siguientes terminos son sinonimos:
> - **Analitica**
> - **Holomorfa**
> - **Regular**
> - **Diferenciable en el sentido complejo**

### Condicion necesaria: Cauchy-Riemann

Una condicion necesaria para que $f$ sea analitica en un dominio $D$ es la **continuidad** de $f$ sobre $D$ y que se satisfagan las **ecuaciones de Cauchy-Riemann**:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

> [!note] Relacion con la semana anterior
> Las ecuaciones de Cauchy-Riemann se introdujeron en [[S03-1 Tema 03 - Derivada de una funcion compleja]] como condicion necesaria para la existencia de $f'(z_0)$ en un punto. Aqui se extienden como condicion sobre todo un dominio.

### Derivada de una funcion analitica

Si $f(z) = u(x, y) + iv(x, y)$ es analitica en $z_0$, entonces:

$$f'(z_0) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x} = \frac{\partial v}{\partial y} - i\frac{\partial u}{\partial y}$$

### Propiedades algebraicas

Si $f(z)$ y $g(z)$ son analiticas en una region $D$, entonces:

| Operacion | Resultado |
| --- | --- |
| Suma | $f(z) + g(z)$ es analitica en $D$ |
| Producto | $f(z) \cdot g(z)$ es analitica en $D$ |
| Cociente | $f(z)/g(z)$ es analitica en $D \setminus \{z : g(z) = 0\}$ |
| Composicion | Si $f: D_1 \to \mathbb{C}$ y $g: D_2 \to \mathbb{C}$ son analiticas con $f(D_1) \subseteq D_2$, entonces $g(f(z))$ es analitica en $D_1$ |

### Procedimiento para verificar analiticidad

> [!abstract] Pasos
> Para verificar que $f(z)$ es analitica en $z_0$:
> 1. Escribir $f(z) = u(x, y) + i\,v(x, y)$.
> 2. Calcular las derivadas parciales $u_x, u_y, v_x, v_y$.
> 3. Verificar las ecuaciones de Cauchy-Riemann en $(x_0, y_0)$:
>    $$u_x(x_0, y_0) = v_y(x_0, y_0), \quad u_y(x_0, y_0) = -v_x(x_0, y_0)$$
> 4. Comprobar que $u_x, u_y, v_x, v_y$ son continuas en $(x_0, y_0)$.

### Ejemplo: $f(z) = z^2$ es analitica en todo $\mathbb{C}$

Sea $f(z) = z^2$. Entonces $f(z) = (x + iy)^2 = (x^2 - y^2) + i(2xy)$, con:

- $u(x, y) = x^2 - y^2$
- $v(x, y) = 2xy$

Derivadas parciales:

$$\frac{\partial u}{\partial x} = 2x, \qquad \frac{\partial u}{\partial y} = -2y$$

$$\frac{\partial v}{\partial x} = 2y, \qquad \frac{\partial v}{\partial y} = 2x$$

Cauchy-Riemann:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \;\Rightarrow\; 2x = 2x \checkmark$$

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} \;\Rightarrow\; -2y = -2y \checkmark$$

Como las derivadas son continuas y C-R se cumple en todo $\mathbb{C}$, $f(z) = z^2$ es **analitica en todo $\mathbb{C}$**.

### Ejemplo: $f(z) = z^3 - 3xy^2 + i(3x^2y - y^3)$ es analitica

Siendo $u(x, y) = x^3 - 3xy^2$ y $v(x, y) = 3x^2y - y^3$:

$$u_x = 3x^2 - 3y^2, \quad u_y = -6xy, \quad v_x = 6xy, \quad v_y = 3x^2 - 3y^2$$

Las derivadas parciales son continuas en todo $\mathbb{C}$ y satisfacen Cauchy-Riemann:
- $u_x = v_y$: $3x^2 - 3y^2 = 3x^2 - 3y^2 \checkmark$
- $u_y = -v_x$: $-6xy = -6xy \checkmark$

Por tanto, $f(z) = z^3$ es analitica en todo el plano complejo.

## 3. Funcion holomorfa

Sea una funcion compleja $f$ definida sobre un conjunto abierto $S$. Decimos que $f$ es **holomorfa** cuando tiene derivada en todo punto de $S$.

Los puntos en los que una funcion no es holomorfa se llaman **puntos de singularidad** o **singularidades**.

> [!info] Analitica vs holomorfa
> En variable compleja, ambos terminos son equivalentes: una funcion es holomorfa en un conjunto abierto si y solo si es analitica en el. La distincion es historica y de enfasis:
> - *Holomorfa* subraya la existencia de la derivada compleja en cada punto.
> - *Analitica* subraya la representabilidad local como serie de potencias (Taylor).

> [!example] Singularidades de $f(z) = 1/(z^2 + 1)$
> La funcion es holomorfa en todo $\mathbb{C}$ excepto donde el denominador se anula:
> $$z^2 + 1 = 0 \;\Rightarrow\; z = \pm i$$
> Por tanto, $f$ es holomorfa en $\mathbb{C} \setminus \{i, -i\}$ y tiene singularidades en $z = i$ y $z = -i$.

## 4. Funcion armonica

### Definicion

Una funcion real $u(x, y)$ de dos variables reales se dice **armonica** en un dominio $D$ si:

1. Tiene derivadas parciales continuas de segundo orden en $D$.
2. Satisface la **ecuacion de Laplace**:

$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

Donde:

- $\nabla^2 = \dfrac{\partial^2}{\partial x^2} + \dfrac{\partial^2}{\partial y^2}$ es el operador Laplaciano.
- Las soluciones con derivadas continuas de segundo orden de la ecuacion de Laplace se llaman **funciones armonicas**.

### Teorema fundamental

> [!tip] Teorema
> Si $f(z) = u(x, y) + i\,v(x, y)$ es **analitica** en un dominio $D$, entonces tanto $u(x, y)$ como $v(x, y)$ son **funciones armonicas** en $D$:
> $$\nabla^2 u = 0, \qquad \nabla^2 v = 0$$

**Demostracion:** Si $f$ es analitica, satisface las ecuaciones de Cauchy-Riemann:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

Derivando la primera respecto a $x$ y la segunda respecto a $y$:

$$\frac{\partial^2 u}{\partial x^2} = \frac{\partial^2 v}{\partial x \partial y}, \qquad \frac{\partial^2 u}{\partial y^2} = -\frac{\partial^2 v}{\partial y \partial x}$$

Como las derivadas mixtas son iguales ($v_{xy} = v_{yx}$):

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = \frac{\partial^2 v}{\partial x \partial y} - \frac{\partial^2 v}{\partial y \partial x} = 0$$

Analogamente se demuestra que $\nabla^2 v = 0$. $\blacksquare$

### Ejemplo: $h(x, y) = x^2 - y^2$ es armonica en $\mathbb{C}$

Calculamos las derivadas parciales de primer y segundo orden:

$$h_x = 2x, \qquad h_y = -2y$$

$$h_{xx} = 2, \qquad h_{yy} = -2$$

$$h_{xy} = 0, \qquad h_{yx} = 0$$

Todas las derivadas son funciones continuas en $\mathbb{C}$. Aplicando la ecuacion de Laplace:

$$\nabla^2 h = h_{xx} + h_{yy} = 2 + (-2) = 0 \checkmark$$

Por tanto, $h(x, y) = x^2 - y^2$ es **armonica en todo $\mathbb{C}$**.

### Criterios de no-armonicidad

Una funcion $u(x, y)$ **no es armonica** si:

- $\nabla^2 u \neq 0$ en algun punto del dominio.
- Las derivadas segundas no existen o no son continuas.
- $u$ depende solo de una variable (excepto funciones lineales, para las cuales $\nabla^2 u = 0$ trivialmente).

### Ejemplos de funciones armonicas basicas

| $u(x, y)$ | Conjugada armonica $v(x, y)$ | $f(z) = u + iv$ |
| --- | --- | --- |
| $x^2 - y^2$ | $2xy$ | $z^2$ |
| $x^3 - 3xy^2$ | $3x^2y - y^3$ | $z^3$ |
| $e^x \cos y$ | $e^x \operatorname{sen} y$ | $e^z$ |
| $\ln(x^2 + y^2)$ | $2 \arctan(y/x)$ | $2 \ln z$ |
| $\operatorname{sen} x \cosh y$ | $\cos x \operatorname{senh} y$ | $\operatorname{sen} z$ |

## 5. Funcion armonica conjugada

### Definicion

Si dos funciones dadas $u$ y $v$ son armonicas en un dominio $D$ y sus derivadas de primer orden satisfacen las **ecuaciones de Cauchy-Riemann** en $D$, se dice que $v$ es **armonica conjugada** de $u$.

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

> [!warning] El orden importa
> La relacion "armonica conjugada" **no es simetrica por defecto**. Si $v$ es armonica conjugada de $u$, entonces en general $u$ **no** es armonica conjugada de $v$; lo que si se cumple es que $-u$ es armonica conjugada de $v$. El signo proviene directamente de las ecuaciones de Cauchy-Riemann.
>
> **Ejemplo:** $v(x,y) = 2xy$ es armonica conjugada de $u(x,y) = x^2 - y^2$, pero $u(x,y) = x^2 - y^2$ **no** es armonica conjugada de $v(x,y) = 2xy$.

### Teorema de existencia

> [!tip] Existencia
> Si $u(x, y)$ es armonica en una region **simplemente conexa** $D$, entonces existe una conjugada armonica $v(x, y)$ tal que $f(z) = u(x, y) + i\,v(x, y)$ es analitica en $D$.

### Unicidad

La conjugada armonica esta determinada **salvo una constante aditiva**. Si $v_1$ y $v_2$ son ambas conjugadas armonicas de $u$, entonces $v_1 - v_2 = C$ (constante real).

### Metodo para encontrar la conjugada armonica

Dada $u(x, y)$ armonica, para encontrar $v(x, y)$:

> [!abstract] Procedimiento (integracion sucesiva)
> **Paso 1:** De la primera ecuacion de C-R, $\dfrac{\partial u}{\partial x} = \dfrac{\partial v}{\partial y}$, integramos respecto a $y$:
> $$v(x, y) = \int \frac{\partial u}{\partial x}\, dy + g(x)$$
> donde $g(x)$ es una funcion de $x$ a determinar.
>
> **Paso 2:** De la segunda ecuacion de C-R, $\dfrac{\partial u}{\partial y} = -\dfrac{\partial v}{\partial x}$, calculamos $v_x$ a partir de la expresion anterior y la igualamos:
> $$\frac{\partial u}{\partial y} = -\frac{\partial}{\partial x}\left[\int \frac{\partial u}{\partial x}\, dy + g(x)\right]$$
>
> **Paso 3:** Despejamos $g'(x)$, integramos para obtener $g(x)$, y sustituimos en la expresion de $v(x, y)$.

### Metodo alternativo (integral de linea)

$$v(x, y) = \int_{(x_0, y_0)}^{(x, y)} \left(-\frac{\partial u}{\partial y}\, dx + \frac{\partial u}{\partial x}\, dy\right) + C$$

### Ejemplo: Verificar que $v(x, y) = 2xy$ es conjugada armonica de $u(x, y) = x^2 - y^2$

1. Verificar que $u$ y $v$ son armonicas: ya visto, $\nabla^2 u = 0$ y $\nabla^2 v = 0$.

2. Verificar Cauchy-Riemann:
   - $u_x = 2x$, $v_y = 2x$ → $u_x = v_y$ ✓
   - $u_y = -2y$, $v_x = 2y$ → $u_y = -v_x$ ✓

Por tanto, $v = 2xy$ **si** es conjugada armonica de $u = x^2 - y^2$, y $f(z) = (x^2 - y^2) + i(2xy) = z^2$ es analitica.

## 6. Relacion entre funciones analiticas y armonicas

> [!abstract] Cadena de implicaciones
> $f$ analitica en $D$ $\Leftrightarrow$ $f$ holomorfa en $D$ $\Rightarrow$ $u$ y $v$ son armonicas en $D$ $\Rightarrow$ $v$ es armonica conjugada de $u$.

- **Toda funcion analitica genera dos funciones armonicas** (su parte real e imaginaria).
- **Toda funcion armonica en una region simplemente conexa es la parte real de alguna funcion analitica**, obtenida construyendo su conjugada armonica.

### Ortogonalidad de curvas de nivel

Si $f(z) = u + iv$ es analitica, las familias de curvas $u(x, y) = c_1$ y $v(x, y) = c_2$ son **ortogonales**: en todo punto de interseccion sus gradientes son perpendiculares,

$$\nabla u \cdot \nabla v = 0$$

## 7. Propiedades de las funciones armonicas

### Principio del maximo

Si $u(x, y)$ es armonica y **no constante** en una region conexa $D$, entonces $u$ **no puede alcanzar su maximo ni su minimo en el interior** de $D$; sus extremos se localizan necesariamente en la frontera.

### Teorema de unicidad

Si $u(x, y)$ es armonica en una region $D$ y continua en $\overline{D}$ (la clausura de $D$), entonces $u$ esta **unicamente determinada por sus valores en la frontera** de $D$.

### Propiedad del valor medio

Si $u(x, y)$ es armonica en un disco, entonces el valor de $u$ en el centro del disco es igual al **promedio de $u$ sobre la circunferencia**.

### Formula integral de Poisson

Para el disco unitario, si $u(x, y)$ es armonica en $|z| < 1$ y continua en $|z| \leq 1$:

$$u(r \cos\theta, r \operatorname{sen}\theta) = \frac{1}{2\pi} \int_0^{2\pi} u(\cos\varphi, \operatorname{sen}\varphi) \cdot \frac{1 - r^2}{1 - 2r\cos(\theta - \varphi) + r^2}\, d\varphi$$

para $0 \leq r < 1$. Esta formula reconstruye los valores interiores de $u$ a partir de los de la frontera.

## 8. Transformaciones conformes

Una funcion analitica $f(z)$ con $f'(z) \neq 0$ define una **transformacion conforme**, que **preserva angulos** localmente.

**Propiedades:**

- Preserva angulos entre curvas en todos los puntos donde $f'(z) \neq 0$.
- Mapea familias ortogonales de curvas en familias ortogonales.
- Util para resolver problemas de valor en la frontera.

**Ejemplo:** $f(z) = \dfrac{z - i}{z + i}$ mapea el semiplano superior $\operatorname{Im}(z) > 0$ al disco unitario $|w| < 1$ de forma conforme, salvo en $z = -i$ donde no es analitica.

## 9. Aplicaciones fisicas

La ecuacion de Laplace $\nabla^2 \varphi = 0$ aparece en una gran variedad de problemas de la fisica matematica. En todos ellos, las soluciones son funciones armonicas:

| Fenomeno | Magnitud armonica |
| --- | --- |
| **Distribucion de temperatura estacionaria** | Temperatura $T(x, y)$ |
| **Potencial electrostatico** en regiones sin carga | Potencial $\varphi(x, y)$ |
| **Flujos irrotacionales e incompresibles** | Potencial de velocidad $\phi$ y funcion de corriente $\psi$ |
| **Conduccion de calor estacionaria** | Temperatura |
| **Potencial gravitacional** en regiones sin masa | Potencial |

### Problema de Dirichlet

Encontrar una funcion armonica $u(x, y)$ en una region $D$ que tome valores dados en la frontera de $D$. Las tecnicas de variable compleja (conjugada armonica + transformaciones conformes) permiten resolver este tipo de problemas reduciendolos a regiones simples como el disco unitario.

## Resumen

| Concepto | Requisito | Dominio de definicion |
| --- | --- | --- |
| **Analitica** | $f'(z)$ existe en cada punto y en una vecindad | Conjunto abierto $S$ |
| **Holomorfa** | $f'(z)$ existe en cada punto | Conjunto abierto $S$ (sinonimo de analitica) |
| **Armonica** | $\nabla^2 \varphi = 0$ con derivadas continuas de segundo orden | Dominio $D$ |
| **Armonica conjugada** | $u, v$ armonicas que satisfacen Cauchy-Riemann | Dominio $D$ |

## Ejercicios desarrollados en clase

Los ejemplos trabajados en la sesion se resuelven paso a paso en:

- [[S04-2 Tema 04 - Ejercicio 1 (SyT)|Ejercicio 1 — Probar que $f(z) = (y^3 - 3x^2y) + i(x^3 - 3xy^2 + 3)$ es armonica]]
- [[S04-3 Tema 04 - Ejercicio 2 (SyT)|Ejercicio 2 — Probar que $u = e^{-x}(x\operatorname{sen} y - y\cos y)$ es armonica]]
- [[S04-4 Tema 04 - Ejercicio 3 (SyT)|Ejercicio 3 — Encontrar la conjugada armonica de $u = x^2 - y^2 - y$]]
- [[S04-5 Tema 04 - Ejercicio 4 (SyT)|Ejercicio 4 — Demostrar que $f(z) = xy + iy$ no es analitica en ningun punto]]

## Bibliografia

- Churchill, R., & Ward, J. (2004). *Variable Compleja y Aplicaciones* (7ma ed.). McGraw-Hill.
- Murray, S., Seymour, Lipschutz, & Dennis, S. (2011). *Variable compleja* (2da ed.). McGraw-Hill Interamericana de Espana S.L.
- Suarez Bueno, V. (1998). *Introduccion a la Variable Compleja* (1a. ed.). Instituto Politecnico Nacional.
