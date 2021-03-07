% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% BMI_class4.m
%
% Find the body-mass index, given a height and weight.
% Example 4, with minimal class definition plus a function,
% and a constructor with variable input arguments.
%
%
% Usage:
%   bmi_object4 = BMI_class4()
%   bmi_object4.height = 70;
%   bmi_object4.weight = 175;
%
%   % or
%
%   bmi_object4 = BMI_class4(70)
%   bmi_object4.weight = 175;
%
%   % or
%
%   bmi_object4 = BMI_class4(70, 175)
%
%   disp(bmi_object4.getBMI);
%   bmi_object4
%

classdef BMI_class4

    properties
        height;
        weight;
    end

    methods
        % constructor
        function obj = BMI_class4(varargin)
            if (nargin > 0)
                obj.height = varargin{1};
            end
            if (nargin > 1)
                obj.weight = varargin{2};
            end
        end

        function bmi = getBMI(obj)
            % Calculate Body Mass Index, and return it
            % For the formula, see http://
            % www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
            bmi = obj.weight * 703 / (obj.height * obj.height);
        end

    end
end

