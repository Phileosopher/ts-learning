% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% Show how clf differs from close.

fig_handle = figure();
text_handle1 = uicontrol('Parent', fig_handle, ...
    'Style', 'text', ...
    'String', 'Wait 5 seconds', ...
    'Position', [30 100 100 100]);
pause(5);
clf(fig_handle)
pause(5);
close(fig_handle)

