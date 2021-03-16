% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% ex_closereqCB.m
%
% Experiment with closereq
% This is the callback for "ex_closereq.m"
%

function ex_closereqCB(obj1, obj2)

disp('Closing the window in 1 sec.');
pause(1);
closereq();
