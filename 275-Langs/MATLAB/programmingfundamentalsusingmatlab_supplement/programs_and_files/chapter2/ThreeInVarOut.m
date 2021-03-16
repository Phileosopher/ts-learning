% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
    % ThreeInVarOut.m
    function varargout = ThreeInVarOut(x, y, z)
    a = (x + y + z)/3;   % average
    b = (x + y + z);     % sum
    c = sqrt(x^2 + y^2 + z^2);   % sqrt sum squared
    switch (nargout)
        case 1
            varargout{1} = a;
        case 2
            varargout{1} = b;
            varargout{2} = c;
        otherwise
            varargout{1} = a;
            varargout{2} = b;
            varargout{3} = c;
    end
