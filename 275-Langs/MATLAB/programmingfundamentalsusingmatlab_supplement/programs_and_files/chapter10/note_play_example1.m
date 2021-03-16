% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% note_play_example1.m
%
% Generate a sine wave for 1 second's worth of data
% for the notes 220 Hz.
%
% This program plays this note.
%
%

% Default is 8192 samples per second
% Alternatively, use sound(s,8192)
fs = 8192;

% middle-C is 261.6
% note = 220;
note = 261.6;

% pre-allocate the memory (not necessary)
%mynote = zeros(1, fs);
% For the note, store the data in one row.
% 0.5 is used to keep the sound from being loud
mynote = 0.5 * sin(2 * pi * note * (0:(fs-1))/fs);

% Play the note
sound(mynote, fs)

