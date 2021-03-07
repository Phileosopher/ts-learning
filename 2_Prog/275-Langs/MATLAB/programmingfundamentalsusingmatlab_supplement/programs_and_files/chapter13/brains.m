% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% brains.m is a program to find a solution
% to a puzzle from Futurama.
% The story goes like this: two people switch brains with the aid of a
% a machine, then realize that they cannot switch back.
% Supposedly, with two more people, they can switch brains
% between people and end up back in the original bodies.
%
% To represent this, we have an array. The "body" of the individual
% is given by the index, while the "brain" is given by the number.
% Initially, we start this with 2, 1, 3, 4, ..., representing
% the condition that people 1 and 2 have switched brains.
%
%


b = [2, 1, 3, 4]  % create our initial state of brains in bodies
% Where the body is given by the array index, and the brain
% might be switched from one person to another.

% Keep a record of where we have switched.
switchHistory = [1, 1, 0, 0];

% switch two brains
x = 1;
y = 2;
temp = b(x);
b(x) = b(y);
b(y) = temp

% Mark in an expanding matrix which ones have switched.
% Once 2 bodies switch brains, they cannot directly switch back.
[ROWS, COLS] = size(swicthHistory);
switchHistory(ROWS+1, :) = [0, 0, 0, 0];
switchHistory(ROWS+1, x) = 1;
switchHistory(ROWS+1, y) = 1;
% switchHistory is not fully implemented

                                 % Physical location is body,
                                 % number means brain,
                                 % * means switch (to get next row).
                                 % 1* 2* 3  4 
b = switch2brains(b, 2, 3)       % 2  1* 3* 4
b = switch2brains(b, 1, 4)       % 2* 3  1  4*
b = switch2brains(b, 1, 3)       % 4* 3  1* 2
b = switch2brains(b, 2, 4)       % 1  3* 4  2*
b = switch2brains(b, 3, 4)       % 1  2  4* 3*
                                 % 1  2  3  4

% Given the list and two brains, switch them.
function newlist = switch2brains(currentList, body1, body2)

newlist = currentList;
temp = newList(body1);
newList(body1) = newList(body2);
newList(body2) = temp;

