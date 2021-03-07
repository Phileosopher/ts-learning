% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% This is a second version that I made, to test it out.
% I have a problem where the corrected FG does not make sense.
%
%
% ``Formula for compensation of ethanol effect on refractometer:
%
% SG=1.001843-0.002318474(OB)-0.000007775(OB^2)-0.000000034(OB^3)+0.00574(AB) +0.00003344(AB^2)+0.000000086(AB^3)
%
% SG = Specific Gravity, OB = Original Brix, AB = Actual Brix (Brix Readings During Fermentation)''
% [ Source: http://www.homebrewstuff.com/refractometer-how-to]
%OG = 1.085; % OG;
%FG = 1.032; % FG;

OG = 1.090; %1.117; %1.1195; %1.117; % OG;
FG = 1.030; %1.0525; %1.075; % FG;
% Convert OG and FG to Brix
x = grav2brix(OG);

i=1;
while (FG < OG)
    y = grav2brix(FG);
    %disp(sprintf('With OG %6.3f, or %4.1f Brix,', OG, x));
    %disp(sprintf(' and FG %6.3f, or %4.1f Brix,', FG, y));
    c = [ 1.001843, 0.002318474, 0.000007775, 0.000000034, 0.00574, 0.00003344, 0.000000086 ];
    % w = c(1) - c(2) * x - c(3) * x^2 - c(4) * x^3 + c(5) * y + c(6) * y^2 + c(7) * y^3;
    w(i) = c(1) - c(2) .* x - c(3) .* x.^2 - c(4) .* x.^3 + c(5) .* y + c(6) .* y.^2 + c(7) .* y.^3;
    %disp(sprintf(' the corrected Refractometer reading is %6.3f', w));
    
    % This is from
    % http://seanterrill.com/2011/04/07/refractometer-fg-results/
    % a blog by Sean Terrill, who seems to have already solved this problem.
    d = [1.0000, -0.0044993, 0.00027581, -0.0000072800,   0.011774, -0.0012717, 0.000063293];
    v(i) = d(1) + d(2) .* x + d(3) .* x.^2 + d(4) .* x.^3 + d(5) .* y + d(6) .* y.^2 + d(7) .* y.^3;
    %disp(sprintf(' the corrected Refractometer reading (Terrill) is %6.3f', v));
    
    % From http://seanterrill.com/2011/04/07/refractometer-fg-results/
    % The line below LOOKS OK, but it generates an error
    % "The input character is not valid in MATLAB statements or expressions."
    %u(i) = 1.0000 – 0.00085683*x + 0.0034941*y;
    % It is the dash. Below is the same thing, with a minus-sign.
    u(i) = 1.0000 - 0.00085683*x + 0.0034941*y;
    %
    % Copy and paste both lines below to see the problem
    % 1 – 0.8
    % 1 - 0.8
    
    
    FGreadings(i) = FG;
    FG = FG + 0.005;
    i = i + 1;
end

% show the OG readings as a line
OGreadings(1:length(w)) = OG;
lowestMin = min([ min(FGreadings), min(w), min(v) ]);
% x_axis_numbers = 1:length(w);
x_axis_numbers = FGreadings;

plot(x_axis_numbers, w, 'b');
hold('on');
plot(x_axis_numbers, v, 'r');
plot(x_axis_numbers, u, 'm');
plot(x_axis_numbers, FGreadings, 'k');
plot(x_axis_numbers, OGreadings, 'g');
title('FG corrections blue, Terrill method in red and purple, OG:green, uncorrected readings:black');
axis([x_axis_numbers(1) max(x_axis_numbers) lowestMin (OG + 0.01) ]);

