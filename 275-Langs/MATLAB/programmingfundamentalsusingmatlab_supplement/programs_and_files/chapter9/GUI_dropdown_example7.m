% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% GUI_dropdown_example7.m
%
% Show an example with a drop-down menu, working with a callback function.
% The callback is a function defined within this function.
% This example DOES WORK.
%
%
function GUI_dropdown_example7

disp('This example does work.');

fig_handle = figure();

set(fig_handle, 'Color', [0.6 0.0 0.0]);
current_choice = 'red';
mystr = 'hello';

handle1 = uicontrol('Style', 'popup', ...
    'String', 'red|green|blue', ...
    'Position', [250 200 100 50], ...
    'Callback', {@GUI_dropdown_CB7, mystr});

%
% GUI_dropdown_CB7.m
%
% This is the callback function for GUI_dropdown_example7.m.
%
%

    function GUI_dropdown_CB7(obj1, obj2, myparam)
       
        persistent old_choice;

        disp(myparam);
 
        % Find out what the choice is now.
        Value = get(obj1, 'Value');
        if (Value == 1)
            set(fig_handle, 'Color', [0.6 0.0 0.0]);
            current_choice = 'red';
        elseif (Value == 2)
            set(fig_handle, 'Color', [0.0 0.6 0.0]);
            current_choice = 'green';
        else
            set(fig_handle, 'Color', [0.0 0.0 0.6]);
            current_choice = 'blue';
        end
        % old_choice might not be assigned yet.
        if (isempty(old_choice))
            disp(sprintf('Switching to %s', current_choice));
        else
            disp(sprintf('Switching from %s to %s', ...
                old_choice, current_choice));
        end

        % Remember what the choice is for next time.
        old_choice = current_choice;
    end  % GUI_dropdown_CB7
end  % GUI_dropdown_example7

