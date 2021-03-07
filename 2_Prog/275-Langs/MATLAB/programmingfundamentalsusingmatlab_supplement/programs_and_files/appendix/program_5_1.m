% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_5_1.m

    input_str = '1 - 2, 4 - 1, 1 - 7, 1 - 3, 1 - 8, 2 - 2, 1 - 7';
    
    % Find the numbers in the string as an array. There are
    % more compact solutions, but should be easy to follow.
    % Make note of the commas and dashes in the input.
    digits = ((input_str >= '0') & (input_str <= '9'));
    count = 1;
    k = 1;
    % Simple way to loop until we've processed 
    % all digits in input
    while (sum(digits(k:end)) > 0)
        % Find the first 1 (digit)
        while ((k <= length(digits)) && (digits(k) ~= 1))
            k = k + 1;
        end
        start = k;
        % Find the next 0 (meaning end of this digit sequence)
        while ((k <= length(digits)) && (digits(k) ~= 0))
            k = k + 1;
        end
        stop = k - 1;
        % Now start, stop define the substring holding a number.
        numbers(count) = str2double(input_str(start:stop));
        count = count + 1;
    end
    
    % Now we have an array, numbers, that contains all values 
    % from input. Assume first is value, second is repetitions,
    % third is value, fourth is repetitions...
    count = 1; % re-use this for a different purpose
    for k=1:floor(length(numbers)/2)
        mystruct.value = numbers(count);
        count = count + 1;
        mystruct.repetitions = numbers(count);
        count = count + 1;
        runlengths(k) = mystruct;
    end
    
    % Finally, print it to make sure it's correct
    disp('Original input:');
    disp(input_str);
    disp('Structure of values and repetitions');
    for k=1:length(runlengths)
        disp(sprintf('  %d value %d repetitions', ...
            runlengths(k).value, runlengths(k).repetitions));
    end
