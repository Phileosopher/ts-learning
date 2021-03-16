% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% testAND.m
%
% Examine the difference between & and && in MATLAB.
%

condition2 = true;

    if (condition2 && condition3)
        disp('two and three are also true');
    else 
        disp('Two and three are not both true');
    end

    if (condition2 & condition3)
        disp('two and three are also true');
    else 
        disp('Two and three are not both true');
    end

condition2 = false;

    if (condition2 && condition3)
        disp('two and three are also true');
    else 
        disp('Two and three are not both true');
    end

    if (condition2 & condition3)
        disp('two and three are also true');
    else 
        disp('Two and three are not both true');
    end


