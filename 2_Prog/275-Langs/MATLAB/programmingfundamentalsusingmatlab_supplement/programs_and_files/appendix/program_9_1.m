% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_9_1.m
    % See also figslider_callback.m

    global x;
    % A few of these globals are not used
    global startR;
    global stopR;
    global startC;
    global halfR;
    global halfC;
    global MAXR;
    global image_handle;

    startR = 1;
    startC = 1;
    x = imread('redBottleCap3.jpg');
    [MAXR, MAXC, MAXD] = size(x);
    halfR = floor(MAXR/2);
    halfC = floor(MAXC/2);
    fighandle = figure();
    
    % Slider 1
    sl = uicontrol('Parent', fighandle, ...
        'Style', 'slider');
    set(sl, 'Position', [180, 110, 200, 50]);
    set(sl, 'Callback', {'figslider_callback', 1});
    set(sl, 'MAX', halfC);
    set(sl, 'Value', startC);
    set(sl, 'SliderStep', [1/halfC 0.1]);
    
    % Slider 2
    sl2 = uicontrol('Parent', fighandle, ...
        'Style', 'slider');
    set(sl2, 'Position', [360, 170, 50, 200]);
    set(sl2, 'Callback', {'figslider_callback', 2});
    set(sl2, 'MAX', halfR);
    set(sl2, 'Value', startR);
    set(sl2, 'SliderStep', [1/halfR 0.1]);

    % Show the initial view
    stopR = 201;
    stopC = startC + halfC;
    image_handle = axes('Parent', fighandle, ...
        'Position', [.25 .4 .5 .5]);

    imshow(x(startR:startR+200, startC:startC+200, :));
