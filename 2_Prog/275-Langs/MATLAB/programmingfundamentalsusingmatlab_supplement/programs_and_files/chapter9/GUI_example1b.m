% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% GUI_example1b 
%
% This version pauses between examples. 
%
% Examples of several simple GUI elements.
% This script is NOT meant to be run as is, 
% but rather the cells should be experimented 
% with one by one.
%
%


    % A very simple GUI example
    handle1 = uicontrol('Style', 'pushbutton', ...
        'String', 'Say Hi', ...
        'Position', [250 200 50 50], ...
        'Callback', 'disp(''hello!'')');
    
    
    disp('Example 1 - a button that responds with hello.');
    disp('Press return to go to the next example');
    pause
    clf  % clear the figure

%%
    
    % A second simple GUI example
    handle1 = uicontrol('Style', 'pushbutton', ...
        'String', 'Say Hi', ...
        'Position', [250 200 50 50], ...
        'Callback', @changeText);

    disp('Example 2 - changing button text.');
    disp('Press return to go to the next example');
    pause
    clf  % clear the figure

%
%    % Alternate way of expressing this.
%    handle1 = uicontrol('Style', 'pushbutton', ...
%        'String', 'Say Hi', ...
%        'Position', [250 200 50 50], ...
%        'Callback', {'changeText'});
    
%%
    % calling a script instead as the callback "function"
    myvalue = 1;
    handle1 = uicontrol('Style', 'pushbutton', ...
        'String', 'Inc myvalue', ...
        'Position', [225 200 100 50], ...
        'Callback', 'changeData');
    
    disp('Example 3 - changing data with each button press.');
    disp('Press return to go to the next example');
    pause
    clf  % clear the figure

%%  

    disp('Example 4 - waiting until the user selects "quit".');

    % waiting until the user selects "quit"
    finished = false;
    handle1 = uicontrol('Style', 'pushbutton', ...
        'String', 'Quit', ...
        'Position', [225 200 100 50], ...
        'Callback', 'finished=true; close');
    while (~finished)
        pause(0.5);
    end
    
    disp('Press return to go to the next example');
    pause
    clf  % clear the figure

%%
disp('Example 5 produces an infinite loop. Skipping.');
%    disp('Example 5 - close without setting finished.');
%
%    % What will happen now?
%    finished = false;
%    handle1 = uicontrol('Style', 'pushbutton', ...
%        'String', 'Quit', ...
%        'Position', [225 200 100 50], ...
%        'Callback', 'close');
%    while (~finished)
%        pause(0.5);
%    end
%
%    disp('Press return to go to the next example');
%    pause
%    clf  % clear the figure

%%
    disp('Example 6 - Using a toggle button to quit.');

    % waiting until the user selects "quit"
    % This uses a togglebutton
    finished = false;
    handle1 = uicontrol('Style', 'togglebutton', ...
        'String', 'Quit', ...
        'Value', 0, ...
        'Position', [225 200 100 50]);
    
    
    pause(0.1);
    while (~finished)
        pause(0.1);
        if (get(handle1, 'Value') ~= 0)
            finished = true;
            disp('Button clicked. Exiting.');
        end 
    end
    close
    
    disp('Press return to go to the next example');
    pause
    clf  % clear the figure

    
%%  
    disp('Example 7 - waiting 3 seconds to check the box.');

    % Setting a component's value after a while.
    handle1 = uicontrol('Style', 'checkbox', ...
        'String', '3 seconds elapsed', ...
        'Value', 0, ...
        'Position', [225 200 150 50]);
    pause(3);
    set(handle1, 'Value', 1);
     
    disp('Press return to go to the next example');
    pause
    clf  % clear the figure

    
%%  
    disp('Example 8 - countdown to check the box.');


    % Show seconds count 10 - 5 - 1 - checked.
    handle1 = uicontrol('Style', 'checkbox', ...
        'String', '10 seconds', ...
        'Value', 0, ...
        'Position', [225 200 150 50]);
    pause(5);
    set(handle1, 'String', '5 seconds');
    pause(4);
    set(handle1, 'String', '1 second');
    pause(1);
    set(handle1, 'String', 'checked');
    set(handle1, 'Value', 1);
    
    
    disp('Press return to go to the next example');
    pause
    clf  % clear the figure

    
%%  
    % Opening two windows at once.
    figure_handle1 = figure(1);
    handle1 = uicontrol('Parent', figure_handle1, ...
        'String', 'Say Hi', ...
        'Position', [250 200 50 50], ...
        'Callback', {'changeText'});

    figure_handle2 = figure(2);
    handle2 = uicontrol('Parent', figure_handle2, ...
        'Style', 'togglebutton', ...
        'String', 'Quit', ...
        'Value', 0, ...
        'Position', [225 200 100 50], ...
        'Callback', 'close all');
    
    disp('Example 9 - multiple figures.');
    disp('Press return to go to the next example');
    pause
    clf  % clear the figure


    
%%    
    % Opening two windows at once.
    % Move the first one.
    figure_handle1 = figure(1);
    handle1 = uicontrol('Parent', figure_handle1, ...
        'String', 'Say Hi', ...
        'Position', [250 200 50 50], ...
        'Callback', {'changeText'});
    figure_handle2 = figure(2);
    handle2 = uicontrol('Parent', figure_handle2, ...
        'Style', 'togglebutton', ...
        'String', 'Quit', ...
        'Value', 0, ...
        'Position', [225 200 100 50], ...
        'Callback', 'close all');
    location = get(figure_handle1, 'Position');
    location(1) = 100;
    set(figure_handle1, 'Position', location);

    disp('Example 10 - multiple figures, but move the first one.');
    disp('Press return to go to the next example');
    pause
    clf  % clear the figure


%%  
    disp('Example 11 - report the toggle button''s status for 10 seconds.');


% An example of a toggle button.
figure_handle = figure(1);
toggle = uicontrol('Parent', figure_handle, ...
    'Style', 'togglebutton', ...
    'String', 'Toggle Me', ...
    'Value', 0, 'Position', [260 20 100 30]);
% Report this button's status every second for 10 seconds.
for t=1:10
    v = get(toggle, 'Value'); % See also set
    disp(v);
    pause(1);
end

disp('Examples finished!');
