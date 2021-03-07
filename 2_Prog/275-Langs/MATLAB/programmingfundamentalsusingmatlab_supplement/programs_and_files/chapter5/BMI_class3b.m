% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% BMI_class3b.m
%
% Find the body-mass index, given a height and weight.
% Example 3b, with minimal class definition plus a function,
% and a constructor. (This shows that the constructor MUST 
% be the first function.)
%
%
% Usage:
%   bmi_object3b = BMI_class3b(70, 175)
%   disp(bmi_object3b.getBMI);
%   bmi_object3b
%

classdef BMI_class3b

    properties
        height;
        weight;
    end

    methods
        function bmi = getBMI(obj)
            % Calculate Body Mass Index, and return it
            % For the formula, see http://
            % www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
            bmi = obj.weight * 703 / (obj.height * obj.height);
        end

        % constructor
        function obj = BMI_class3b(height, weight)
            obj.height = height;
            obj.weight = weight;
        end

    end
end

