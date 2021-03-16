% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% Example code for centering an image

[x, m, xa] = imread('redBottleCap2.png');
imshow(x)
[MAXR, MAXC, MAXD] = size(x);

disp('Select a point on the image');

[c,r] = ginput(1);
c = round(c);
r = round(r);
y = zeros(512,512,3, 'uint8');
y(:,:,1) = x(r,c,1);
y(:,:,2) = x(r,c,2);
y(:,:,3) = x(r,c,3);
figure(); imshow(y)
for r=1:MAXR
    for c=1:MAXC
        if (xa(r,c) == 0)
            x(r,c,1) = y(r,c,1);
            x(r,c,2) = y(r,c,2);
            x(r,c,3) = y(r,c,3);
            xa(r,c) = 255;
        end
    end
end
imshow(x)

disp('Press a key to continue');
pause 

z = y;
ROW = 100;
COL = 100;
z(1+ROW:MAXR+ROW, 1+COL:MAXC+COL,:) = x;
imshow(z)

disp('Press a key to continue');
pause

ROW = 120;
COL = 95;
z = y;
z(1+ROW:MAXR+ROW, 1+COL:MAXC+COL,:) = x;
imshow(z)

imwrite(z, 'redBottleCap3.jpg', 'JPG');

