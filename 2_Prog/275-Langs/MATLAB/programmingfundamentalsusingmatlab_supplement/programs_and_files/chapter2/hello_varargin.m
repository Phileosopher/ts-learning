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
% Example:
%    hello_varargin('John', 'Doe');

    % Variable argument input
    function hello_varargin(varargin)

    str = 'hello';
    for k=1:nargin
        % Add a space, followed by next parameter.
        str = sprintf('%s %s', str, varargin{k});
    end
    disp(str);

