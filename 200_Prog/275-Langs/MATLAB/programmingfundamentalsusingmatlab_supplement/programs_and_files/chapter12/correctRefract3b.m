% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%  correctRefract3b.m
%
%  This program shows an example bug.
%  The problem is about the data -- we define it to be one length, then
%  re-run a program that re-defines it. When plotted, we see a jump in the
%  line that should not be there. Everything past the sudden jump is old data.
%
%
% Usage:
%   correctRefract3b
%   % Enter 100
%   correctRefract3b
%   % Enter  80
%

x = input('Please enter a number higher than 30: ');
i = 1;
% To fix the problem, uncomment the next line.
% clear w   
for y = 30:5:x
    w(i) = x - y;
    i = i + 1;
end
plot(1:length(w), w, 'b');
% This way would not have the problem:
%v = x - (30:5:x);
