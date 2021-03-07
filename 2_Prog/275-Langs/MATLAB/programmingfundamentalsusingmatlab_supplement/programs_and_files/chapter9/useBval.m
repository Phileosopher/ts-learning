% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% useBval
%
% Use a Boolean value set by another callback.
% See callback_bug.m
%
%
% Usage:
%    This is a callback function, so you should not run it directly.

function useBval(object, eventdata)

% global main_figure
global Bval

if (Bval)
    disp('Variable Bval is true. Resetting it to false.');
    Bval = false;
else
    disp('Variable Bval is false.');
end


