% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% if_example2.m
%
%
    userSays = input('Enter f, s, or q: ', 's');

    if (userSays == 'f')
        disp(' flag');
    elseif (userSays == 's')
        disp(' step');
    elseif (userSays == 'q')
        disp(' quit');
    else
        disp('not valid');
    end
