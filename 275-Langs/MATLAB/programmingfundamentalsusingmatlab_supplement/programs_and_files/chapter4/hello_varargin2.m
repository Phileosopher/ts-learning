% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% hello_varargin2.m
%
% Variable argument input
%
% Demonstrate varargin.
% This program prints "hello" followed by a name.
% The user specifies the name, as zero or more strings,
%
% Usage:
%   hello_varargin2('Ms.', 'Rosie', 'the', 'Riveter');
%

function hello_varargin2(varargin)

% Initialize our string to later display.
str = 'hello';
% Now for each argument, add it to our string.
for k=1:nargin
    % Add a space, followed by next parameter.
    str = sprintf('%s %s', str, varargin{k});
end

% Show the string to the user.
disp(str);
