% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 


    f = @(x) sin(x) ./ x;
    x = 0.001:0.1:1000;
    fx = f(x);
    N = length(fx);  % 10000;
     
    % slow way:
    clear mysum
    tic
    for last=1:length(fx)
        mysum(last) = sum(fx(1:last));
    end
    toc 
    plot(x, mysum/10)

    % fast way:
    clear mysum
    tic 
    mysum(1) = fx(1);
    for last=2:length(fx)
        mysum(last) = mysum(last-1) + fx(last);
    end
    toc 
    plot(x, mysum/10)

