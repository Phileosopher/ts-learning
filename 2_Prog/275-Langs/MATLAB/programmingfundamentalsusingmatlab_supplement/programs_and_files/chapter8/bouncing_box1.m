% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
background = zeros(400,400,3,'uint8');

% Make a yellow box
% box_ROWS = 20;
% box_COLS = 20;
box = zeros(20,20,3,'uint8');
[box_ROWS, box_COLS, box_DEPTH] = size(box);
box(:,:,1) = 255;
box(:,:,2) = 255;

myimage = background;


% also show the box about in the middle
row_offset = 200;
col_offset = 200;

% initialize myimage
myimage = background;
old_row_offset = 200;
old_col_offset = 200;
for row_offset=200:4:300
    % get rid of the box we previously showed
    myimage(old_row_offset+1:old_row_offset + box_ROWS, old_col_offset+1:old_col_offset + box_COLS, :) = background(old_row_offset+1:old_row_offset + box_ROWS, old_col_offset+1:old_col_offset + box_COLS, :);
    % now show the box in this location
    myimage(row_offset+1:row_offset + box_ROWS, col_offset+1:col_offset + box_COLS, :) = box;
    imshow(myimage)
    % update the old information so we remember it next time
    old_row_offset = row_offset;
    old_col_offset = col_offset;
    % wait a bit, say 1 second
    pause(1);
end



