% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_8_5.m
    % See also blue_image.m

    v = imread('redBottleCap3.jpg');
    x = rgb2gray(v);
    imshow(x);
    [mousex, mousey] = ginput(1);
    r = round(mousey);
    c = round(mousex);
    % Set the neighbors blue, too
    y = blue_image(x, r, c);
    % Show the result
    imshow(y);
