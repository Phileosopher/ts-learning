% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Simple function to increment a counter.
%

function GUI_incCount()

global count 

count =  count + 1;
disp(sprintf('count now is %d', count));

