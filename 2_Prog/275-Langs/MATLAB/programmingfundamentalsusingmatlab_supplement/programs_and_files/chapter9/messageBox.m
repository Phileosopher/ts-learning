% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% A simple textbox example in MATLAB.
%
% Usage:
%    messageBox('Click OK')
%

function messageBox(myText)

figure_handle = figure;
% Make a guess as to how big the text will appear
guessWidth = length(myText) * 10;

% Text that cannot be edited.
text_handle1 = uicontrol('Parent', figure_handle, ...
   'Style', 'text', ...
   'String', myText, ...
   'Position', [30 100 guessWidth 100]);

set(text_handle1, 'FontSize', 25);

% Add "quit" button to the figure.
quitButton_handle = uicontrol('Parent', figure_handle, ...
    'Style', 'pushbutton', ...
    'String', 'OK', ...
    'BackgroundColor', [0.9, 0.8, 0.8], ...
    'Position', [475 50 80 60], 'Callback', 'close();'); 
