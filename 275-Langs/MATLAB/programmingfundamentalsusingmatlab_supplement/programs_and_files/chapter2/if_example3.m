% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% if_example3.m
%
%
    userSays = input('Enter f, s, or q: ', 's');
    switch userSays
        case ('f')
            disp(' flag');
        case ('s')
            disp(' step');
        case ('q')
            disp(' quit');
        otherwise
            disp('not valid');
    end
