% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% 
% A simple function
% 
%
% f = @g2;
% integral(f, -100, 100)
%
% Usage:
%    g2(n)  % where n is some real value

function result = g2(x) 

result = ((x >= 0) & (x < 5)) * 2;


