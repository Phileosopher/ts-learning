% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_4_9.m

    % Create an example image
    N = 200;
    x = 255*ones(N, N, 'uint8');
    s = floor(99*sin(2*pi*(1:N)/N) + 100);
    for k=1:N
        x(floor(s(k)), k) = 0;
    end
    % Now x is a black sinusoid on a white background.
    % To reverse the image values, use 255 minus the original.
    y = 255 - x;
    % Show the result
    imshow(y);
