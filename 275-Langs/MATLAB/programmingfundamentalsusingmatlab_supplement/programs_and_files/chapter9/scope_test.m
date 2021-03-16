% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% scope_test.m
%
% See what variables are defined.
%
%

function scope_test(x)

y = 2;
whos
a = a + 1;   % This causes an error
