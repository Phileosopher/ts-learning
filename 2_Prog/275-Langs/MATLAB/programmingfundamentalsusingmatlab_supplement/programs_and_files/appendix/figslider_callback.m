% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% Callback function for a GUI with 2 sliders for an image

    function figslider_callback(object, ignoreme, num)
    global x;
    global startR;
    global startC;
    % global stopR;
    % global halfR;
    % global halfC;
    global MAXR;
    global image_handle;
   
    % disp('get object');
    % get(object)
 
    V = round(get(object, 'Value'));
    % disp(V);
    if (num == 1)
        disp(sprintf('Changing startC from %d to %d', startC, (V+1)));
        startC = V + 1;
    else
        disp(sprintf('Changing startR from %d to %d', startR, (V+1)));
        startR = V + 1;
        % Turn this value around:
        %disp(sprintf('Changing stopR from %d to %d', stopR, MAXR - (V+1)));
        % stopR = MAXR - (V + 1);
    end
    axes(image_handle);
    % disp(sprintf('stopR is %d', stopR));
    % imshow(x(stopR-200:stopR, startC:startC+200, :));
    imshow(x(startR:startR+200, startC:startC+200, :));

