% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% This is a utility program to show a square image from
% a rectangular one, allowing the user to specify commands
% like left and right.
% 

    [x, m, xa] = imread('graphics/berryTree.png');
    [MAXR, MAXC, MAXD] = size(x);
    done = false;
    offset = 100;
    while (~done)
        y = x(1:MAXR,offset+1:offset+MAXR,:);
        imshow(y)
        response = input('(l)eft (r)ight or (q)uit: ', 's');
        if ((response == 'q') || (response == 'Q'))
            done = true;
        elseif ((response == 'l') || (response == 'L'))
            offset = offset - 10;
            % Make sure we did not go too far left.
            if (offset < 1)
                offset = 1;
            end
        elseif ((response == 'r') || (response == 'R'))
            offset = offset + 10;
            % Make sure we did not go too far right.
            if (offset + MAXR > MAXC)
                offset = offset - 10;
            end
        end
        % Anything else input will be ignored.
    end
    ya = xa(1:MAXR,offset+1:offset+MAXR);
    imwrite(y, 'graphics/newBerryTree.png', 'PNG', 'alpha', ya);




