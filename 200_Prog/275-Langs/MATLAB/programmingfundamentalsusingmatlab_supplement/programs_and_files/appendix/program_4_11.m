% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_4_11.m

    % Start with example input
    a = [2, 1, 1, 1, 1, 7, 3, 8, 2, 2, 7];
    n = 2;
    count = 1;
    out = ''; % Empty string
    while (n <= length(a))
        % for the current value (n), is it repeated?
        if (a(n) == a(n-1))
            % repeat of the previous
            count = count + 1;
        else
            % not a repeat
            % report previous run
            out = sprintf('%s, %d - %d', out, count, a(n-1));
            count = 1;
        end
        n = n + 1;
    end
    disp(out);
