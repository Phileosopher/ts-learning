% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% countStageTime.m
%
% This function figures out how long a heating stage 
% took to raise the temperature, and also displays
% how long it was held.
%
%
% Usage:
%   countStageTime(filename);

% fname = 'data139.csv';
function countStageTime(fname)

disp(sprintf('Data set is %s', fname));
y = csvread(fname);
measured = y(:,1).';
target = y(:,2).';
z = locateOverlap(measured, target);
x = 1:length(measured);

% plot(x, measured, 'b');
% hold('on');
% plot(x, target.*z, 'r*');

j = 1;
% The heating system should heat up to a target temperature and hold it.
% The transition to the target and the hold time are called a stage,
% Here we consider a phase to be half of a stage, 
% i.e. a stage is a heating phase and holding phase.
% "count" is the number of samples in each phase.
% "temp" is the temperature for the stage.
% "holding" is whether this is a "holding" phase (or a heating phase).
count(1) = 0;
temp(1) = target(1);
holding(1) = z(1);
% mtemp is the measured temperature
mtemp(1) = measured(1);
index(1) = 1;
% Find sum of each stage
for k=2:length(z)
    if (z(k) == z(k-1))
        % count(j) = count(j) + z(k);
        count(j) = count(j) + 1;
    else
        % This is a transition
        j = j + 1;
        count(j) = 0;
        temp(j) = target(k);
        mtemp(j) = measured(k);
        holding(j) = z(k);
        index(j) = k;
    end
end
index(j+1) = length(measured);
% Now correct count to include the first ones
for k=1:length(count)
    if (count(k) > 0)
        count(k) = count(k) + 1;
    end
end

%count

% Each count represents 3 seconds.
% Convert to minutes.
count = count * 3 / 60;

% Now display results
stage = 1;
for k=1:length(count)
    if (count(k) > 0)
        if (holding(k))
            str=sprintf('  phase %d:  starting at %d hold at %d  for %d minutes', stage, round(mtemp(k)), round(temp(k)), round(count(k)));
            myavg = mean(measured(index(k):index(k+1)));
            str = strcat(str, sprintf('  avg temp %d', round(myavg)));
        else
            str=sprintf('  phase %d: heating from %d   to    %d took %d minutes', stage, round(mtemp(k)), round(temp(k)), round(count(k)));
            myavg = mean(measured(index(k):index(k+1)));
            str = strcat(str, sprintf('  avg temp %d', round(myavg)));
        end
        disp(str);
        stage = stage + 1;
    end
end
disp(' ');
