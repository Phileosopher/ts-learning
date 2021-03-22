% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% 
% ShowMineField.m
%
% Given two matrices: 1 showing where the user stepped/flagged,
% and one showing the mines and number of adjacent mines,
% display the minefield to the command screen.
%
% From the homework assignment:
% "The first matrix should contain the mines, as well as the number 
% of mines around each square. If there are no mines in an adjacent 
% square, then mark it with 0. The second matrix should contain a 
% record of where the user has stepped or flagged. 
% Use a 0 if the user has not stepped there, 
%       1 if the user has stepped there, and 
%       2 if the user has a flag there.
%
% When printing the minefield, you will use both matrices. For each 
% row and column, check to see if the user stepped there. If not, 
% display a '.' (or '@' if there is a flag). If there are no mines 
% around, show a space ' '. If there are mines around, show the number, 
% e.g., '2'. If there is a mine there, show a '*'."
% [https://carmaux.cs.gsu.edu/~mweeks/csc4630/hmwk2.html]
%
% Example:
%   mines = [0, 1, 1; 1, -1, 2; 1, 2, -1];
%   steps = [1, 1, 0; 0, 2, 1; 0, 0, 0];
%   ShowMineField(mines,steps);
%
%

function ShowMineField(mines, steps)

% Define symbols to use in output.
notStepped = '.';
bomb = '*';
blank = '_';
flag = '@';

% Get the dimensions of the matrices.
[rows1, cols1] = size(mines);
[rows2, cols2] = size(steps);

% Make sure they are the same size.
if ((rows1 ~= rows2) || (cols1 ~= cols2))
    % If they are different sizes, show an error and quit.
    error('Sorry, input matrices must be the same size.');
end

% Go through each element of the matrices, and build a
% string to show the output.
rowString = '';   % Set row to default (empty string).
for row = 1:rows1
    for col = 1:cols1
        % According to what is in the matrix, 
        if (steps(row, col) == 0)
            % Show that this has not been stepped on.
            ch = notStepped;
        elseif (steps(row, col) == 1)
            % Show the mine / number of adjacent mines.
            %  First, check for a mine.
            if (mines(row, col) == -1)
                ch = bomb;
            elseif (mines(row, col) == 0)
                ch = blank; 
            else
                % Make a character from the number.
                ch = mines(row, col) + '0';
            end
        else
            % Show the flag.
            ch = flag;
        end
        
        % Append this character to the string.
        rowString = strcat(rowString, ch);
    end
    disp(rowString);  % Show this row.
    rowString = '';   % Set row to default (empty string).
end
        
