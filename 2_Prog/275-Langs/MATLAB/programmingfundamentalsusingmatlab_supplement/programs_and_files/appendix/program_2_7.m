% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_2_7.m

    % loop
    for k=1:5
        disp(k);
    end
    
    % conditional flow
    if (k < 3)
        disp('less than three');
    end
    
    % error control
    try 
        n = input('Enter a number: '); 
        s = 1/n;
    catch
        % If user only presses return
        disp('Try a different number');
    end
