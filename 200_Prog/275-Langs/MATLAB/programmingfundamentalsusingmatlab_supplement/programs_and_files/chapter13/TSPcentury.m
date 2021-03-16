% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 

% Assuming 50 cities, how long would you computer need to check all
% possibilities?

% My current computer has a quad-core, 1.4 GHz processor.
cycles = 4 * (1.4 * 1000^3);
% Find 50 factorial
fiftyCities = factorial(50);
% How many seconds in a year?
secInYear = 60 * 60 * 24 * 365;
% How many seconds in a leap year?
secInLeapYear = 60 * 60 * 24 * 366;
% Ignore leap centuries...
% How many seconds in a century?
secInCentury = (3*secInYear + secInLeapYear) * 25;
% How many seconds to check all possible solutions?
sec2answer = fiftyCities / (cycles);

disp('It will take this many centuries to check all possibilities:');
sec2answer / secInCentury



