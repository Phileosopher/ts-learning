% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Count down from 10 to 0 seconds
%

    fig_handle = figure();
    count_handle1 = uicontrol('Parent', fig_handle, ...
       'Style', 'text', ...
       'String', 'X', ...
       'FontSize', 50, ...
       'Position', [100 200 100 100]);
    for count = 10:-1:1
        set(count_handle1, 'String', sprintf('%d', count));
        pause(1);
    end
    set(count_handle1, 'String', '0');
    set(fig_handle, 'Color', [0.5 0.1 0.1]);

