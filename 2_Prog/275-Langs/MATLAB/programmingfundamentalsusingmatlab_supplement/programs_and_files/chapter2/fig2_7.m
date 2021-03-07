% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
   x = -4:4;
   y = 3:11;
   z = pascal(9);
%   surf(x, y, z);
%   figure();
%   mesh(x, y, z);
%   figure();
%   contour(x, y, z);
   figure();
   subplot(2,2,1);
   surf(x, y, z);
   title('surf');
   subplot(2,2,2);
   mesh(x, y, z);
   title('mesh');
   subplot(2,2,3);
   contour(x, y, z);
   title('contour');
   subplot(2,2,4);
   plot3(x, y, z);
   title('plot3');

