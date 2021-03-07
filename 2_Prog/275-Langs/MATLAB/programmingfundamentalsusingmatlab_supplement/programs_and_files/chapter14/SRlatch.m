% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Use simulink on "SRlatch_simfile.mdl", then
% show the waveforms.
%
%

sim SRlatch_simfile

Clock = simout2.signals.values;
R = simout1.signals.values;
S = simout6.signals.values;
w = simout.signals.values;
x = simout5.signals.values;
Q = simout3.signals.values;
Q_prime = simout4.signals.values;

plot((1:length(Clock))/100, Clock + 12, 'r');
hold on
plot((1:length(R))/100, R + 10, 'b');
plot((1:length(S))/100, S + 8, 'g');
plot((1:length(w))/100, w + 6, 'b.-');
plot((1:length(x))/100, x + 4, 'g.-');
plot((1:length(Q))/100, Q + 2, 'k');
plot((1:length(Q_prime))/100, Q_prime, 'm');
% axis tight
axis([1/100 length(Q)/100 -0.5 13.5]);
grid on
xlabel('time');
title('Clock in red, R input in blue, S input in green, Q output in black');

% Add text to the plot (labels on the left)
str1 = text(0.1,12.5,'Clock');
set(str1, 'color', [0.5, 0.5, 0.5]);
set(str1, 'FontSize', 16);

str2 = text(0.1,10.5,'R');
set(str2, 'color', [0.5, 0.5, 0.5]);
set(str2, 'FontSize', 16);

str2b = text(0.1,8.5,'S');
set(str2b, 'color', [0.5, 0.5, 0.5]);
set(str2b, 'FontSize', 16);

Wstr = text(0.1,6.5,'w');
set(Wstr, 'color', [0.5, 0.5, 0.5]);
set(Wstr, 'FontSize', 16);

Xstr = text(0.1,4.5,'x');
set(Xstr, 'color', [0.5, 0.5, 0.5]);
set(Xstr, 'FontSize', 16);

str3 = text(0.1,2.5,'Q');
set(str3, 'color', [0.5, 0.5, 0.5]);
set(str3, 'FontSize', 16);

str4 = text(0.1,0.5,'Q''');
set(str4, 'color', [0.5, 0.5, 0.5]);
set(str4, 'FontSize', 16);

