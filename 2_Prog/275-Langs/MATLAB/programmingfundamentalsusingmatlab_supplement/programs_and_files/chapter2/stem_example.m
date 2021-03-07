% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% stem_example.m
%

    pascal3 = conv([1, 1], [1, 1]);
    pascal5 = conv(pascal3, pascal3);
    y = conv(pascal5, pascal5);
 
    x = (1:length(y)) - 5;
    y2 = sqrt(y);
    hold on;
    stem(x, y2, 'go--');

    xlabel('centering at zero');
    ylabel('triangle values');
    title('Pascal''s Triangle');
    text(0.5, 68, 'maximum is here at y_0');


