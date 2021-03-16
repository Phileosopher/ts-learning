% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% proceedCB.m
%
% This is a callback function for the "proceed.m" example.
%
% Usage:
%    proceed
%

function proceedCB(myHandle, eventInfo, buttonHandle)

if (get(myHandle, 'Value') == true)
    disp('Checkbox value is true');
    set(buttonHandle, 'Visible', 'on');
else
    disp('Checkbox value is false');
    set(buttonHandle, 'Visible', 'off');
end

