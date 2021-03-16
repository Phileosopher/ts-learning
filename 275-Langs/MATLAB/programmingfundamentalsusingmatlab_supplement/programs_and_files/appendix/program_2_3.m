% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_2_3.m

    n = 1; % initial, non-zero value
    clear mylist; % In case we already have this defined
    next_index = 1;
    while (n ~= 0)
        n = input('Enter a number, or 0 to exit: ');
        
        if (n ~= 0)
            % Add it to the list
            mylist(next_index) = n;
            next_index = next_index + 1;
            % Print some statistics
            disp(sprintf('Sum is %5.2f', sum(mylist)));
            disp(sprintf('Mean is %5.2f', mean(mylist)));
            disp(sprintf('Median is %5.2f', median(mylist)));
            disp(sprintf('Variance is %5.2f', var(mylist)));
        end
    end 
