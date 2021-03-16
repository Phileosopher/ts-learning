% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% This function works with a GUI program.
%
% "future" is an argument that MATLAB reserves for future use.
%
% Usage:
%    handle1 = uicontrol('Style', 'pushbutton', ...
%        'String', 'Say Hi', ...
%        'Position', [250 200 50 50], ...
%        'Callback', @changeText);
%
%
function changeText(uihandle, future)

current_greeting = get(uihandle, 'String');
if (strcmp(current_greeting, 'hello'))
    set(uihandle, 'String', 'HELLO');
else
    set(uihandle, 'String', 'hello');
end

