% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_11_5.m

    % See exampleValidation2.m 
    % myInput double {mustBeInteger, mustBeNonzero}

    disp('This works...');
    exampleValidation2(4)
    disp('This works...');
    exampleValidation2(-4)
    disp('This does not work...');
    exampleValidation2(0)
    disp('This does not work...');
    exampleValidation2(4.1)
    disp('This does not work...');
    exampleValidation2(4 + 1j)
