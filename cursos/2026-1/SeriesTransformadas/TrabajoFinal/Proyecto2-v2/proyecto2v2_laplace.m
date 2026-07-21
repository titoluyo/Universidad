% ============================================================
% proyecto2v2_laplace.m  --  Proyecto 2 v2 (PROY, Series y Transformadas)
% Voltaje del capacitor V_o(t) en un circuito R-L-C serie con fuente escalon.
% Compara la solucion TEORICA (Transformada de Laplace, forma cerrada)
% contra la SIMULADA (integracion numerica de la EDO con lsode).
% Circuito: R = 6 ohm, L = 1 mH, C = 4 uF, E = 300 V, CI nulas.
% ============================================================
clear all; close all; clc;

% --- 1. Parametros del circuito ---
R = 6;        % ohm
L = 1e-3;     % H   (1 mH)
C = 4e-6;     % F   (4 uF)
E = 300;      % V   (fuente escalon, cierra en t = 0)

a1 = R/L;         % 6000       (EDO en q:  q'' + a1 q' + a0 q = u)
a0 = 1/(L*C);     % 2.5e8
u  = E/L;         % 3e5
alpha = a1/2;                 % 3000 s^-1 (parte real de los polos)
wd    = sqrt(a0 - alpha^2);   % 1000*sqrt(241) ~ 15524.2 rad/s

printf("Circuito R-L-C serie: R=%g ohm, L=%g H, C=%g F, E=%g V\n", R, L, C, E);
printf("EDO en q:  q'' + %g q' + %.3e q = %.3e   (q(0)=0, q'(0)=0)\n", a1, a0, u);
printf("Polos: -%g +/- j%.4f  |  alpha=%g s^-1, wd=%.4f rad/s (f_d=%.1f Hz)\n\n", ...
       alpha, wd, alpha, wd, wd/(2*pi));

% --- 2. Solucion teorica cerrada (obtenida por Laplace) ---
% q(t)  = C*E - e^{-alpha t}( C*E cos(wd t) + (3.6/wd) sin(wd t) )    [C]
% Vo(t) = q(t)/C = 300 - e^{-3000 t}( 300 cos(wd t) + 900/sqrt(241) sin(wd t) )
kc = E;                 % 300
ks = 900/sqrt(241);     % 57.9748
Vo_teo = @(t) E - exp(-alpha*t).*(kc*cos(wd*t) + ks*sin(wd*t));

% --- 3. Solucion simulada: EDO numerica (via independiente) ---
% NO usa la formula cerrada: integra la EDO original con lsode.
% Estado x = [q; q'] ;  x1' = x2 ;  x2' = u - a1*x2 - a0*x1
f_rlc = @(x, t) [ x(2); u - a1*x(2) - a0*x(1) ];
t  = linspace(0, 2e-3, 4001)';        % 0 a 2 ms, paso 0.5 us
X  = lsode(f_rlc, [0; 0], t);         % CI: q(0)=0, q'(0)=0
q_sim  = X(:,1);                      % carga simulada [C]
Vo_sim = q_sim / C;                   % voltaje del capacitor simulado [V]

% --- 4. Error simulado vs. teorico ---
vt      = Vo_teo(t);
err_abs = abs(vt - Vo_sim);
rmse    = sqrt(mean((vt - Vo_sim).^2));
printf("RMSE        = %.4e V\n", rmse);
printf("max |error| = %.4e V\n\n", max(err_abs));

% Tabla en instantes representativos
tp = pi/wd;                            % primer pico (~0.2024 ms)
inst = [0.1e-3 tp 0.3e-3 0.5e-3 0.8e-3 1.0e-3 1.31e-3 2.0e-3];
printf("   t [ms]   | Vo teo [V]  | Vo sim [V]  |  |err| [V]  | err rel [%%]\n");
printf("------------+-------------+-------------+-------------+------------\n");
for ti = inst
  [~, k] = min(abs(t - ti));
  e = err_abs(k);
  printf("  %8.4f  | %11.4f | %11.4f | %.4e  | %.6f\n", ...
         t(k)*1e3, vt(k), Vo_sim(k), e, e/E*100);
end

Vp = E*(1 + exp(-alpha*pi/wd));        % pico teorico (en wd*t = pi)
printf("\nPico teorico: Vp = %.2f V en tp = %.4f ms (%.1f %% sobre la fuente)\n", ...
       Vp, tp*1e3, (Vp-E)/E*100);

% --- 5. Figuras (eje temporal en ms) ---
tms = t*1e3;

% Figura 2: respuesta teorica
figure(2);
plot(tms, vt, 'linewidth', 1.6); hold on;
plot([0 2], [E E], '--k');
plot(tp*1e3, Vp, 'v', 'markersize', 8, 'markerfacecolor', 'r');
text(tp*1e3 + 0.06, Vp, sprintf(' pico %.1f V', Vp));
grid on; xlabel('t [ms]'); ylabel('V_o [V]'); ylim([0 500]);
title('Figura 2. Respuesta teorica del voltaje del capacitor V_o(t)');
legend('V_o(t) teorico (Laplace)', 'V_o(\infty) = E = 300 V', 'location', 'southeast');
print(figure(2), 'attachments/fig2_vo_teorico.png', '-dpng', '-r130');

% Figura 3: comparacion teorico vs. simulado
figure(3);
plot(tms, vt, '-', 'color', [0.45 0.45 0.45], 'linewidth', 2); hold on;
plot(tms(1:80:end), Vo_sim(1:80:end), 'ro', 'markersize', 4);
grid on; xlabel('t [ms]'); ylabel('V_o [V]'); ylim([0 500]);
title('Figura 3. V_o(t): teorico (Laplace) vs. simulado (Octave, lsode)');
legend('teorico', 'simulado', 'location', 'southeast');
print(figure(3), 'attachments/fig3_comparacion.png', '-dpng', '-r130');

% Figura 4: error absoluto puntual
figure(4);
semilogy(tms, err_abs + eps, 'linewidth', 1.2); hold on;
semilogy([0 2], [rmse rmse], '--r');
grid on; xlabel('t [ms]'); ylabel('|V_o^{teo} - V_o^{sim}| [V]');
title('Figura 4. Error absoluto puntual entre teoria y simulacion');
legend('|error(t)|', sprintf('RMSE = %.2e V', rmse), 'location', 'southeast');
print(figure(4), 'attachments/fig4_error.png', '-dpng', '-r130');

printf("\nFiguras exportadas: fig2_vo_teorico.png, fig3_comparacion.png, fig4_error.png\n");
printf("(El diagrama del circuito, Figura 1, se dibuja aparte.)\n");
