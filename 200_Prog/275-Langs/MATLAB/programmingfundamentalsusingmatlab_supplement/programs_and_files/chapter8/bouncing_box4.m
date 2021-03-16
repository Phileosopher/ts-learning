% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% bouncing_box, version 4
%
% This version should actually bounce.
% The yellow square is now a 3-D looking box.
%

background = zeros(400,400,3,'uint8');
[backgr_ROWS, backgr_COLS, backgr_DEPTH] = size(background);

% Make a yellow box
% box_ROWS = 20;
% box_COLS = 20;
box = zeros(20,20,3,'uint8');
[box_ROWS, box_COLS, box_DEPTH] = size(box);

%
% Make the yellow square look like a 3-D box.
%
box(1:15,1:15,1) = 255;
box(1:15,1:15,2) = 255;
% copy the square diagonally
for k=0:5
    box(1+k:15+k,1+k:15+k,1) = 255;
    box(1+k:15+k,1+k:15+k,2) = 255;
end
% vertical line
box(15,1:15,1) = 0;
box(15,1:15,2) = 0;
% horizontal line
box(1:15,15,1) = 0;
box(1:15,15,2) = 0;
% diagonal line
for k=15:20
    box(k,k,1) = 0;
    box(k,k,2) = 0;
end

myimage = background;

% Make this interesting
row_offset = 100;
col_offset = 200;

% initialize myimage
myimage = background;
old_row_offset = row_offset;
old_col_offset = col_offset;

delta_row = 4;
delta_col = 4;

for iteration = 1:300
    % get rid of the box we previously showed
    myimage(old_row_offset+1:old_row_offset + box_ROWS, old_col_offset+1:old_col_offset + box_COLS, :) = background(old_row_offset+1:old_row_offset + box_ROWS, old_col_offset+1:old_col_offset + box_COLS, :);

    % Update the coordinates of the box
    new_row_offset = row_offset + delta_row;
    new_col_offset = col_offset + delta_col;

    % Is the box still on screen?
    if (new_row_offset + box_ROWS > backgr_ROWS)
        % Too far, so reset
        new_row_offset = row_offset;
        delta_row = -delta_row;
    elseif (new_row_offset < 1)
        % Too far, so reset
        new_row_offset = row_offset;
        delta_row = -delta_row;
    end
    if (new_col_offset + box_COLS > backgr_COLS)
        % Too far, so reset
        new_col_offset = col_offset;
        delta_col = -delta_col;
    elseif (new_col_offset < 1)
        % Too far, so reset
        new_col_offset = col_offset;
        delta_col = -delta_col;
    end
    row_offset = new_row_offset;
    col_offset = new_col_offset;

    % now show the box in this location
    myimage(row_offset+1:row_offset + box_ROWS, col_offset+1:col_offset + box_COLS, :) = box;
    imshow(myimage)

    % update the old information so we remember it next time
    old_row_offset = row_offset;
    old_col_offset = col_offset;

    % wait a bit 
    pause(0.01);
end



