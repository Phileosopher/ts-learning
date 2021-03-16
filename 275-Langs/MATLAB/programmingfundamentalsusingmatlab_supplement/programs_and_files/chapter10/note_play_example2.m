% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% note_play_example2.m
%
% Generate sine waves with 1 second's worth of data
% for notes from 220 Hz to 440 Hz.
%
% This program plays these notes in sequence,
% then plays some of them randomly.
%
%

% Default is 8192 samples per second
% Alternatively, use sound(s,8192)
fs = 8192;

% notes from A to A (next octave)
% A4 is 440 Hz, middle-C is 261.6
% A A# B C C# D D# E F F# G G# A
% 
notes = [220, 233, 247, 262, 277, 294, 311, ...
    330, 349, 370, 392, 415, 440];

% pre-allocate the memory
% allnotes = zeros(length(notes), fs);  % not really needed
% For each note, store the data in a row's matrix.
for k=1:length(notes)
    % store this note
    % 0.5 is used to keep the sound from being loud
    allnotes(k, 1:fs) = 0.5 * sin(2 * pi * notes(k) * (0:(fs-1))/fs);
end

% Play the notes in sequence
for k=1:length(notes)
    sound(allnotes(k,1:fs))
    pause(1);
end

% Play a random set of 10 notes
r = ceil(rand(1,10)*length(notes));
for k = r
    % Play a random note
    sound(allnotes(k,1:fs));
    % Wait only half a second, to overlap notes
    pause(0.5);
end
