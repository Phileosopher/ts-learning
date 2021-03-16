% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% plotTemps.m
%
% Show a nice plot of temperatures recorded by the impee device.
% The file name could be 'impout' or 'impout.csv', and usually
% comes from a log file like 'impout.txt' or
% '/usr/lib/cgi-bin/sandboxFiles/impout'.
% It should report the temperature every 15 minutes.
%
% See also tempMonitor.m, which is a program to do the same thing. 
% I could not find it and did not think I had written it, so I wrote plotTemps.
%
% This version allows you to pass a parameter or two.
%
%
% Usage:
%   plotTemps()
%   plotTemps('datafile.csv')
%   plotTemps('datafile.csv', 'xaxis title') 
%

function plotTemps(varargin)

% Set defaults
filename = 'tempsFerm.csv';
xaxis_text = 'Days';
yaxis_text = 'Degrees Fahrenheit';
if (nargin >= 1)
    filename = varargin{1};
    if (nargin > 1)
        % title for x axis 
        xaxis_text = varargin{2};
    end
end

% impout.first has the raw data. 
% tempsFerm_Nov_to_Mar_2015.csv has the processed data.
y1 = csvread(filename);
% y1(:,1) = y1(:,1) + 60;
maxIndex = length(y1(:,1));
maxVal = max(y1(:,2));
% Make months a periodic spike, marking the new month.
%months1 = abs(y1(2:maxIndex,1) - y1(1:maxIndex-1,1))*maxVal;
months1 = (y1(2:maxIndex,1) - y1(1:maxIndex-1,1));
% Make it a logical array, then multiply.
months1 = (months1 ~= 0) * maxVal;
months1 = months1.';
% plot(y1)
x1 = (1:length(y1))/(24*4);
% plot(x1,y1)
% The line below is adapted
% from http://www.mathworks.com/matlabcentral/answers/
% 43376-why-is-the-autocolor-green-of-plot-not-the-same-as-plotting-g
plot(x1,y1(:,2),'color',[0 0.4 0.1])
hold on
axis('tight');
% plot after axis so we don't re-scale it.
plot(x1,[0,months1],'b-');
xlabel(xaxis_text);
ylabel(yaxis_text);
title('Temperatures reported by the impee device');


