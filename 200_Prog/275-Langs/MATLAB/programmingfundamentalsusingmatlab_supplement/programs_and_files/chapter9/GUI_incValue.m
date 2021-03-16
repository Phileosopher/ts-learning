% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Simple function to increment a value.
%

function GUI_incValue()

global value

value = value + 1;
disp(sprintf('value now is %d', value));

