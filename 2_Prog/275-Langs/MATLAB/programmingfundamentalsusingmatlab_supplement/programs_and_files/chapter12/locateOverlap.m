% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% locateOverlap.m
%
%   Given two signals, find where they overlap.
% Return a third, binary signal that shows this.
% For example, suppose you have a measured temperature signal,
% and a target temperature signal. When does the measured temp
% reach the target? How long is it before the target
% changes? This function finds this.
%   This function uses within 1 degree to be a match. Also, if 
% the temperature falls, it is still considered part of the hold time.
% So if the target is 154, the "start" is the first measured temp sample
% at or above 153.  
%
%
% Usage:
%    z = locateOverlap(measured, desired);
%

function z = locateOverlap(measured, target)

assert(length(measured) == length(target), ...
    'The two signals should be the same length.');

% How many times does the target change?
target2 = [0, target(1:(length(target)-1))];
% changes will be 1 every time the target changes
changes = (target - target2) ~= 0;

% start is either 0 or 1, indicating if measured == target yet.
start = 0;
% Find the first place where the target is met.
targetMet = ((target - measured) < 1);

% Create the output, set it to 0.
z = zeros(1, length(target));
% countIndex = 1;
% count(1) = 0;

% Every value of targetMet will be 0 or 1.
for k=1:length(measured)
    if (changes(k) == 1)
        % This marks a new stage.
        % It will probably take a while before measured
        % matches this temperature.
        %newStage = k;
        start = 0;
    end
    if ((start == 0) && ((target(k) - measured(k)) < 1))
        % measured matches target
        %start = k;
        start = 1;
    end
    z(k) = start;
    % count(countIndex) = count(countIndex) + start;
end

