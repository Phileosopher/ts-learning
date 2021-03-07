% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% Given original image and r,c,
% set the pixel at r,c blue, and 
% set every neighbor blue, too, if it matches the first pixel. 
function x = blue_image(original, r, c)
    % Copy original to color
    x(:,:,1) = original;
    x(:,:,2) = original;
    x(:,:,3) = original;
    originalR = x(r, c, 1);
    originalG = x(r, c, 2);
    originalB = x(r, c, 3);
    % Make this pixel blue
    blue1 = 0;
    blue2 = 0;
    blue3 = 200;
    x(r, c, 1) = blue1;
    x(r, c, 2) = blue2;
    x(r, c, 3) = blue3;
    [MAXR, MAXC, MAXD] = size(x);
    checkMatrix = zeros(MAXR, MAXC);
    k = 1;
    checkedIndex = 0;
    checklist(k).row = r;
    checklist(k).col = c;
    checkMatrix(r, c) = 1;
    % Offsets to neighbors
    roffset = [-1, -1, -1,  0, 0,  1, 1, 1];
    coffset = [-1,  0,  1, -1, 1, -1, 0, 1];

while (checkedIndex < length(checklist))
    checkedIndex = checkedIndex + 1;
    % get the next thing, process it
    r1 = checklist(checkedIndex).row;
    c1 = checklist(checkedIndex).col;
    % Check each of the 8 neighbors
    for m=1:8
       r2 = r1 + roffset(m); 
       c2 = c1 + coffset(m);
       % Make sure this row,col is good 
       if (isRCinbounds(r2, c2, MAXR, MAXC))
           % Have we been here before? 
           % If so, go on to next
           if (checkMatrix(r2, c2) == 0)
               checkMatrix(r2, c2) = 1; % Mark it 
               % Is this pixel the same as the original?               
               if ((x(r2, c2, 1) == originalR) && ...
                   (x(r2, c2, 2) == originalG) && ...
                   (x(r2, c2, 3) == originalB))
                   % Make it blue
                   x(r2, c2, 1) = blue1;
                   x(r2, c2, 2) = blue2;
                   x(r2, c2, 3) = blue3;
                   % Add neighbors to check list
                   for m=1:8
                       r3 = r2 + roffset(m); 
                       c3 = c2 + coffset(m); 
                       if (isRCinbounds(r3, c3, MAXR, MAXC))
                           % Add this neighbor to the list to check
                           k = length(checklist) + 1;
                           checklist(k).row = r3;
                           checklist(k).col = c3;
                       end
                   end
               end
           end
        end
    end 
end

function OK = isRCinbounds(r1, c1, MAXR, MAXC)
if ((r1 > 0) && (r1 <= MAXR) && (c1 > 0) && (c1 <= MAXC))
    OK = 1;
else
    OK = 0;
end

