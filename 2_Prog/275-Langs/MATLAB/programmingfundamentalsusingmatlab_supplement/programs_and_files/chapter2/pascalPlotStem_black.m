% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%

    % Make x and y
    pascal3 = conv([1, 1], [1, 1]);
    pascal5 = conv(pascal3, pascal3);
    y = conv(pascal5, pascal5);
    x = (1:length(y)) - 5;

    % Show x,y
    figure();
    plot(x, y, 'k*:');

    % Make another array: y2
    y2 = sqrt(y);

    % Show y2 on the same figure
    hold on;
    stem(x, y2, 'ko--');

    % Put some text on the figure.
    xlabel('centering at zero');
    ylabel('triangle values');
    title('Pascal''s Triangle');
    text(0.5, 68, 'maximum is here at y_0');


