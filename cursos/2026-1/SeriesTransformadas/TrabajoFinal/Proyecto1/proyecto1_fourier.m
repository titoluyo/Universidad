% =====================================================================
%  proyecto1_fourier.m
%  Proyecto 1 - Series y Transformadas (UTP 2026-1)
%  Serie de Fourier de una senal senoidal RECTIFICADA DE MEDIA ONDA:
%    - reconstruye la senal con N terminos (coeficientes teoricos),
%    - grafica f(t) vs. S_N(t) para varios N,
%    - calcula el error cuadratico medio Ek teorico (Parseval) y
%      simulado (integracion numerica con trapz) y los compara.
%
%  Ejecutar en GNU Octave:  >> proyecto1_fourier
%  Requiere el paquete de graficas por defecto (no hace falta 'pkg load').
% =====================================================================
clear; clc; close all;

% ---------- 1. Parametros de la senal ----------
A  = 12*sqrt(2);        % amplitud pico [V]  (secundario 12 Vrms -> pico)
T  = 1/60;              % periodo [s]        (red peruana 60 Hz)
w0 = 2*pi/T;            % frecuencia angular fundamental [rad/s]
printf("A = %.4f V | T = %.4f ms | w0 = %.4f rad/s\n", A, T*1000, w0);

% ---------- 2. Coeficientes teoricos ----------
% a0 = 2A/pi ; a1 = 0 ; an = -2A/(pi(n^2-1)) para n par, 0 para n impar>=3
% b1 = A/2   ; bn = 0 para n>=2
a_coef = @(n) (n==0).*(2*A/pi) + (n>=2 & mod(n,2)==0).*(-2*A./(pi*(n.^2-1)));
b_coef = @(n) (n==1).*(A/2);

% ---------- 3. Senal original (media onda) ----------
% f(t) = A*sin(w0 t) cuando sin(w0 t) >= 0 ; 0 en el resto
f_orig = @(t) A*sin(w0*t) .* (sin(w0*t) >= 0);

% ---------- 4. Reconstruccion S_N(t) ----------
function y = S_N(t, N, A, w0, a_coef, b_coef)
  y = (a_coef(0)/2) * ones(size(t));        % componente DC = A/pi
  for n = 1:N
    y = y + a_coef(n)*cos(n*w0*t) + b_coef(n)*sin(n*w0*t);
  end
end

% ---------- 5. Vector de tiempo (2 periodos, paso fino) ----------
Np = 4000;                       % puntos por periodo
t  = linspace(0, 2*T, 2*Np);
f  = f_orig(t);

% ===== FIGURA 1: senal original =====
figure(1);
plot(t*1000, f, 'LineWidth', 1.8, 'Color', [0.12 0.31 0.55]);
xlabel('t [ms]'); ylabel('f(t) [V]');
title('Figura 1. Senal senoidal rectificada de media onda (A=12\surd2 V, 60 Hz)');
grid on;
print(figure(1), 'fig1_senal.png', '-dpng', '-r130');

% ===== FIGURA 2: superposicion f vs S_N =====
figure(2);
Ns = [1 2 4 10];
for i = 1:4
  subplot(2,2,i);
  plot(t*1000, f, 'Color', [0.6 0.6 0.6], 'LineWidth', 2.4); hold on;
  plot(t*1000, S_N(t, Ns(i), A, w0, a_coef, b_coef), 'r', 'LineWidth', 1.5);
  title(sprintf('N = %d armonicos', Ns(i)));
  xlabel('t [ms]'); ylabel('V'); grid on;
  legend('f(t) original', sprintf('S_N, N=%d', Ns(i)), 'location', 'northeast');
  hold off;
end
print(figure(2), 'fig2_superposicion.png', '-dpng', '-r130');

% ===== 6. Error cuadratico medio =====
P = A^2/4;                        % potencia media teorica [V^2]

function E = Ek_teorico(k, A, P, a_coef, b_coef)
  s = (a_coef(0)/2)^2;
  for n = 1:k
    s = s + 0.5*(a_coef(n)^2 + b_coef(n)^2);
  end
  E = P - s;
end

% error simulado: (1/T) * integral_0^T [f - S_k]^2 dt  con trapz (un periodo)
tp = linspace(0, T, Np);
fp = f_orig(tp);
function E = Ek_simulado(k, tp, fp, T, A, w0, a_coef, b_coef)
  e = fp - S_N(tp, k, A, w0, a_coef, b_coef);
  E = trapz(tp, e.^2) / T;
end

ks = [1 2 4 6 10];
printf('\n  k |  Ek_teorico [V^2] | Ek_simulado [V^2] | dif.rel(%%)\n');
Et = zeros(size(ks)); Es = zeros(size(ks));
for i = 1:numel(ks)
  k = ks(i);
  Et(i) = Ek_teorico(k, A, P, a_coef, b_coef);
  Es(i) = Ek_simulado(k, tp, fp, T, A, w0, a_coef, b_coef);
  dr = abs(Et(i)-Es(i))/Et(i)*100;
  printf(' %2d |   %.6e    |   %.6e    |  %6.3f\n', k, Et(i), Es(i), dr);
end

% ===== FIGURA 3: Ek vs k (semilog) =====
kk = 1:12;
Ek_t = arrayfun(@(k) Ek_teorico(k, A, P, a_coef, b_coef), kk);
Ek_s = arrayfun(@(k) Ek_simulado(k, tp, fp, T, A, w0, a_coef, b_coef), kk);
figure(3);
semilogy(kk, Ek_t, 'o-', 'LineWidth', 1.6, 'Color', [0.12 0.31 0.55]); hold on;
semilogy(kk, Ek_s, 's--', 'LineWidth', 1.4, 'Color', [0.75 0.23 0.16]);
xlabel('k (numero de armonicos)'); ylabel('Ek [V^2] (escala log)');
title('Figura 3. Error cuadratico medio Ek vs. numero de terminos');
legend('Ek teorico (Parseval)', 'Ek simulado (trapz)'); grid on; hold off;
print(figure(3), 'fig3_error.png', '-dpng', '-r130');

printf('\nPotencia media P = A^2/4 = %.4f V^2\n', P);
printf('Figuras exportadas: fig1_senal.png, fig2_superposicion.png, fig3_error.png\n');
