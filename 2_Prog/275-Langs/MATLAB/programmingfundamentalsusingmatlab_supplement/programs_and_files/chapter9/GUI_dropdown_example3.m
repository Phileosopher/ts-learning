% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% GUI_dropdown_example3.m
%
% Show an example with a drop-down menu, working with a callback function.
% This example DOES WORK when the callback attempts to change
% a variable that is normally out of its scope, since the variable is
% accessed and reassigned using "evalin" and "assignin".
%
% This is an interesting MATLAB feature, though I consider it poor 
% programming practice. Using global variables is best avoided when
% possible, but I think using global variables is a better solution.
% This is because "evalin" is a powerful command, like "eval", that
% can have unexpected consequences if not used properly.
%
%

disp('This example does work.');

fig_handle = figure();

current_choice = 'red';

handle1 = uicontrol('Style', 'popup', ...
    'String', 'red|green|blue', ...
    'Position', [250 200 100 50], ...
    'Callback', {'GUI_dropdown_CB3', 'hello'});


