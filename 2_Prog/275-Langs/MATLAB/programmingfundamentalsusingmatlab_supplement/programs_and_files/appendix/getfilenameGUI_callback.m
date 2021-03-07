% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
    % getfilenameGUI_callback.m
    % Callback for a get filename
    %
    function getfilenameGUI_callback(object, ignoreme, num)

    global fname 
    global fighandle

    if (num == 1)
        % filename is set
        fname = get(object, 'String');
    else
        % button is pressed
        try
            load(fname);
            % x = imread(fname);
            plot(mydata);
            set(fighandle, 'Color', [0, 1, 0]); % green
        catch
            disp('File does not exist');
            set(fighandle, 'Color', [1, 0, 0]); % red
        end
    end
    
    
    


