% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_4_7.m

    % Create an example image
    N = 200;
    x = 255*ones(N, N, 'uint8');
    s = floor(99*sin(2*pi*(1:N)/N) + 100);
    for k=1:N
        x(floor(s(k)), k) = 0;
    end
    % Now x is a black sinusoid on a white background.

    % First, copy x to y
    y = x; 
    for k=1:N
        % Copy the columns of x to the rows of y
        y(k+1:end, k) = x(k, k+1:end);
    end
    % Show the result
    imshow(y);
