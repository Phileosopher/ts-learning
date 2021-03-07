% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% Note: if you click on the MATLAB window, the image may be re-displayed
% behind it on some systems. If the image seems to disappear, try moving
% the MATLAB window.

% Image read, show, and write
x0 = imread('stRing.JPG');
imshow(x0)
imwrite(x0, 'stRing.tiff');
pause


% converting to black and white
x1 = imread('stRing.JPG');
imshow(x1)
b = im2bw(x1);
% This does not look good
figure(2);
imshow(b)
pause 
b2 = im2bw(x1, 0.8);
% This does look good
%figure(3); 
imshow(b2)
pause
close(2)

% White line segment on a black background
x = zeros(128,128,'uint8');
x(10:118, 10:20) = 255;
imshow(x)
pause

x(10:118, 20:30) = 128;
imshow(x)
pause


% sin pattern
% y = has values from 0 to 2
t = 0:127;
y = sin(t/100*2*pi) + 1;
x2 = y.' * t;
imshow(uint8(x2))
pause

% diamond pattern
s = sin((0:127)/100*2*pi);
c = cos((0:127)/100*2*pi);
x3 = c.' * s;
x3 = uint8((x3+1)*127);
imshow(x3)
pause


% red square on a black background
x4 = zeros(128,128,3,'uint8');
x4(10:118, 10:118, 1) = 255;
imshow(x4)
pause

x4(10:118, 10:118, 3) = 255;
imshow(x4)
pause


% red green, blue squares on a black background
% x = zeros(128,128,3,'uint8');
% x(10:40, 10:40, 1) = 255;
% x(10:40, 30:70, 2) = 255;
% x(30:70, 20:50, 3) = 255;
% imshow(x)
x5 = zeros(128,128,3,'uint8');
maxR1 = 64+20;
maxC1 = 64;
x5(10:maxR1, 10:maxC1+15, 1) = 255;
x5(10:maxR1, maxC1-15:118, 2) = 255;
x5(maxR1-40:118, 20:108, 3) = 255;
imshow(x5)
pause






%%  [black]
%  [black][red][rb][rgb][gb][g][black]
%              [b          ]
%  [black]
%
%  [black]
%  [black][10][10][10][10][10][black]
%             [   3x10   ]
%  [black]
overlap = 20;
border = 10;
square_size = border * 2 + overlap * 5;
x6 = zeros(square_size, square_size, 3, 'uint8');
minRedRow = border;
minRedCol = border; 
maxRedRow = minRedRow + overlap * 3;
maxRedCol = minRedCol + overlap * 3;
minGreenCol = maxRedCol - overlap;
maxGreenCol = minGreenCol + overlap * 3;
minBlueRow = maxRedRow - overlap*2;
minBlueCol = minGreenCol - overlap;
maxBlueRow = minBlueRow + overlap * 3;
maxBlueCol = minBlueCol + overlap * 3;
for red = 127:128:255
    for green = 127:128:255
        for blue = 127:128:255
            % Red
            x6(minRedRow:maxRedRow, border:maxRedCol, 1) = red;
            % Green
            x6(minRedRow:maxRedRow, minGreenCol:maxGreenCol, 2) = green;
            % Blue
            x6(minBlueRow:maxBlueRow, minBlueCol:maxBlueCol, 3) = blue;
            imshow(x6)
            % pause
            pause(1);
         end
    end
end
pause


x7 = imread('stRing.JPG');
redValues = x7(:,:,1);
greenValues = x7(:,:,2);
blueValues = x7(:,:,3);
x7(:,:,1) = greenValues;
x7(:,:,2) = blueValues;
x7(:,:,3) = redValues;
imshow(x7)
pause

x7(:,:,1) = greenValues;
x7(:,:,2) = redValues;
x7(:,:,3) = redValues;
imshow(x7)
pause

x7(:,:,1) = greenValues;
x7(:,:,2) = redValues;
x7(:,:,3) = blueValues / 4;
imshow(x7)
pause

x7(:,:,1) = greenValues;
x7(:,:,2) = redValues;
x7(:,:,3) = blueValues.';
imshow(x7)
pause
    
%%
x0 = imread('stRing.JPG');
[MAXR, MAXC, MAXD] = size(x0);
%imshow(x0);
image(x0);
title('Select two points');
[xpts, ypts] = ginput(2);
rows = round(ypts);
cols = round(xpts);
outOfBounds = false;
% Check the rows and cols
if ((min(rows) < 1) || (max(rows) > MAXR))
    outOfBounds = true;
end
if ((min(cols) < 1) || (max(cols) > MAXC))
    outOfBounds = true;
end
if (~outOfBounds)
    % these are OK
    x8 = x0(min(rows):max(rows), min(cols):max(cols), :);
    imshow(x8);
else
    title('Out of bounds of the image');
    disp('Out of bounds of the image');
end

