% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
    % Return the division of a by b.
    % Usage:
    %    c = mydivision(a, b);
    function c = mydivision(a, b)
    assert(b ~= 0, 'Second parameter must not be zero.');
    c = a/b;


