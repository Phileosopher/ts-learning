% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% correctRefract.m
%
% This program uses two different formulas to correct the gravity
% of a refractometer reading after fermentation.
%
% Note that this program uses grav2brix.m, and
% that uses Brix2SPGTable_v2.m, which has an error in one of the data points. 
%   I wrote some text that discusses this, and I do not want to 
% replace Brix2SPGTable_v2. 
%   This data error PROBABLY does not affect this program. 
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

OG = 1.117; %1.1195; %1.117; % OG;
FG = 1.0525; %1.075; % FG; 
% Convert OG and FG to Brix
x = grav2brix(OG);
y = grav2brix(FG);
disp(sprintf('With OG %6.3f, or %4.1f Brix,', OG, x));
disp(sprintf(' and FG %6.3f, or %4.1f Brix,', FG, y));

c = [ 1.001843, 0.002318474, 0.000007775, 0.000000034, 0.00574, 0.00003344, 0.000000086 ];
% w = c(1) - c(2) * x - c(3) * x^2 - c(4) * x^3 + c(5) * y + c(6) * y^2 + c(7) * y^3;
w = c(1) - c(2) .* x - c(3) .* x.^2 - c(4) .* x.^3 + c(5) .* y + c(6) .* y.^2 + c(7) .* y.^3;
disp(sprintf(' the corrected Refractometer reading is %6.3f', w));

% This is from
% http://seanterrill.com/2011/04/07/refractometer-fg-results/
% a blog by Sean Terrill, who seems to have already solved this problem.
d = [1.0000, -0.0044993, 0.00027581, -0.0000072800,   0.011774, -0.0012717, 0.000063293];
v = d(1) + d(2) .* x + d(3) .* x.^2 + d(4) .* x.^3 + d(5) .* y + d(6) .* y.^2 + d(7) .* y.^3;
disp(sprintf(' the corrected Refractometer reading (Terrill) is %6.3f', v));

