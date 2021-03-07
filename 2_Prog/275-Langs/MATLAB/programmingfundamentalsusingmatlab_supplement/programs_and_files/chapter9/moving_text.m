% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 

fig_handle = figure;
set(fig_handle, 'KeyPressFcn', 'keypress_cursors');

global x y hndl

x = 135;
y = 380;

hndl = uicontrol(fig_handle, ...
    'Style', 'text', ...
    'String', 'Moving with Arrow Keys', ...
    'FontSize', 20, ...
    'Position', [x, y, 300, 24]);
