% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% mysum_example1.m

    A = [45, 21, 33, 9, 17];
    mysum = 0;
    k = 1;
    while (k <= length(A))
        mysum = mysum + A(k);
        k = k + 1;
    end
    disp(mysum)

