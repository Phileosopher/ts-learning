% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% GUI_dropdown_example4.m
%
% Show an example with a drop-down menu, working with a callback function.
% This example DOES NOT WORK.
%
%
function GUI_dropdown_example4

fig_handle = figure();

disp('This example does NOT work.');

current_choice = 'red';
mystr = 'hello';

handle1 = uicontrol('Style', 'popup', ...
    'String', 'red|green|blue', ...
    'Position', [250 200 100 50], ...
    'Callback', {'GUI_dropdown_CB4', current_choice, mystr});


%
% GUI_dropdown_CB4.m
%
% This is the callback function for GUI_dropdown_example4.m.
%
%

    function GUI_dropdown_CB4(obj1, obj2, current_choice, myparam)
        
        disp('hello from GUI_dropdown_CB4');
        disp(myparam);
        
        Value = get(obj1, 'Value')
        
        % Remember what the choice was last time.
        old_choice = current_choice;
        % Find out what the choice is now.
        if (Value == 1)
            current_choice = 'red';
        elseif (Value == 2)
            current_choice = 'green';
        else
            current_choice = 'blue';
        end
        disp(sprintf('Switching from %s to %s', old_choice, current_choice));
    end  % GUI_dropdown_CB4
end  % GUI_dropdown_example4

