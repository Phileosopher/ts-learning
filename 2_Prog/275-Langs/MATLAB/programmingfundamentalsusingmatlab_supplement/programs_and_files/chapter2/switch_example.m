% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% switch_example

    b = input('enter a number ');

    switch b
        case 1
            disp('one');
        case 2
            disp('two');
        case 3
            disp('three');
        otherwise
            disp('not one, two, or three');
    end

