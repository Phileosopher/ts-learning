% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% Generate a line of Pascal's triangle
pascal3 = conv([1, 1], [1, 1]);
pascal5 = conv(pascal3, pascal3);
y = conv(pascal5, pascal5);
plot(1:length(y), y, 'k')



% Here is an alternate way
pascal1 = 1;
pascal2 = conv(pascal1, [1, 1]);
pascal3 = conv(pascal2, [1, 1]);
pascal4 = conv(pascal3, [1, 1]);
pascal5 = conv(pascal4, [1, 1]);
pascal6 = conv(pascal5, [1, 1]);
pascal7 = conv(pascal6, [1, 1]);
pascal8 = conv(pascal7, [1, 1]);
y = conv(pascal8, [1, 1]);
disp(pascal1);
disp(pascal2);
disp(pascal3);
disp(pascal4);
disp(pascal5);
disp(pascal6);
disp(pascal7);
disp(pascal8);
disp(y);



