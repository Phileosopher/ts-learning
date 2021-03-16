% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_13_1.m

    N = length(str);
    % Get matrix of permutations for values 1, 2, .. N
    p = perms(1:N);
    % Apply p to character string
    [MAXR, MAXC] = size(p);
    
    for k=1:MAXR
        disp(str(p(k, :)))
    end
