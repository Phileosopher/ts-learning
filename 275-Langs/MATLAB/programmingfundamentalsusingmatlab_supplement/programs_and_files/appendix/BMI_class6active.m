% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% BMI_class6active.m
%
% Find the body-mass index, given a height and weight.
% Example 6, with minimal class definition plus a function,
% and a constructor with variable input arguments.
% Also, this class stores the bmi once it is calculated.
% And, since it inherits from the handle superclass,
% it remembers the bmi without reassigning the object.
%
%
% Usage:
%   bmi_object6active = BMI_class6active()
%   bmi_object6active.height = 70;
%   bmi_object6active.weight = 175;
%
%   % or
%
%   bmi_object6active = BMI_class6active(70)
%   bmi_object6active.weight = 175;
%
%   % or
%
%   bmi_object6active = BMI_class6active(70, 175)
%
%   bmi_object6active
%   disp(bmi_object6active.getBMI);
%   % we see that it remembers the bmi value
%   bmi_object6active

classdef BMI_class6active < handle

    properties
        height;
        weight;
        bmi;
        am_active;
    end

    methods
        % constructor
        function obj = BMI_class6active(varargin)
            if (nargin > 0)
                obj.height = varargin{1};
            end
            if (nargin > 1)
                obj.weight = varargin{2};
            end
            if (nargin > 2)
                obj.am_active = varargin{3};
            end
        end

        function obj = getBMI(obj)
            
            % Calculate Body Mass Index, and return it
            % For the formula, see https://
            % www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
            bmi = obj.weight * 703 / (obj.height * obj.height);
            if (obj.am_active)
                bmi = bmi - 5;
            end
            disp(bmi);
            obj.bmi = bmi;
        end

    end
end

