% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% Show that changing all red values leads to pink-colors
% in the grey pixels.
%

x = imread('streetcar.JPG');

figure(1);
imshow(x);
title('Original image');

x(:,:,1) = x(:,:,1) + 20;
figure(2);
imshow(x);
title('Image with red values increased');

