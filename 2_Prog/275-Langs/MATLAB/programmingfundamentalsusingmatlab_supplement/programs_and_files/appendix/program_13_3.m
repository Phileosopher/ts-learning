% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_13_3.m

    a = rand(1, 1000000);
    t = zeros(1, 10);
    for k=1:10
        tic; 
        c = fft(a); 
        t(k) = toc;
    end

    t1 = sum(t)/10;
    disp(t1)

    op1 = 19931568;
    op2 = 1000000 ^ 2;
    t2 = t1 * op2 / op1;
