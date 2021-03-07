% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Experiment with closereq
%

    figHandle = figure;
    disp('The default close function is:');
    disp(get(figHandle, 'CloseRequestFcn'));
    buttonHandle = uicontrol(figHandle, ...
        'Style', 'pushbutton', ...
        'String', 'Close', ...
        'Position', [40 40 50 20], ...
        'Callback', 'close');
    set(figHandle, 'CloseRequestFcn', @ex_closereqCB)


