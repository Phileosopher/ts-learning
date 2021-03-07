% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% assert_example.m
%
% Example of the assert command.
% 
% Usage:
%     assert_example(1);
%
function assert_example(n)

assert(n < 100);
assert(n > 0);

disp('The value is OK.');
