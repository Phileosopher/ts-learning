% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% subtract 1.
% 

function x = recursiveSub1(y)

disp(sprintf('starting recursiveSub1: y is %d', y));
if (y > 0)
    x = recursiveSub1(y-1);
else
    x = 1;
end
disp(sprintf('  ending recursiveSub1: y is %d', y));

