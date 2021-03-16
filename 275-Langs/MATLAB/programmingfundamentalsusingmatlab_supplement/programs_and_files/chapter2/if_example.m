% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% if_example.m
%
%
    userSays = input('Enter f, s, or q: ', 's');

    if (userSays == 'f')
        disp(' flag');
    else if (userSays == 's')
            disp(' step');
        else if (userSays == 'q')
                disp(' quit');
            else
                disp('not valid');
            end
        end
    end
