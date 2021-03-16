% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% myKarplusStrongAlgo2.m
%
% Try out the Karplus-Strong Algorithm
%   Given a starting signal (random) and the delay
% (assumed to be the length of the initial signal), 
% find the next M output values.
%   This version uses the db2 scaling function.
%
%
% Usage:
%   x = rand(1,100)-0.5;
%   y = myKarplusStrongAlgo2(x, 16000);
%   sound(y, 8000)
%
%   % You can specify whether to use clipping at +/-1,
%   % and if you want to scale the filter coefficients.
%   y = myKarplusStrongAlgo2(x, 8000, true, 0.7);
%
%   % You can clip the samples yourself like this:
%   y = myKarplusStrongAlgo2(x, 16000, false, 0.75);
%   y2 = y.*(abs(y) < 0.6);
%   % You might not want to play this example through your speakers...
%   %sound(y2, 8000)
%
%   % A few variations:
%   y1 = myKarplusStrongAlgo2(x, 16000);
%   y2 = y1.*(abs(y1) < 1);
%   y3 = y2(length(y2):-1:1);
%   y4 = y1/max(abs(y1));
%   sound(y1, 8000)
%   sound(y2, 8000)
%   sound(y3, 8000)
%   sound(y4, 8000)


function y = myKarplusStrongAlgo2(x, M, varargin)

% clipping = true;
if (nargin < 2)
    disp('myKarplusStrongAlgo2: using defaults of a random array');
    disp('    and 8000 samples. That is, as if you had asked to run');
    disp('    myKarplusStrongAlgo2(rand(1,100) - 0.5, 8000)');
    if (nargin == 0)
        x = rand(1,100) - 0.5;
    end
    M = 8000;
    clipping = true;
    scaling  = 1.0;
elseif (nargin == 2)
    clipping = true;
    scaling  = 1.0;
elseif (nargin == 3)
    clipping = varargin{1};
    scaling = 1.0;
elseif (nargin == 4)
    clipping = varargin{1};
    scaling = varargin{2};
end


% Allow for N sample delay,
% then find y(n) = y(n-N)*0.5 + y(n-N-1)*0.5

%[lo_filter, hi_filter] = wfilters('db2');
[lo_filter, hi_filter] = wfilters('db2');

% reduce the coeffs in magnitude
% let x = rand(1,100) - 0.5;
% lo_filter (of db2) * 0.75 leads to values outside the bounds (unstable)
% lo_filter (of db2) * 0.71 looks conditionally stable for 2 seconds,
%                           then grows. By 6 seconds, it is over -1 bound.
% lo_filter (of db2) * 0.7071 (1/sqrt(2)) leads to values that decay slowly
% lo_filter (of db2) * 0.7 leads to values that decay
lo_filter = lo_filter * scaling;
% lo_filter*0.71 gets interesting after clipping comes in to play...

%  x = rand(1,8);  M = 40;
N = length(x);
if (N < 4)
    % Make x at least 4 values
    x = [x, 1, zeros(1, 3-N)];
    N = length(x);
end


y = zeros(1,M);

% Get the first N values
%k = length(x)-1;
k = 1;
y(1:N) = x;
% disp(sprintf('init y = x'));
y(N+1) = y(N-3)*lo_filter(4) + y(N-2)*lo_filter(3) + y(N-1)*lo_filter(2) + y(N)*lo_filter(1);
% disp(sprintf('init y(%d) = y(%d)*h4 + y(%d)*h3 + y(%d)*h2 + y(%d)*h1', ...
%      N+1, N-3, N-2, N-1, N));
y(N+1) = y(N-3)*lo_filter(4) + y(N-2)*lo_filter(3) + y(N-1)*lo_filter(2) + y(N)*lo_filter(1);
% disp(sprintf('init y(%d) = y(%d)*h4 + y(%d)*h3 + y(%d)*h2 + y(%d)*h1', ...
%      N+2, N-2, N-1, N, N+1));
y(N+1) = y(N-3)*lo_filter(4) + y(N-2)*lo_filter(3) + y(N-1)*lo_filter(2) + y(N)*lo_filter(1);
% disp(sprintf('init y(%d) = y(%d)*h4 + y(%d)*h3 + y(%d)*h2 + y(%d)*h1', ...
%      N+3, N-1, N, N+1, N+2));

oldk = k;
k = k + N+3;
% Use these to find the next N values
while (k < M)
    a = y(oldk:k-4)*lo_filter(1) + y(oldk+1:k-3)*lo_filter(2) ...
        + y(oldk+2:k-2)*lo_filter(3) + y(oldk+3:k-1)*lo_filter(4);
    % Clip data to within -1 to +1
    if (clipping)
        % array "a" has 4 values
        % Keep them all below 1
        a = min(a, 1);
        % Make sure a is not growing too much in positive direction
        if (sum(a) >= 4)
            a(2:3) = 0;
        end
        % Keep them all above -1
        a = max(a, -1);
        % Make sure a is not growing too much in negative direction
        if (sum(a) <= -4)
            a(2:3) = 0;
        end
    end
    y(k:k+N-1) = a;
    % disp(sprintf('y(%d:%d) = y(%d:%d)*h4 + y(%d:%d)*h3 + y(%d:%d)*h2 + y(%d:%d)*h1', ...
    %      k, k+N-1,    oldk, k-4,    oldk+1, k-3,  oldk+2, k-2,  oldk+3, k-1));

    oldk = oldk + N;
    k = k + N;
end


