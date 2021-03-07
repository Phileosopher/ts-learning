% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
    % ThreeIn3Out.m
    function [a, b, c] = ThreeIn3Out(x,y,z)
    a = (x + y + z)/3;   % average
    b = (x + y + z);     % sum
    c = sqrt(x^2 + y^2 + z^2);   % sqrt sum squared
