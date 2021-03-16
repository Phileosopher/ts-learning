% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% pascal3.m
%
% Make a Pascal's triangle.
%
%
% Usage:
%   pascal3(iterations)
%
% Example:
%   pascal3(10)
%

function pascal3(iterationsString)
%iterations = 21;
iterations = str2num(iterationsString);

% iterations should be an odd number.
if (mod(iterations, 2) == 0)
    % This number is even, so make it odd.
    iterations = iterations + 1;
end

% p = pascal(iterations);

q = zeros(iterations, iterations);
% start = round(iterations/2);
q(1,1) = 1;
% q(2,1) = q(1,1);
% q(2,2) = q(1,1) + q(1,2);
% 
% q(3,1) = q(2,1);
% q(3,2) = q(2,1) + q(2,2);
% q(3,3) = q(2,2) + q(2,3);

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
for row=1:iterations
    str = '';
    for col=1:iterations
        % Add a character to the string.
        % The character is chars2print(index), 
        % where index is 1..chars2printLength.
        str = strcat(str, sprintf('%c', chars2print(p(row, col))));
    end
    disp(str);
end


