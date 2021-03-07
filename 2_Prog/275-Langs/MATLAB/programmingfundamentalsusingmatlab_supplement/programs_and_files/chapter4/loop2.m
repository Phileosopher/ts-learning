% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% This example gets the elapsed time for a calculation using an array.
for i=1:10
    tic
    x = 1:900;
    g = 2*x.^2 + 5*x - 3;
    toc
    clear
end
