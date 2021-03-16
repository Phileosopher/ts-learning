% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_2_13.m
 
    day_of_month = 0; % initial value
    while ((day_of_month < 1) || (day_of_month > 31))
        day_of_month = input('Please enter a day of the month: ');
    end
