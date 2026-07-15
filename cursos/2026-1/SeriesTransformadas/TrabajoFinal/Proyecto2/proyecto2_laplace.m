% =====================================================================
%  proyecto2_laplace.m
%  Proyecto 2 - Series y Transformadas (UTP 2026-1)
%  Voltaje del capacitor Vo(t) de un circuito RLC serie con fuente escalon,
%  resuelto por Transformada de Laplace:
%    - solucion TEORICA cerrada  Vo(t) = 100 - 100 e^{-3t}cos4t - 75 e^{-3t}sin4t
%    - solucion SIMULADA integrando numericamente la EDO con lsode (via
%      independiente: NO usa la formula cerrada),
%    - grafica ambas superpuestas y calcula el error punto a punto (RMSE).
%
%  Circuito:  L=1 H, R=6 Ohm, C=0.04 F, E=100 V (escalon en t=0)
%  EDO:       vC'' + 6 vC' + 25 vC = 2500 ,  vC(0)=0, vC'(0)=0
%
%  Ejecutar en GNU Octave:  >> proyecto2_laplace
% =====================================================================
clear; clc; close all;

% ---------- 1. Parametros del circuito ----------
L = 1; R = 6; C = 0.04; E = 100;
a1 = R/L;            % 6   (coef. de vC')
a0 = 1/(L*C);        % 25  (coef. de vC)
u  = E/(L*C);        % 2500 (termino forzante)
printf("R/L = %g | 1/LC = %g | E/LC = %g\n", a1, a0, u);

% Parametros del sistema de 2do orden
alpha = R/(2*L);            % atenuacion = 3
w0    = sqrt(1/(L*C));      % frec. natural = 5 rad/s
zeta  = alpha/w0;           % amortiguamiento = 0.6 (subamortiguado)
wd    = w0*sqrt(1-zeta^2);  % frec. amortiguada = 4 rad/s
Mp    = exp(-zeta*pi/sqrt(1-zeta^2));   % sobreimpulso
tp    = pi/wd;                          % tiempo de pico
printf("alpha=%g  w0=%g  zeta=%g  wd=%g\n", alpha, w0, zeta, wd);
printf("Sobreimpulso Mp=%.3f%%  Vpico=%.3f V @ tp=%.4f s  ts(2%%)=%.4f s\n", ...
        Mp*100, E*(1+Mp), tp, 4/alpha);

% ---------- 2. Solucion teorica (cerrada, por Laplace) ----------
Vo_teo = @(t) E - 100*exp(-3*t).*cos(4*t) - 75*exp(-3*t).*sin(4*t);

% ---------- 3. Solucion simulada (via independiente: EDO numerica) ----------
% Estado x = [vC; vC'] ;  x1' = x2 ;  x2' = u - a1*x2 - a0*x1
function xdot = rlc(x, t)
  global A1 A0 U
  xdot = [ x(2);  U - A1*x(2) - A0*x(1) ];
end
global A1 A0 U
A1 = a1; A0 = a0; U = u;

t  = linspace(0, 2.5, 2501)';        % vector de tiempo (columna)
x0 = [0; 0];                          % vC(0)=0, vC'(0)=0
X  = lsode(@rlc, x0, t);              % integrador de Octave
Vo_sim = X(:,1);                      % voltaje del capacitor simulado

vt = Vo_teo(t);

% ===== FIGURA 1: respuesta teorica con anotaciones =====
figure(1);
plot(t, vt, 'LineWidth', 2.0, 'Color', [0.12 0.24 0.41]); hold on;
plot([0 2.5], [E E], '--', 'Color', [0.6 0.6 0.6]);
plot(tp, E*(1+Mp), 'o', 'Color', [0.71 0.20 0.10], 'MarkerFaceColor', [0.71 0.20 0.10]);
xlabel('t [s]'); ylabel('V_o [V]');
title('Figura 2. Respuesta teorica del voltaje del capacitor (subamortiguado)');
legend('V_o(t) teorico', 'V_o(\infty)=100 V', 'location', 'southeast'); grid on; hold off;
print(figure(1), 'fig2_vo_teorico.png', '-dpng', '-r130');

% ===== FIGURA 2: comparacion teorico vs simulado =====
figure(2);
plot(t, vt, 'LineWidth', 3.0, 'Color', [0.55 0.55 0.55]); hold on;
plot(t(1:40:end), Vo_sim(1:40:end), 'o', 'Color', [0.71 0.20 0.10], 'MarkerSize', 4);
xlabel('t [s]'); ylabel('V_o [V]');
title('Figura 3. Comparacion V_o(t): teorico (Laplace) vs. simulado (Octave)');
legend('V_o teorico (Laplace)', 'V_o simulado (lsode)', 'location', 'southeast');
grid on; hold off;
print(figure(2), 'fig3_comparacion.png', '-dpng', '-r130');

% ===== 4. Error punto a punto =====
err_abs = abs(vt - Vo_sim);
rmse    = sqrt(mean((vt - Vo_sim).^2));
printf("\nRMSE = %.4e V   max|err| = %.4e V\n", rmse, max(err_abs));

% Tabla en instantes representativos
inst = [0 0.2 0.4 0.6 tp 1.0 4/alpha 1.6 2.0 2.5];
printf("\n  t[s]   | Vo_teo[V] | Vo_sim[V] | |err|[V]  | err_rel[%%]\n");
for ti = inst
  [~, j] = min(abs(t - ti));
  a = Vo_teo(t(j)); b = Vo_sim(j); e = abs(a-b);
  printf(" %6.4f | %9.4f | %9.4f | %.3e | %.3e\n", t(j), a, b, e, e/E*100);
end

% ===== FIGURA 3: error absoluto puntual (semilog) =====
figure(3);
semilogy(t(2:end), err_abs(2:end), 'LineWidth', 1.5, 'Color', [0.48 0.12 0.61]); hold on;
plot([0 2.5], [rmse rmse], '--', 'Color', [0.71 0.20 0.10], 'LineWidth', 1.2);
xlabel('t [s]'); ylabel('|V_{teo}-V_{sim}| [V] (escala log)');
title('Figura 4. Error absoluto puntual entre teoria y simulacion');
legend('|error|', sprintf('RMSE = %.2e V', rmse), 'location', 'northeast');
grid on; hold off;
print(figure(3), 'fig4_error.png', '-dpng', '-r130');

printf("\nFiguras exportadas: fig2_vo_teorico.png, fig3_comparacion.png, fig4_error.png\n");
printf("(El diagrama del circuito, Figura 1, se dibuja aparte.)\n");
