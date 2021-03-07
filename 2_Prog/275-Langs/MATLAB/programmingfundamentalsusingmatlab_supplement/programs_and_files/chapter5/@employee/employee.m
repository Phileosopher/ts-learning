% @employee/employee.m
% An example class
%
function emp = employee(name, age, married)

tempStructure.name = name;
tempStructure.age = age;
tempStructure.payRate = 8.75;
tempStructure.married = married;
tempStructure.sickDays = 5;

emp = class(tempStructure,'employee');
