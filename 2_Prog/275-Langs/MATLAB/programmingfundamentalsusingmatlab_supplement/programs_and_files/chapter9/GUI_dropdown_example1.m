% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% GUI_dropdown_example1.m
%
% Show an example with a drop-down menu, working with a callback function.
% This example DOES NOT WORK, since the callback attempts to change
% a variable that is out of its scope. 
%
%

disp('This example does NOT work.');

fig_handle = figure();

current_choice = 'red';

handle1 = uicontrol('Style', 'popup', ...
    'String', 'red|green|blue', ...
    'Position', [250 200 100 50], ...
    'Callback', {'GUI_dropdown_CB1', 'hello'});


