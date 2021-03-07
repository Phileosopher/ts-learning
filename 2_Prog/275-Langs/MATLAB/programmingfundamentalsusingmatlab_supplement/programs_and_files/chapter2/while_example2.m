% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% while_example2.m

    k=1;
    while (k < 0)
        disp('This is never displayed.');
        k = k + 2;
    end

