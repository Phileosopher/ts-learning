% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
    %
    % An example summation of 10 to 97, 
    % in increments of 2.718

    startvalue = 10;
    endvalue = 97;
    increment = 2.718;

    % Initialize the sum
    mysum = 0;
    counter = startvalue;
    % Loop until finished
    while (counter <= endvalue)
        mysum = mysum + counter;
        % add the increment
        counter = counter + increment;
    end

    disp(sprintf('The sum from %d to %d with ', ...
        startvalue, endvalue));
    disp(sprintf('increment %4.2f is %8.2f', ...
        increment, mysum));

