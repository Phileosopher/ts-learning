% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%% grav2brix_compare.m
%
% How much error is in the grav2brix_approx function?
% This program calculates it.
%
%

%spg=1.000:0.001:1.120;

%% Get a subset of the specific gravities
Brix2SPGTable_v2
spg = SPGarray(1:282);
m = 1;
for k=spg
    approx(m) = grav2brix_approx(k);
    exact(m) = grav2brix(k);
    % Print a few of the exact values, to double-check them.
    if ((k > 1.050) && (k < 1.060))
        disp(sprintf('exact Brix for %8.6f is %4.2f',k,exact(m)));
    end
    m = m + 1;
end

%% 
% Plot the exact versus the approximate Brix values.
figure(1);
plot(spg, exact, 'b');
hold on
% plot(1:length(approx), approx, 'r');
plot(spg, approx, 'r');
axis('tight');
title('Exact Brix values (blue) versus approximate ones (red)');

%%
% Now find the differences between them.
diff = exact - approx;

%% 
% Now plot the differences.
figure(2); 
stem(spg, diff)
title('Errors between approximate and actual Brix values');
axis('tight');

