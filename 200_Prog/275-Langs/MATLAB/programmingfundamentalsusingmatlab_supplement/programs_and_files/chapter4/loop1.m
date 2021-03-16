% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% This example gets the elapsed time for a calculation in a for loop.
for i=1:10
    tic
    for x = 1:900
        g(x) = 2*x^2 + 5*x - 3;
    end 
    toc
    clear
end
