% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% mysum_example2.m

    A = [45, 21, 33, 9, 17];
    mysum = 0;
    for k=1:length(A)
        mysum = mysum + A(k);
    end
    disp(mysum)

