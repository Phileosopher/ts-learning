% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% errordlg_example.m

    for n = 1:3
        mystr = sprintf('Something went wrong, code %d.', n);
        errordlg(mystr, 'Pop up window');
        disp(n);
    end

