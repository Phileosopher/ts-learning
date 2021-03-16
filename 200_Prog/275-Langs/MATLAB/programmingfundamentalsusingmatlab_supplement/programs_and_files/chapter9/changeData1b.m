% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
    % changeData1b.m
    %
    % Use with:
    %     myvalue = 1;
    %     handle1 = uicontrol('Style', 'pushbutton', ...
    %         'String', 'Inc myvalue', ...
    %         'Position', [225 200 100 50], ...
    %         'Callback', @changeData1b);
    %
    % This does not work, but is used to demonstrate that point.

    function changeData1b(uihandle, future)

    myvalue = myvalue + 1;
    disp(sprintf('myvalue is %d', myvalue));

