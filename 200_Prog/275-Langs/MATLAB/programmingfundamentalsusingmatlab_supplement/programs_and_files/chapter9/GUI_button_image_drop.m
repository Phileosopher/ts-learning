% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Demonstrate a button with an image.
% Also include a drop-down menu.
%
% This function is old, and has been replaced by "GUI_example2.m"
%

figure_handle = figure(1);


% The variable "count" will be available globally,
% that is, any other functions/script can access and change it. 
global count;
count=23;
disp(sprintf('count is initially set to %d', count));

% Put two buttons in the figure.
% Notice that we specify which figure by "figure_handle".
handle1 = uicontrol('Parent', figure_handle, 'Style', 'pushbutton', ...
    'String', 'Inc Count', ...
    'Position', [430 30 60 60], 'Callback', 'GUI_incCount');
% Pushbutton seems to be the default.
handle2 = uicontrol('Parent', figure_handle, 'Style', 'pushbutton', ...
    'String', 'Quit', ...
    'Position', [500 30 60 60], 'Callback', 'close'); 

% Show an image in the figure.
x = imread('graphics/plant.jpg');
% The axes function specifies where the image will go, and how
% big it will be. The last two numbers after Position should be the
% same size, since our image is square. 
handle3 = axes('Parent', figure_handle, 'Position', [.25 .4 .5 .5]);
imshow(x);

% Add a drop-down menu
% Example from MATLAB help:
handle4 = uicontrol(figure_handle, 'Style', 'popupmenu', ...
    'String', {'one','two','three','four'}, ...
    'Value', 1, 'Position', [50 80 100 20], ...
    'Callback', {'hello2', 'drop-down menu'});

% Add a check box
% Example from MATLAB help:
handle5 = uicontrol(figure_handle, 'Style', 'checkbox', ...
    'String', 'Check here please',...
    'Value', 0, 'Position', [30 20 130 20], ...
    'Callback', {'hello2', 'checkbox'});

% Add change-able text
% Example from MATLAB help:
eth = uicontrol(figure_handle, 'Style', 'edit', ...
    'String', 'Enter your name here.', ...
    'Position', [30 50 130 20], ...
    'Callback', {'hello2', 'editable text'});

% Add text.
% Example from MATLAB help:
sth = uicontrol(figure_handle, 'Style', 'text', ...
    'String', 'Select a number from the menu below.', ...
    'Position', [30 100 130 40]);

% Add toggle button.
% Example from MATLAB help:
tbh = uicontrol(figure_handle, 'Style', 'togglebutton', ...
    'String', 'Toggle Me', ...
    'Value', 0, 'Position', [260 20 100 30], ...
    'Callback', {'hello2', 'toggle button'});

% Add radio button.
% Example from MATLAB help:
rbh = uicontrol(figure_handle, 'Style', 'radiobutton', ...
    'String', 'Radio button', ...
    'Value', 1, 'Position', [260 60 150 20], ...
    'Callback', {'hello2', 'radio button'});

% Add slider.
% Example from MATLAB help:
sh = uicontrol(figure_handle, 'Style', 'slider', ...
    'Max', 100, 'Min', 0, 'Value', 50, ...
    'SliderStep', [0.05 0.2], ...
    'Position', [260 80 150 30], ...
    'Callback', {'hello2', 'slider'});
% Add text.
% Example from MATLAB help:
sth2 = uicontrol(figure_handle, 'Style', 'text', ...
    'String', 'Slide this left/right.', ...
    'Position', [260 110 130 20]);

% Add a list box.
% Example from MATLAB help:
lbh = uicontrol(figure_handle, 'Style', 'listbox', ...
    'String', {'alpha','beta','gamma','delta'}, ...
    'Value', 1, 'Position', [450 300 60 50], ...
    'Callback', {'hello2', 'list box'});


% Give the user time to respond.
disp('Select one through four');            
pause(3);

% Get the current value of the drop-down menu.
v = get(handle4, 'Value');           
disp(sprintf('The drop-down menu has current value of %d.', v));


disp('This script is terminating.');

