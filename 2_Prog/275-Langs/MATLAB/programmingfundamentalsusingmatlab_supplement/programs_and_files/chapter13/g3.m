% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% 
% A simple function
% 
%
% f = @g3;
% integral(f, 0, 10)
%
% Usage:
%    g3(n)  % where n is some real value

function result = g3(x) 

% result1 only has non-zero values from 0 to whatever
result1 = (x >= 0) * 5;

% define x2 to be 0.0001 any place where x is 0
x2 = (x == 0) .* 0.0001;
% Now redefine x to be 0.0001 wherever it was 0.
x = x + x2;
% result2 should not have a NaN value
result2 = sin(x)./x;

% Add the two results, to return.
result = result1 + result2;

