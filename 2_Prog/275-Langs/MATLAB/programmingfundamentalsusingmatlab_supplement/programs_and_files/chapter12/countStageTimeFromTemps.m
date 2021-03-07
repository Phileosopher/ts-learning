% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% countStageTimeFromTemps.m
%
% This is a version of countStageTime.m that uses the original data file
% (e.g. BB140temps.csv) instead of the specially prepared data file that
% I made for earlier batches (e.g. data92.csv).
%
% This function figures out how long a heating stage 
% took to raise the temperature, and also displays
% how long it was held.
%
% When you pass "true" to the second param of this function, it will 
% generate LaTeX output.
%
%
% See also latexFromStages.sh, a shell script that takes the output
% of countStageTime.m and creates a Latex table from it.
% (It was a pre-cursor to this function.)
%
% Usage:
%   countStageTimeFromTemps(filename, false);
%
% Example:
%   countStageTimeFromTemps('BB140temps.csv', true);

function countStageTimeFromTemps(fname, LatexOutput)
%fname = 'BB353temps.csv';
%LatexOutput = true;

% LatexOutput = true;  % false;

if (~LatexOutput)
    disp(sprintf('Data set is %s', fname));
end

y = csvread(fname);
measured = y(:,2).';
target = y(:,3).';
z = locateOverlap(measured, target);
% onTarget is when the target is met.
% When onTarget is 0, the target has not been met.
% onTarget is non-zero when the target has been met 
% (e.g. 152 when met at target temperature of 152).
% Use onTarget to figure out how long the stage was supposed to be, 
% without counting time for the next transition.
%onTarget = target .* z;
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
% "index" is the index of the transitions (used for finding average temp)
count(1) = 0;
temp(1) = target(1);
holding(1) = z(1);
% mtemp is the measured temperature
mtemp(1) = measured(1);
index(1) = 1;
% Find sum of each stage
% This seems like a bad way to go about it. 
% We have a pretty good idea of what the stages are, by
% the target temps. 
% z should tell us if the target has been met (yet), or not.
phase(1) = target(1);
count(1) = 0;
myStage(1).target = target(1);
myStage(1).startIndex = 1;
% myStage(1).stopIndex = 1;
myStage(1).metIndex = 0;
myStage(1).startTemp = measured(1);
for k=2:length(target)
    if (target(k) == target(k-1))
        % count(j) = count(j) + z(k);
        % disp(sprintf('j = %d', j));
        count(j) = count(j) + 1;
        % Check to see if the target temp has been met yet
        if ((myStage(j).metIndex == 0) && (z(k) == 1))
            myStage(j).metIndex = k;
        end
    else
        % This is a transition
        myStage(j).stopIndex = k-1;
        myStage(j).count = count(j);
        j = j + 1;
        myStage(j).startTemp = measured(k);
        myStage(j).target = target(k);
        myStage(j).metIndex = 0;
        myStage(j).startIndex = k;
        %myStage(j).target = target(k);
        phase(j) = target(k);
        count(j) = 0;
        temp(j) = target(k);
        mtemp(j) = measured(k);
        holding(j) = z(k);
        index(j) = k;
disp(sprintf('% At index %d, Going from stage with target %d to target %d', k, target(k-1), target(k)));
    end
end
% old way:
% j = 1;
% for k=2:length(z)
%     if (z(k) == z(k-1))
%         % count(j) = count(j) + z(k);
%         count(j) = count(j) + 1;
%     else
%         % This is a transition
%         j = j + 1;
%         count(j) = 0;
%         temp(j) = target(k);
%         mtemp(j) = measured(k);
%         holding(j) = z(k);
%         index(j) = k;
%     end
% end
index(j+1) = length(measured);
myStage(j).stopIndex = length(measured);
myStage(j).count = count(j);
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
for k=1:length(myStage)
    myStage(k).count = myStage(k).count * 3 / 60;
end

% Now display results
if (LatexOutput)
    disp(' ');
    disp('\vspace{0.2in}');
    disp(' ');
    disp('\begin{center}');
    disp('\begin{tabular}{|c|l|l|l|l|}');
    disp('  \hline');
    str = strcat(fname, ' & initial     & target      & time in & average  \\');
    disp(str);
    disp('Mash steps & temperature & temperature & minutes & temperature (F)  \\');
end
stage = 1;
for k=1:length(count)
    if (count(k) > 0)
        if (holding(k))
            str=sprintf('  phase %d:  starting at %d hold at %d  for %d minutes', stage, round(mtemp(k)), round(temp(k)), round(count(k)));
            lstr=sprintf('  hold & %d & %d & %d ', round(mtemp(k)), round(temp(k)), round(count(k)));
            myavg = mean(measured(index(k):index(k+1)));
            str = strcat(str, sprintf('  avg temp %d', round(myavg)));
            lstr = strcat(lstr, sprintf(' & %d \\\\', round(myavg)));
        else
            str=sprintf('  phase %d: heating from %d   to    %d took %d minutes', stage, round(mtemp(k)), round(temp(k)), round(count(k)));
            lstr=sprintf('  heat & %d & %d & %d ', round(mtemp(k)), round(temp(k)), round(count(k)));
            myavg = mean(measured(index(k):index(k+1)));
            str = strcat(str, sprintf('  avg temp %d', round(myavg)));
            lstr = strcat(lstr, sprintf(' & %d \\\\', round(myavg)));
        end
        if (LatexOutput)
            disp('  \hline');
            disp(lstr);
        else 
            disp(str);
        end
        stage = stage + 1;
    end
