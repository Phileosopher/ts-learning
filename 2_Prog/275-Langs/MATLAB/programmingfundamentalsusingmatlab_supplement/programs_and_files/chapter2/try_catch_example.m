% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
    % demonstrate the try..catch
    try
        display('Trying an unknown function.');
        f = unknown(3);
        disp('The unknown function worked!');
    catch
        disp('The function "unknown" must not exist.');
    end

