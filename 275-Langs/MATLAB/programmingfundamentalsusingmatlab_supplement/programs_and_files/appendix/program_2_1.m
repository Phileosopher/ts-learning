% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_2_1.m

    % function [y,z] = SortTwo(a,b)
    function [y,z] = program_2_1(a,b)
        
        if (a < b)
            y = a; % a,b in order already
            z = b;
        else
            y = b; % copy in order
            z = a;
        end
    end % This last end is not required for a function
