% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_10_1.m

    [x, fs] = audioread('piano1.wav');
    sound(x, fs)
