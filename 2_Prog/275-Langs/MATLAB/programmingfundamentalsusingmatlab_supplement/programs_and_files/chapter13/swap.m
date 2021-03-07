% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% swap.m
%
% Given an array and two indices,
% return the array with the values at those
% two positions swapped.
% 
% Example:
%    swap(1:5, 3, 4)
%    returns  1, 2, 4, 3, 5
%
%

function myarray = swap(myarray, index1, index2)

assert(index1 <= length(myarray));
assert(index2 <= length(myarray));

tempValue = myarray(index1);
myarray(index1) = myarray(index2);
myarray(index2) = tempValue;
