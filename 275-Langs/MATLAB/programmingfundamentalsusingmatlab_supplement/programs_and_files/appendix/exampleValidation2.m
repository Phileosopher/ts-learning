% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Based on exampleValidation.m
% updated to add checks for non-zero, and integer
%
function exampleValidation2(myInput)
  arguments
    % argument name, size, class, functions = default
    % https://www.mathworks.com/help/matlab/matlab_prog/argument-validation-functions.html
    % myInput (1) double mustBePositive = 0
    myInput double {mustBeInteger, mustBeNonzero} 
  end
% .. rest of the function goes here.
  disp(sqrt(myInput));

end
