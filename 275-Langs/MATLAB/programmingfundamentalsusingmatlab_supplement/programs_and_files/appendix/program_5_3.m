% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_5_3.m

    employee_table = readtable('example_table.csv');
    employee_table{1,2} = employee_table{1,2} + 1;
    writetable(employee_table, 'example_table_new.csv');
