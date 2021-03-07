% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_7_1.m

    % function rsum = recursive_sum(n)
    function rsum = program_7_1(n)
    
    if (n <= 1)
        % If we get bad input, like -1, this will give a bad result
        % but it will work.
        rsum = 1;
    else
        % rsum = n + recursive_sum(n-1);
        rsum = n + program_7_1(n-1);
    end