end
if (LatexOutput)
    disp('  \hline');
    disp('\end{tabular}');
    disp('\end{center}');
end
disp(' ');



% 
% Make another table, with just the apparent mash schedule
%
% Now display results
if (LatexOutput)
    disp(' ');
    disp('\vspace{0.2in}');
    disp(' ');
    disp('\begin{table}');
    disp('\begin{center}');
    %disp('\caption{Mash schedule}');
    disp(sprintf('  \\caption{Mash schedule from %s}', fname));
    disp('\vspace{0.2in}');
    disp('\begin{tabular}{|c|l|l|l|}');
    disp('  \hline');
    str = strcat(fname, '   & target      & time in  & \\');
    disp(str);
    disp('Mash stage & temperature (F) & minutes & \\');
end
%stage = 1;
%actualStage = 1;
% % There is a bug, if the temperature in stage N+1 is met at the start of it.
% % That is, if the temperature happens to go high at the end of stage N,
% % the system switches to stage N+1, and the temperature in N+1 is met,
% % then this code puts N and N+1 together as one large stage.
%line1 = target.*z;
%line2 = line1(2:end);
%line2(length(line1)) = line1(end);
%sub12 = line1 - line2;
% % Find the transitions, i.e. when the target temperature changes.
%transition = (sub12 ~= 0);
%for k=1:length(count)
%    if (count(k) > 0)
%        if (holding(k))
%            str=sprintf('  phase %d:  starting at %d hold at %d  for %d minutes', stage, round(mtemp(k)), round(temp(k)), round(count(k)));
%            % Show a label for the type of mash rest
%            rest = '';
%            if ((round(temp(k)) >= 90) && (round(temp(k)) < 113))
%                rest = 'acid rest';
%            elseif ((round(temp(k)) >= 113) && (round(temp(k)) < 132))
%                rest = 'protein rest';
%            elseif ((round(temp(k)) >= 132) && (round(temp(k)) < 150))
%                rest = 'low saccarification rest';
%            elseif ((round(temp(k)) >= 150) && (round(temp(k)) < 160))
%                rest = 'saccarification rest';
%            elseif (round(temp(k)) >= 160)
%                rest = 'mash-out';
%            end
%            lstr=sprintf('  %d & %d & %d & %s \\\\', ...
%                actualStage, round(temp(k)), round(count(k)), rest);
%            myavg = mean(measured(index(k):index(k+1)));
%            actualStage = actualStage + 1;
%            if (LatexOutput)
%                disp('  \hline');
%                disp(lstr);
%            else
%                disp(str);
%            end
%            stage = stage + 1;
%        end
%    end
%end

% This should work...
stageCount = 0;
for k=1:length(myStage)
    % Ignore any stages that are less than 1 minute.
    if (round((myStage(k).stopIndex - myStage(k).metIndex)*3/60) > 0)
        stageCount = stageCount + 1;
            str=sprintf('  phase %d:  starting at %d hold at %d  for %d minutes', stageCount, round(myStage(k).startTemp), round(myStage(k).target), round(myStage(k).count));
            % Show a label for the type of mash rest
            rest = '';
            tempTemp = round(myStage(k).target);
            if ((tempTemp >= 90) && (tempTemp < 113))
                rest = 'acid rest';
            elseif ((tempTemp >= 113) && (tempTemp < 132))
                rest = 'protein rest';
            elseif ((tempTemp >= 132) && (tempTemp < 150))
                rest = 'low saccarification rest';
            elseif ((tempTemp >= 150) && (tempTemp < 160))
                rest = 'saccarification rest';
            elseif (tempTemp >= 160)
                rest = 'mash-out';
            end
            lstr=sprintf('  %d & %d & %d & %s \\\\', ...
                stageCount, round(myStage(k).target),  ...
              round((myStage(k).stopIndex - myStage(k).metIndex + 1)*3/60), ...
                rest);
            %   k, round(myStage(k).startTemp), round(myStage(k).count), rest);
            myavg = mean(measured(index(k):index(k+1)));
            % actualStage = actualStage + 1;
            if (LatexOutput)
                disp('  \hline');
                disp(lstr);
            else
                disp(str);
            end
    end
end

if (LatexOutput)
    disp('  \hline');
    disp('\end{tabular}');
    disp(sprintf('  \\label{tab:%s}', fname));
    disp('\end{center}');
    disp('\end{table}');
end
disp(' ');

% target(transition)
%if (sum(transition) > actualStage)
%    ttemps = target(transition);
%    disp(sprintf('There are %d actual stages, but %d stages were detected.', actualStage, sum(transition)));
%    disp('These are:');
%    disp(ttemps(2:end));
%end



