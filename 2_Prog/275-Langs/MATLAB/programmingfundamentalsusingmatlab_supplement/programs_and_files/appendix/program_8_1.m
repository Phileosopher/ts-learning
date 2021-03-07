% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_8_1.m

    x = imread('redBottleCap3.jpg');
    figure();
    imshow(x);
    % Convert to grayscale
    y = rgb2gray(x);
    figure();
    imshow(y);
