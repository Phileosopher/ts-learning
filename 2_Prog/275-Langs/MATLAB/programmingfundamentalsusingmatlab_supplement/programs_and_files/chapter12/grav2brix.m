% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% grav2brix.m 
%
% The data are from an SPG to Brix table (see Brix2SPGTable.txt).
% This should be an accurate conversion since it is based on table data.
%
% See also   grav2brix_approx.m
%
%
% Usage: 
%   grav2brix(1.052) 
%

function brix = grav2brix(SPG)

% First, define our array
Brix2SPGTable_v2

% Now look through the array.
k = 1;
index = 0;
done = false;
while ((k < length(SPGarray)) && (~done))
    if (SPGarray(k) >= SPG)
        % Stop here
        index = k;
        done = true;
    end
    k = k + 1;
end

%    disp(sprintf('Found the value at index %d', index));
if (~done)
    disp('The value was not found!');
end

%var brix = index / 10.0;
% Subtract 1 from index since MATLAB starts indices at 1.
brix = (index - 1) / 10.0;


