% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Show a GUI
%
% x = imread('place_1_10_23_45.tiff');
% GUI_test(x);

function GUI_test(x)

figure(1);
%imshow(x);
 
global row;
row=23;
col=1;

    disp(sprintf('(%d, %d)', row, col));

        
handle1 = uicontrol('String',' up ', 'Position', [240 20 60 20], 'Callback', 'move_up(row, col)'); 
handle2 = uicontrol('String','down', 'Position', [240 1 60 20], 'Callback', 'incrow'); 
handle3 = uicontrol('String','right', 'Position', [180 10 60 20], 'Callback', 'hello'); 
%handle4 = uicontrol('String','left ', 'Position', [300 10 60 20], 'Callback', {'hello2', row});

handle4 = uicontrol('String','left ', 'Position', [300 10 60 20], 'Callback', {'hello2', 'you pressed the left button'});
handle5 = uicontrol('String','quit ', 'Position', [400 10 60 20], 'Callback', 'close'); 
% for size, the values are: [ column, row (from bottom), width, height]
handles.row = row;
handles.col = col;
%set(handle1, UserData, 'row');

get(handle1) %, 'Parent')

disp('This function is terminating.');

