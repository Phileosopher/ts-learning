% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 


employee_table = readtable('example_table.csv');
employee_table.Properties.RowNames = {'marketing', 'sales'};
employee_table.Properties.VariableDescriptions = ...
{'person''s name', 'employee age', 'pay rate', 'marital status', 'sick days'};
writetable(employee_table, 'example_table2c.xls');

employee_tab2 = readtable('example_table2c.xls');
% It (employee_tab2) still does not have the extra information.

