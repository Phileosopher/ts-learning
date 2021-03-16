% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_3_7.m
    % The problem:
    if ((userEntry ~= 1) || (userEntry ~= 2))
        disp('entry must be one or two');
    end

    % This should help see the problem
    userEntry = 1;
    disp('userEntry ~= 1 returns:');
    disp(userEntry ~= 1);
    disp('userEntry ~= 2 returns:');
    disp(userEntry ~= 2);
