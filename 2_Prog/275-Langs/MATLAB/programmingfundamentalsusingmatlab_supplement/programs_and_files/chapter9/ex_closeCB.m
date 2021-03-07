% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% ex_closeCB.m
%
% This is the callback for "ex_close.m"
%

function ex_closeCB(obj1, obj2)

disp('Doing some clean-up tasks before closing...');
pause(1);
close();

