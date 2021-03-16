% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 


employee_table = readtable('example_table.csv'); 

employee_table

employee_table.Properties

employee_table.Properties.VariableNames{2}

employee_table.Properties.RowNames = {'marketing', 'sales'};

mytable_from_cell.Properties.VariableNames = ...
     {'name', 'age', 'pay', 'married', 'sickdays'}

mytable_from_cell.Properties.VariableDescriptions = ...
     {'person''s name', 'employee age', 'pay rate', 'marital status', 'sick days'};

mytable_from_cell.Properties

writetable(mytable_from_cell, 'example_table2b.csv');



