% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% while_example5

    done = 0;
    while (~done)
       mykey = input('press q: ', 's');
       disp('you pressed a key');
       if ((mykey == 'q') | (mykey == 'Q'))
          done = 1;
       end
    end

