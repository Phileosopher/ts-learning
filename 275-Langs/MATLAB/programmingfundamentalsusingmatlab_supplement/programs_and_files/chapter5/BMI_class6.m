% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% BMI_class6.m
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
%   bmi_object6 = BMI_class6()
%   bmi_object6.height = 70;
%   bmi_object6.weight = 175;
%
%   % or
%
%   bmi_object6 = BMI_class6(70)
%   bmi_object6.weight = 175;
%
%   % or
%
%   bmi_object6 = BMI_class6(70, 175)
%
%   bmi_object6
%   disp(bmi_object6.getBMI);
%   % we see that it remembers the bmi value
%   bmi_object6

classdef BMI_class6 < handle

    properties
        height;
        weight;
        bmi;
    end

    methods
        % constructor
        function obj = BMI_class6(varargin)
            if (nargin > 0)
                obj.height = varargin{1};
            end
            if (nargin > 1)
                obj.weight = varargin{2};
            end
        end

        function obj = getBMI(obj)
            
            % Calculate Body Mass Index, and return it
            % For the formula, see https://
            % www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
            bmi = obj.weight * 703 / (obj.height * obj.height);
            disp(bmi);
            obj.bmi = bmi;
        end

    end
end

