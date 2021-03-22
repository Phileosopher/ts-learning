% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% BMI_class2.m
%
% Find the body-mass index, given a height and weight.
% Example 2, with minimal class definition plus a function.
%
%
% Usage:
%   bmi_object2 = BMI_class2
%   bmi_object2.height = 70;
%   bmi_object2.weight = 175;
%   disp(bmi_object2.getBMI);
%   bmi_object2
%

classdef BMI_class2

    properties
        height;
        weight;
    end

    methods
        function bmi = getBMI(obj)
            % Calculate Body Mass Index, and return it
            % For the formula, see https://
            % www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
            bmi = obj.weight * 703 / (obj.height * obj.height);
        end

    end
end

