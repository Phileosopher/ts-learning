% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 

function keypress_cursors(obj1, obj2)

global x y hndl 

a = get(gcf, 'CurrentCharacter');
% disp(sprintf('keypress: %d', a));

% 28 is the left arrow
% 29 is the right arrow
% 30 is the up arrow
% 31 is the down arrow
switch (a) 
    case 28
        % left 
        x = x - 10;
        if (x < 1) 
          x = 1;
        end
    case 29
        % right 
        x = x + 10;
        if (x > 260) 
          x = 260;
        end
    case 30
        % up 
        y = y + 10;
        if (y > 400) 
          y = 400;
        end
    case 31
        % down 
        y = y - 10;
        if (y < 1) 
          y = 1;
        end
end

set(hndl, 'Position', [x, y, 300, 24]);


