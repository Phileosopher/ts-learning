% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% myKarplusStrongAlgo.m
%
% Try out the Karplus-Strong Algorithm
%   Given a starting signal (random) and the delay
% (assumed to be the length of the initial signal), 
% find the next M output values.
%
%
% Usage:
%    x = rand(1,100) - 0.5;
%    y = myKarplusStrongAlgo(x, 16000);
%    sound(y, 8000)
%
%    x = (1:50)/50;
%    y = myKarplusStrongAlgo(x, 8000);
%    sound(y-0.5, 8000)


function y = myKarplusStrongAlgo(x, M)
% Allow for N sample delay,
% then find y(n) = y(n-N)*0.5 + y(n-N-1)*0.5

%  x = rand(1,8);  M = 40;
N = length(x);
if (N < 2)
    % Pad by one or two zeros
    x = [x, ones(1, 2-N)];
    N = length(x);
end

y = zeros(1,M);

% Get the first N values
%k = length(x)-1;
k = 1;
y(1:N) = x;
% disp(sprintf('init y = x'));
y(N+1) = y(N-1)*0.5 + y(N)*0.5;
% disp(sprintf('init y(%d) = y(%d)*0.5 + y(%d)* 0.5', N+1, N-1, N));

oldk = k;
k = k + N+1;
% Use these to find the next N values
while (k < M)
    y(k:k+N-1) = y(oldk:k-2) *0.5 + y(oldk+1:k-1)* 0.5;
    % disp(sprintf('y(%d:%d) = y(%d:%d)*0.5 + y(%d:%d)* 0.5', ...
    %     k, k+N-1,    oldk, k-2,    oldk+1, k-1));
    oldk = k-1;
    k = k + N;
end


