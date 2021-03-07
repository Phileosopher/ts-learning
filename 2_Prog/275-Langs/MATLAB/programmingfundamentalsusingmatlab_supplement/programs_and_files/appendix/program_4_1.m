% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_4_1.m

    % Sort matrix x along row 1
    %
    % First, define x
    x = [ 3.32 2.91 2.55 2.55 2.95;
          1    2    3    4    5     ];
    % Build a new matrix, x2
    % copy row 1 to a new variable
    y = x(1, :);
    % Remember the largest value, to use as a replacement
    largest = max(y) + 1; % Make it larger than the largest
    n = 1; % index for sorted array
    % Find the smallest value, note where it is, replace
    % it with something larger than the largest.
    % Repeat for every value in the array
    for k = 1:length(y)
        % What is the smallest value?
        [v, loc] = min(y);
        % Remember where it is
        sorted_cols(n) = loc;
        n = n + 1;
        % Replace the smallest value with largest
        y(loc) = largest;
    end
    
    disp('After sorting to preserve row 2:');
    % sorted_cols now has the order of the columns
    newx = [x(1, sorted_cols);
        sorted_cols]
