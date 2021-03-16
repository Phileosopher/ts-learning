% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
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

