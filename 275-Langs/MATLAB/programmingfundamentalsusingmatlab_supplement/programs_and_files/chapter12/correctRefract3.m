% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% This is a test version of a program that I made.
% I ran into an interesting problem here, and I made this version to
% demonstrate the problem.
%
%
% Note that this program uses grav2brix.m, and
% that uses Brix2SPGTable_v2.m, which has an error in one of the data points.
%   I wrote some text that discusses this, and I do not want to
% replace Brix2SPGTable_v2.
%   This data error PROBABLY does not affect this program.     
%
%
% To see the problem:
%   OG = 1.117;
%   correctRefract3
%   close;
%   OG = 1.090;
%   correctRefract3
%   disp('See how the blue signal dips at point 14?');
%   disp('That does not make sense.');
%   disp('The problem is that the arrays were not cleared,');
%   disp(' so point 14 and beyond is old data.');

%OG = 1.090; %1.117; %1.1195; %1.117; % OG;
FG = 1.030; %1.0525; %1.075; % FG;
% Convert OG and FG to Brix
x = grav2brix(OG);

i=1;
c = [ 1.001843, 0.002318474, 0.000007775, 0.000000034, 0.00574, 0.00003344, 0.000000086 ];
while (FG < OG)
    y = grav2brix(FG);
    %disp(sprintf('With OG %6.3f, or %4.1f Brix,', OG, x));
    %disp(sprintf(' and FG %6.3f, or %4.1f Brix,', FG, y));
    % w = c(1) - c(2) * x - c(3) * x^2 - c(4) * x^3 + c(5) * y + c(6) * y^2 + c(7) * y^3;
    w(i) = c(1) - c(2) .* x - c(3) .* x.^2 - c(4) .* x.^3 + c(5) .* y + c(6) .* y.^2 + c(7) .* y.^3;
    %disp(sprintf(' the corrected Refractometer reading is %6.3f', w));
    
    % This is from
    % https://seanterrill.com/2011/04/07/refractometer-fg-results/
    % a blog by Sean Terrill, who seems to have already solved this problem.
    d = [1.0000, -0.0044993, 0.00027581, -0.0000072800,   0.011774, -0.0012717, 0.000063293];
    v(i) = d(1) + d(2) .* x + d(3) .* x.^2 + d(4) .* x.^3 + d(5) .* y + d(6) .* y.^2 + d(7) .* y.^3;
    %disp(sprintf(' the corrected Refractometer reading (Terrill) is %6.3f', v));
    
    FGreadings(i) = FG;
    FG = FG + 0.005;
    i = i + 1;
end

% show the OG readings as a line
OGreadings(1:length(w)) = OG;
lowestMin = min([ min(FGreadings), min(w), min(v) ]);
plot(1:length(w), w, 'b');
hold('on');
plot(1:length(v), v, 'r');
plot(1:length(FGreadings), FGreadings, 'm');
plot(1:length(OGreadings), OGreadings, 'g');
title('FG corrections blue, Terrill method in red, OG:green, uncorrected readings:purple');
axis([1 length(v) lowestMin (OG + 0.01) ]);

