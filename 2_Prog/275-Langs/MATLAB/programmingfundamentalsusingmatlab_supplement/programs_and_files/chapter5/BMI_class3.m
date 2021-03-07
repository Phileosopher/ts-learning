% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% BMI_class3.m
%
% Find the body-mass index, given a height and weight.
% Example 3, with minimal class definition plus a function,
% and a constructor.
%
%
% Usage:
%   bmi_object3 = BMI_class3(70, 175)
%   disp(bmi_object3.getBMI);
%   bmi_object3
%

classdef BMI_class3

    properties
        height;
        weight;
    end

    methods
        % constructor
        function obj = BMI_class3(height, weight)
            obj.height = height;
            obj.weight = weight;
        end

        function bmi = getBMI(obj)
            % Calculate Body Mass Index, and return it
            % For the formula, see http://
            % www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
            bmi = obj.weight * 703 / (obj.height * obj.height);
        end

    end
end

