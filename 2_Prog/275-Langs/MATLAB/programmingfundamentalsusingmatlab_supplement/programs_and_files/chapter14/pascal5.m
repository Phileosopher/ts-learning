% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% pascal5.m
%
% Make a Pascal's triangle.
% Optional argument "iterations" gives the number of outputs.
% This version is almost identical to pascal4, except for an animated graph.
%
%
% Usage:
%   pascal5(iterations)
%
% Example:
%   pascal5()
%   pascal5('11')
%

function pascal5(varargin)

% Get the number passed, or use a default value.
if (nargin >= 1)
    iterationsString = varargin{1};
    iterations = str2num(iterationsString);
else 
    iterations = 21;
end

% iterations should be an odd number.
if (mod(iterations, 2) == 0)
    % This number is even, so make it odd.
    iterations = iterations + 1;
end

% Allocate the matrix memory
q = zeros(iterations, iterations);

% Put in the initial value
q(1,1) = 1;
% Here are a few of the next values, to show the pattern.
% q(2,1) = q(1,1);
% q(2,2) = q(1,1) + q(1,2);
% 
% q(3,1) = q(2,1);
% q(3,2) = q(2,1) + q(2,2);
% q(3,3) = q(2,2) + q(2,3);

% Populate the matrix q 
% Every q(row,col) value is q(row-1, col-1) + q(row-1, col),
% i.e. the sum of the value in the row above, and above-left
for row=2:iterations
    q(row,1) = q(row-1, 1);
    for col=2:iterations
        % disp(sprintf('q(%d, %d) = q(%d, %d) + q(%d, %d)', ...
        %     row, col, row-1, col-1, row-1, col));
        q(row, col) = q(row-1, col-1) + q(row-1, col);
    end
end

% Now map the numbers to lower-case letters.
chars2print = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
chars2printLength = length(chars2print);
% Make a new matrix with just the values we can print.
% p will be the same as q, for small values.
p = mod(q, chars2printLength) + 1;

% % This is an alternate way to show the data.
figure();
hold on;
colorArray = 'bgrkmcy';
for row=1:iterations
    % Make a colorIndex by mapping the row to one of the 
    % colorArray characters.
    colorIndex = mod(row, length(colorArray)) + 1;
    bar(1:iterations, p(row,:), colorArray(colorIndex));
    % plot(1:iterations, p(row,:), colorArray(colorIndex));
    pause(1);
end
title('Bar chart showing each iteration in a different color');

% Output the data graphically. 
%figure();
%mesh(1:iterations, 1:iterations, p);

