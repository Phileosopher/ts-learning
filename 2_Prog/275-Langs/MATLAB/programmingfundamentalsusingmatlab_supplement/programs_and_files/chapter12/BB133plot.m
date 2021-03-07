% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Example of a bad data plot 

y1 = csvread('BB133temps.csv');
% There are 3 seconds between samples,
% so div by 20 to have x-axis in minutes.
x1 = (1:length(y1))/20; 

y2 = y1(:,1);
y2(:,2) = y1(:,2);
y2(:,3) = y1(:,4);
y2(:,4) = y1(:,5);
k=100;
firsttarget = y2(k,2);
while ((y2(k,2) == firsttarget) && (k < length(y2)))
    k = k + 1;
end
k=k-1;
figure;
plot(x1, y2(:,1).');
hold on
plot(x1(1:k), y2(1:k,7)-15.0, 'g');

