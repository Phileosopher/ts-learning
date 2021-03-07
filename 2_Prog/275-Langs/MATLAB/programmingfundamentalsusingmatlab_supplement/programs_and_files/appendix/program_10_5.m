% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_10_5.m

    [x, fs] = audioread('piano1.wav');
    sound(x, fs);
    plot(x);
    pause

    plot(x(450000:end,1));
    sound(x(1:450000), fs);
    audiowrite('piano1b.ogg', x(1:450000), fs);
