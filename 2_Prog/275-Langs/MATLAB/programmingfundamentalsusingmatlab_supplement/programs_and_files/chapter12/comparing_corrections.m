% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% comparing_corrections.m
%
% Given two gravities, an original and a final one,
% figure out which correction formula.
%   bestOG should be a reliable measurement
%   bestFG when it comes from a refractometer, it needs to be adjusted
%
%
% Usage:
%   comparing_corrections(bestOG, bestFG)
%
% Example:
%   comparing_corrections(1.050, 1.030)
%
function [bestFG] = comparing_corrections(bestOG, bestFG)

    x = grav2brix(bestOG);
    y = grav2brix(bestFG);
    c = [ 1.001843, 0.002318474, 0.000007775, ...
       0.000000034, 0.00574, 0.00003344, 0.000000086 ];
    d = [ 1.0000, -0.0044993, 0.00027581, ...
       -0.0000072800,  0.011774, -0.0012717, 0.000063293 ];
    % Could also use the ^ operator
    w = c(1) - c(2) * x - c(3) * x * x - c(4) * x * x * x ...
           + c(5) * y + c(6) * y * y + c(7) * y * y * y;
    v = d(1) + d(2) * x + d(3) * x * x + d(4) * x * x * x ...
           + d(5) * y + d(6) * y * y + d(7) * y * y * y;
    s1 = strcat('Refractometer reading corrected', ...
        ' (formula from HomeBrewStuff.com) is ');
    disp(sprintf('%s %7.4f ', s1, w));
    s2 = strcat('Refractometer reading corrected', ...
        ' (formula from SeanTerrill.com) is ');
    disp(sprintf('%s %7.4f ', s2, v));
    if (v < w) 
        % v Seems OK
        bestFG = v;
    else 
        % v is too large! So use w instead.
        bestFG = w;
    end
    disp(sprintf('Using %7.4f ', bestFG));

