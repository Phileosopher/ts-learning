% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% AZslider_callback.m
%
% Callback for slider that selects A..Z
%
% Usage:
%   This is a callback function. See AZslider instead.
%

function AZslider_callback(object, ignore) 

global letter 
global tx

V = round(get(object, 'Value'));
letter = 'A' + V;

s = sprintf('%c',letter);
disp(s);

set(tx, 'String', s);


