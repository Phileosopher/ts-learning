% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% callback_good.m
%
% This demonstrates a problem with a callback function.
% The original problem was in a complex set of programs with 
% 21 different files.
% This version keeps the bug, but scales it down to the bare minimum.
% callback_bug.m shows the problem; callback_good.m shows what it should do.
% 
%
% Usage:
%   callback_good
%   

function callback_good() 

global Bval

Bval = false;

main_figure = figure();

copyButton_handle = uicontrol('Parent', main_figure, ...
    'Style', 'pushbutton', ...
    'String', 'Use Bval', ...
    'Position', [50 100 100 60], 'Callback', 'useBval');
%   'Position', [X YfromBottom width height]
copyButton2_handle = uicontrol('Parent', main_figure, ...
    'Style', 'pushbutton', ...
    'String', 'set Bval to true', ...
    'Position', [50 200 100 60], ...
    'Callback', 'global Bval;Bval=true;');

%   'Callback', 'Bval=true;');

