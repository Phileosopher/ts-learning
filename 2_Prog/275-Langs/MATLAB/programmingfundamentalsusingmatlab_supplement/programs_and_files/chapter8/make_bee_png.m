% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% make_bee_png.m
%
% Make a 16x16 .png image of a bee.
%
%
%  Usage:
%    make_bee_png
%

BEE_LENGTH = 16;
BEE_WIDTH = 16;

% binary pattern to use 
% (transparent / yellow / black / white)
bee = [ ...
    0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 0, 3, 3, 3,  3, 0, 0, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 3, 3, 3, 3,  3, 3, 0, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 3, 3, 3, 3,  3, 3, 3, 0, 0, 0, 0, 0;
    0, 0, 0, 1, 2, 3, 3, 3,  3, 3, 1, 1, 1, 0, 0, 0;
    0, 0, 0, 1, 2, 2, 1, 1,  2, 2, 1, 2, 2, 1, 0, 0;
    1, 1, 1, 1, 2, 2, 1, 1,  2, 2, 1, 2, 1, 1, 0, 0;
    
    0, 0, 1, 1, 2, 2, 1, 1,  2, 2, 1, 1, 1, 1, 0, 0;
    0, 0, 0, 1, 2, 2, 1, 1,  2, 2, 1, 1, 1, 0, 0, 0;
    0, 0, 0, 1, 2, 2, 1, 1,  2, 2, 1, 1, 1, 0, 0, 0;
    0, 0, 0, 0, 1, 2, 1, 1,  2, 2, 1, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 1, 0, 0, 0,  0, 0, 1, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 1, 0, 0, 0,  0, 0, 1, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0];

% Make it all black by default
z = uint8(zeros(BEE_LENGTH, BEE_WIDTH, 3));

% Now color in the pixels
[R, C] = size(bee);
for r = 1:R
    for c=1:C
        % Examine each bee(r,c) value, and color z.
        if (bee(r,c) == 1)
            % color this pixel yellow
            z(r, c, 1) = 240;
            z(r, c, 2) = 170;
            z(r, c, 3) = 35;
        elseif (bee(r,c) == 2)
            % color this pixel black
            z(r, c, 1) = 0;
            z(r, c, 2) = 0;
            z(r, c, 3) = 0;
        elseif (bee(r,c) == 3)
            % color this pixel white 
            z(r, c, 1) = 255;
            z(r, c, 2) = 255;
            z(r, c, 3) = 255;
        else
            % color this pixel black
            % If the bee value is 0, this
            % pixel will be transparent.
            z(r, c, 1) = 0;
            z(r, c, 2) = 0;
            z(r, c, 3) = 0;
        end
    end
end

% Try to use alpha values to make the bee appear
% without a black background (i.e., in case we want to
% show it with a different background, or over top of
% another object).
alpha = uint8((bee>0)*255);

imshow(z);
imwrite(z, 'bee.png', 'PNG', 'Alpha', alpha);

