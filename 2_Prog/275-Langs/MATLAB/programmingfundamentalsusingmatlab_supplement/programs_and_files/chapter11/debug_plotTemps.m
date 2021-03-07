% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% plotTemps('tempsFerm.csv') does not work as expected.
% Instead of blue bars separating data between months, we get
% one big spike.
% See plotTemps_bad.m and the fixed version: plotTemps.m
% The fix means just looking for a difference, i.e. ~= 0,
% then multiplying that logical array.

filename = 'tempsFerm.csv';
y1 = csvread(filename);
maxVal = max(y1(:,2));
maxIndex = length(y1(:,1));
months1 = abs(y1(2:maxIndex,1) - y1(1:maxIndex-1,1))*maxVal;
months1 = months1.';
x1 = (1:length(y1))/(24*4);

% figure();
% plot(x1,[0,months1],'b-');
% title('This shows the problem; all blue points should be 1 of 2 heights');


b = y1(1:maxIndex-1,1);
a = y1(2:maxIndex,1);
figure();
plot(1:length(a),a, 'r')
hold on
plot(a-b)
title('The sudden drop causes the problem');

% localize the problem
% a and b have 23388 values
c = a-b;
[v,i] = min(c)
% 
% v =
% 
%    -10
% 
% 
% i =
% 
%         8377
% 
a2 = a(8370:8385);
b2 = b(8370:8385);
a2 - b2   % shows 0 and -10
% a (and b) are month codes. Usually, there is no difference or 1.
% That is, data points from September 3 and September 4 are both in the
% same month, so the month difference is 0. 
% Likewise, data points from September 31 and October 1 are in diffferent
% months, so the difference should be 1 (or -1).
% But a set of samples stopped in December, and started again in February.
% The difference is -10. So the data does not match our assumption.



