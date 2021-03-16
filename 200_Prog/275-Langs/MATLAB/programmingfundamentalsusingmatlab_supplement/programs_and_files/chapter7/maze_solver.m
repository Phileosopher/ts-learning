% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Given a crude maze, solve it through recursion.
%
%
% Usage:
%    valid = maze_solver(maze, row, col);
%

function [valid] = maze_solver(maze, row, col)

% initialize valid to false.
valid = false;

[MAXROW, MAXCOL] = size(maze);

% Check the row and column
if ((row >= 1) && (row <= MAXROW) && ...
    (col >= 1) && (col <= MAXCOL))
    % Check - is this spot the goal?
    if (maze(row,col) == '@')
        disp('Solved!');
        disp(maze);
    end

    % Now check the maze at this row and column.
    if (maze(row,col) == ' ')
        % This spot is clear, so move here.
        maze(row, col) = '.';
        valid = true;
    end
end

% Now try to move to an adjacent square.
if (valid)
    % Try moving right
    maze_solver(maze, row, col+1);

    % Try moving down
    maze_solver(maze, row+1, col);

    % Try moving left
    maze_solver(maze, row, col-1);

    % Try moving up
    maze_solver(maze, row-1, col);
end
