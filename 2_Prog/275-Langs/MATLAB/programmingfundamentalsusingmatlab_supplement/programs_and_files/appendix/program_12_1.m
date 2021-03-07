% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_12_1.m

    x = csvread('BB133temps.csv');
    plot(x(:,1),'b')
    hold on
    plot(x(:,2),'g')

    % Find the error
    y = x(:,1) - x(:,2);
    figure();
    plot(y, 'r');

    err_sum(1) = y(1);
    for k=2:length(y)
        err_sum(k) = err_sum(k-1) + y(k);
    end
    avgerr = err_sum./(1:length(y));
    plot(avgerr); 
