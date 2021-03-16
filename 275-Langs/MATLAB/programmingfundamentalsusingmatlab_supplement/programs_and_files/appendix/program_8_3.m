% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_8_3.m

    x = imread('redBottleCap3.jpg');
    y = rgb2gray(x);
    edges1 = edge(y, 'canny');
    edges2 = edge(y, 'log');
    edges3 = edge(y, 'prewitt');
    edges4 = edge(y, 'sobel');
    % Show the results
    figure();
    subplot(2, 2, 1);
    imshow(edges1);
    title('Canny');
    subplot(2, 2, 2);
    imshow(edges2);
    title('Laplacian of Gaussian');
    subplot(2, 2, 3);
    imshow(edges3);
    title('Prewitt');
    subplot(2, 2, 4);
    imshow(edges4);
    title('Sobel');
