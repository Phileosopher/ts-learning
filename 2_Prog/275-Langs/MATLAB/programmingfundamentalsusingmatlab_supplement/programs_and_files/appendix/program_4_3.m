% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_4_3.m

    %
    % Given an array of numbers, output an array that 
    % only contains the ones that are repeated.
    %
    % For example, [4, 7, 2, 3, 2, 4, 2, 5] should 
    % return [4, 2, 2, 4, 2].
    function outArray = noUnique(inArray)

    % Initialize output array
    outArray = [];

    for k=1:length(inArray)
        if (isUnique(inArray(k), inArray))
            outArray = [outArray, inArray(k)];
        end
    end

    % Determine if the value appears more than once
    % in the array
    function moreThanOnce = isUnique(value, array)

    % Count the number of times value appears in array.
    EqCount = sum(value == array);

    moreThanOnce = (EqCount > 1);
