% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% try_catch_example2

    try
        disp('trying myfuncton');
        userSays = myfuncton(4);
        disp('OK, myfuncton worked.');
    catch functionNotFoundException
        disp('Sorry, could not find "myfuncton".');
    end

