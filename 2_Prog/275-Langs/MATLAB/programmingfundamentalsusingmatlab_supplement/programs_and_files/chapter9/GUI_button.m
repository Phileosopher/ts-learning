% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Demonstrate a button.
%

% We don't specify what image to use, but we should.

% The variable "count" will be available globally,
% that is, any other functions/script can access and change it. 
global count;
count=23;
disp(sprintf('count is initially set to %d', count));

% Put two buttons in the figure.
handle1 = uicontrol('String', 'Inc Count', 'Position', [100 100 160 120], ...
    'Callback', 'GUI_incCount'); 
handle2 = uicontrol('String', 'quit', 'Position', [300 100 160 120], ...
    'Callback', 'close'); 

disp('This function is terminating.');

