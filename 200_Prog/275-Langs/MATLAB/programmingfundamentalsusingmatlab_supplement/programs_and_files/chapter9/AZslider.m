% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% AZslider.m
%
% Show a slider-bar to select a letter from A to Z.
%
% Usage:
%    AZslider

fh = figure();

% Make these global to communicate with callback
global letter
global tx

letter = 'A';

tx = uicontrol('Parent', fh, ...
    'Style', 'text', 'String', letter);
set(tx, 'Position', [250, 100, 100, 50]);

sl = uicontrol('Parent', fh, ...
    'Style', 'slider');
set(sl, 'Position', [150, 100, 100, 50]);
set(sl, 'Callback', {'AZslider_callback'});
set(sl, 'MAX', 25);
set(sl, 'SliderStep', [1 0.1]);

