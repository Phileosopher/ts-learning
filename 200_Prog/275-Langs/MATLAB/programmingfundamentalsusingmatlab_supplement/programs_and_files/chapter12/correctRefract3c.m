% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% This is a test version of a program that I made.
% I ran into an interesting problem here, and I made this version to
% demonstrate the problem.
%
%
% To see the problem:
%   OG = 1.117;
%   correctRefract3c
%   close;
%   OG = 1.090;
%   correctRefract3c
%   disp('See how the signal dips about 1.09?');
%   disp('That does not make sense.');
%   disp('The problem is that the arrays were not cleared,');
%   disp(' so that point and beyond is old data.');

%OG = 1.090;
FG = 1.030; %1.0525; %1.075; % FG;
% Convert OG and FG to Brix
x = grav2brix(OG);

i=1;
c = [ 1.001843, 0.002318474, 0.000007775, 0.000000034, ...
      0.00574, 0.00003344, 0.000000086 ];
while (FG < OG)
    y = grav2brix(FG);
    w(i) = c(1) - c(2) * x - c(3) * x^2 - c(4) * x^3 ...
        + c(5) * y + c(6) * y^2 + c(7) * y^3;
    
    FGreadings(i) = FG;
    FG = FG + 0.005;
    i = i + 1;
end

% show the corrections as a line 
plot(FGreadings, w, 'k');
title(sprintf('FG corrections for OG %5.3f', OG));
xlabel('Refractometer reading');
ylabel('Corrected reading');
axis('tight');

