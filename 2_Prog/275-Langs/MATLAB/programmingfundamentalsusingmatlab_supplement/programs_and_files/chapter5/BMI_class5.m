% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% BMI_class5.m
%
% Find the body-mass index, given a height and weight.
% Example 5, with minimal class definition plus a function,
% and a constructor with variable input arguments.
% Also, this class stores the bmi once it is calculated.
%
%
% Usage:
%   bmi_object5 = BMI_class5()
%   bmi_object5.height = 70;
%   bmi_object5.weight = 175;
%
%   % or
%
%   bmi_object5 = BMI_class5(70)
%   bmi_object5.weight = 175;
%
%   % or
%
%   bmi_object5 = BMI_class5(70, 175)
%
%   disp(bmi_object5.getBMI);
%   bmi_object5
%

classdef BMI_class5

    properties
        height;
        weight;
        bmi;
    end

    methods
        % constructor
        function obj = BMI_class5(varargin)
            if (nargin > 0)
                obj.height = varargin{1};
            end
            if (nargin > 1)
                obj.weight = varargin{2};
            end
        end

        function obj = getBMI(obj)
            
            % Calculate Body Mass Index, and return it
            % For the formula, see http://
            % www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
            bmi = obj.weight * 703 / (obj.height * obj.height);
            disp(bmi);
            obj.bmi = bmi;
        end

    end
end

