% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_2_5.m

    side_len = 100;
    x= 0:0.01:50;
    volume = (side_len - 2*x) .* (side_len - 2*x) .* x;
    plot(x, volume)

    [value, index] = max(volume);

    disp(x(index))
