% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
classdef exClass  
    % This is just a simple example.
    
    properties
        myRow = 0;
        myCol = 0;
        color = 'red';
        mySize = 20;
    end
    
    methods
        % Constructor
        function obj = exClass(r, c, colorStr)
            obj.myRow = r;
            obj.myCol = c;
            obj.color = colorStr;
        end
          
        function obj1 = setCol(obj1, c)
            obj1.myCol = c;
        end
          
        function obj1 = setRow(obj1, r)
            obj1.myRow = r;
        end

        function obj1 = setColor(obj1, colorStr)
            obj1.color = colorStr;
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

