% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_10_3.m

    [x, fs] = audioread('flute1.wav');
    audiowrite('flute1.ogg', x, fs);
