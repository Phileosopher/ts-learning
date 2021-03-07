% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% grav2brix_approx.m
%
% Given a SPG reading, convert it to degrees Brix.
% This uses a line to approximate the conversion.
% But the relation is NOT EXACTLY a line, so this simple method
% is not precise.
%
% See also   grav2brix.m
%
%
%
% Usage:
%   grav2brix_approx(1.052)

function Brix = grav2brix_approx(SPG)

if ((SPG < 1.000) || (SPG > 1.130))
    disp('grav2brix: Expecting an SPG value between 1.000 and 1.130.');
    disp('Results may not be accurate.');
end
m = 23.49 / 0.0990;
b = -237.0404;
% b = -237.9682;
% m = 29.12/0.126
Brix = SPG * m + b;


