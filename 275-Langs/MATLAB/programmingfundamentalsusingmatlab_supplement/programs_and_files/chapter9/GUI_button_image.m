% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Demonstrate a button with an image.
%

figure_handle = figure(1);

% Show an image in the figure.
x = imread('graphics/plant.jpg');
% The axes function specifies where the image will go, and how
% big it will be. The last two numbers after Position should be the
% same size, since our image is square. 
handle3 = axes('Parent', figure_handle, 'Position', [.25 .4 .5 .5]);
imshow(x);

% The variable "count" will be available globally,
% that is, any other functions/script can access and change it. 
global count;
count=23;
disp(sprintf('count is initially set to %d', count));

% Put two buttons in the figure.
% Notice that we specify which figure by "figure_handle".
handle1 = uicontrol('Parent', figure_handle, 'String', 'Inc Count', ...
    'Position', [100 30 160 120], 'Callback', 'GUI_incCount'); 
handle2 = uicontrol('Parent', figure_handle, 'String', 'quit ', ...
    'Position', [300 30 160 120], 'Callback', 'close'); 

disp('This function is terminating.');

