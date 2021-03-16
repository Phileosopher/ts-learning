% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% 
% A simple function
% 
%
% f = @g;
% integral(f, -100, 100, 'ArrayValued', true)
%
% Usage:
%    g(n)  % where n is some real value

function result = g(x) 

if (x < 0)
    result = 0;
elseif (x >= 5)
    result = 0;
else
    result = 2;
end

