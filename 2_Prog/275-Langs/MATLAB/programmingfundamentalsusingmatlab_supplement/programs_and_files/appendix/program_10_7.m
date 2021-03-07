% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_10_7.m

    audioObject = audiorecorder(8000, 16, 1);
    record(audioObject); pause(3); pause(audioObject);
    play(audioObject);

    audioData = getaudiodata(audioObject);
    audiowrite('speaking1.ogg', audioData, 8000);
