% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_4_5.m

    % Create an example image
    N = 200;
    x = 255*ones(N, N, 'uint8');
    s = floor(99*sin(2*pi*(1:N)/N) + 100);
    for k=1:N
        x(floor(s(k)), k) = 0;
    end
    % Now x is a black sinusoid on a white background.
    % Create a new image, y, as x reversed along rows
    % (columns in reversed order)
    % This forms a mirror image along the right edge.
    y = x(1:N, N:-1:1);
    % We can put these together, and
    % form a new matrix of twice the width
    z = 255*ones(N, 2*N, 'uint8');
    % copy x, then y
    z(1:N, 1:N) = x;
    z(1:N, N+1:N+N) = y;
    % Show the new image to verify 
    imshow(z)
