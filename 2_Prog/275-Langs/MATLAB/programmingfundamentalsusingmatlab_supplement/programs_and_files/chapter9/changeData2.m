% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
    % changeData2.m
    %
    % Use with:
    %     global myvalue;
    %     myvalue=1;
    %     handle1 = uicontrol('Style', 'pushbutton', ...
    %         'String', 'Inc myvalue', ...
    %         'Position', [225 200 100 50], ...
    %         'Callback', @changeData2);
    %
    % 
    function changeData2(uihandle, future)

    global myvalue;
    myvalue = myvalue + 1;
    disp(sprintf('myvalue is %d', myvalue));

    % disp(sprintf('handle is %d', uihandle));
    % The callback must not be "'Callback', 'changeData2'",
    % or the above access to uihandle will fail.


