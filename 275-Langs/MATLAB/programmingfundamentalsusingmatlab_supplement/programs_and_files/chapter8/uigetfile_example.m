% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Let the user select a file with the graphical user interface
% command uigetfile.
% Only .png files will be selectable.
% This code also displays the image.

[f, p] = uigetfile('*.png', 'Please choose an image file.');
% Assume that a file was selected. 
[x, m, xa] = imread(strcat(p,f));
figure(); 
imshow(x)

