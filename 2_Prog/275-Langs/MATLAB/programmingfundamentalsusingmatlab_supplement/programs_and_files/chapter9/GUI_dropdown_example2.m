% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% GUI_dropdown_example2.m
%
% Show an example with a drop-down menu, working with a callback function.
% This example DOES WORK when the callback attempts to change
% a variable that is normally out of its scope, since the variable is
% made global. 
%
%

global current_choice

disp('This example does work.');

fig_handle = figure();

current_choice = 'red';

handle1 = uicontrol('Style', 'popup', ...
    'String', 'red|green|blue', ...
    'Position', [250 200 100 50], ...
    'Callback', {'GUI_dropdown_CB2', 'hello'});


