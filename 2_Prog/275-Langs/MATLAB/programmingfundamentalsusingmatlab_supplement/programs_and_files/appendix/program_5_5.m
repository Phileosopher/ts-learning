% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_5_5.m
    % Copy bmi_object6.m to BMI_class6active.m
    % Add this to it
    % % in the constructor
    % if (nargin > 2)
    %     obj.am_active = varargin{3};
    % end
    % % in getBMI
    % if (obj.am_active)
    %     bmi = bmi - 5;
    % end

    bmi_object6active1 = BMI_class6active(70, 175);
    bmi_object6active1.getBMI(); % without active
    bmi_object6active2 = BMI_class6active(70, 175, true);
    bmi_object6active2.getBMI(); % with active
