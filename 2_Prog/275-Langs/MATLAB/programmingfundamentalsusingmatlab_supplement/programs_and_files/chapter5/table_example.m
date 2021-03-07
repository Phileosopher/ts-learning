% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 

    employee{1} = 'John Doe';
    employee{2} = 26;
    employee{3} = 8.75;
    employee{4} = false;
    employee{5} = 5;
    employee{2,1} = 'Jane Public';
    employee{2,2} = 32;
    employee{2,3} = 11.12;
    employee{2,4} = false;
    employee{2,5} = 6;
    mytable_from_cell = cell2table(employee);


    names = {'John Doe'; 'Jane Public'};
    ages = [26; 32];
    payrate = [8.75; 11.12];
    married = [false; false];
    sick_days = [5; 6];
    mytable = table(names, ages, payrate, married, sick_days);

    writetable(mytable, 'example_table.csv');


