% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
    % Determine if the value appears more than once
    % in the array
    function moreThanOnce = isUnique(value, array)

    % Count the number of times value appears in array.
    EqCount = sum(value == array);

    moreThanOnce = (EqCount > 1);
