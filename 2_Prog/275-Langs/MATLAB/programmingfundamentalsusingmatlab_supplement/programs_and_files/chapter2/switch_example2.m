% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% switch_example2

    % Get input from the user.
    % Notice how the second parameter to "input" is 's',
    % which specifies a string. Otherwise, input will not
    % work for strings.
    acronym = input('Enter an acronym: ', 's');

    % Now print a response according to the input.
    switch acronym
        case 'html'
        case 'HTML'
            disp('Hyper Text Markup Language');
        case {'MATLAB', 'matlab'}
            disp('MATrix LABoratory, by MathWorks');
        otherwise
            disp('I do not know that one.');
    end

