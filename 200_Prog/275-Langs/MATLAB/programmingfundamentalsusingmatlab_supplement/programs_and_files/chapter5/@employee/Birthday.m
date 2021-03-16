% @employee/Birthday.m
% Example method for employee class
%
% function Birthday(emp)
% function emp = Birthday(emp)
function emp = Birthday(emp)


% Print a nice message
disp(sprintf('Happy Birthday, %s!',emp.name))

% Update the age info
disp(sprintf('You were %d',emp.age));
emp.age = emp.age + 1;
disp(sprintf('You are now %d',emp.age));

