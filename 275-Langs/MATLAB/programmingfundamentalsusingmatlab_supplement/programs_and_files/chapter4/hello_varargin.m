% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% hello_varargin.m
%
% Variable argument input
%
% Demonstrate varargin.
% This program accepts a name, as zero or more strings.
% It then reports on the various parameters.
%
%
% Usage:
%   hello_varargin2('Ms.', 'Rosie', 'the', 'Riveter');
%   hello_varargin('fish', 'three', 3);
%   hello_varargin(uint16(3), 'three', 3);

function hello_varargin(varargin)

disp('Parameter list is:');
disp(varargin);

disp(sprintf('length of varargin is %d', length(varargin)));

disp(sprintf('nargin (number of arguments in) = %d', nargin));

for k=1:nargin
    if (ischar(varargin{k}))
        disp(sprintf('argument %d is string %s', k, varargin{k}));
    elseif (isinteger(varargin{k}))
        disp(sprintf('argument %d is int %d', k, varargin{k}));
    elseif (isfloat(varargin{k}))
        disp(sprintf('argument %d is float %5.3f', k, varargin{k}));
    else
        disp(sprintf('argument %d is ', k));
        varargin{k}
    end    
end

