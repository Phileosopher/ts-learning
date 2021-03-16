% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
classdef exHandleClass < matlab.mixin.SetGet 
    % Inheriting from matlab.mixin.SetGet allows us to use it like a figure handle.
    % This is just a simple example.
    
    properties
        myRow = 0;
        myCol = 0;
        color = 'red';
        mySize = 20;
    end
    
    methods
        % Constructor
        function obj = exHandleClass(r, c, colorStr)
            obj.myRow = r;
            obj.myCol = c;
            obj.color = colorStr;
        end
          
        function draw(obj1)
            hold on
            % Put a square at this location.
            plot(obj1.myCol, obj1.myRow, strcat('s', obj1.color(1)), ...
                'MarkerFaceColor', obj1.color(1), ...
                'MarkerSize', obj1.mySize);
        end
    end
end

