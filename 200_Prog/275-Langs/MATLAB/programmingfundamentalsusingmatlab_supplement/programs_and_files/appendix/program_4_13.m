% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_4_13.m

    % Start with example input
    a = [2, 1, 1, 1, 1, 7, 3, 8, 2, 2, 7];
    kept(1) = a(1); % keep 1st value
    k = 2;  % index of next kept value
    for n = 2:length(a)
        % Is a(n) already on kept list?
        % find (a(n) == kept), a logical array
        % if the sum of it is 0, it is not on the list
        if (sum(a(n) == kept) == 0)
            % Not on kept list yet
            kept(k) = a(n);
            k = k + 1;
        end
    end
    disp(kept);
