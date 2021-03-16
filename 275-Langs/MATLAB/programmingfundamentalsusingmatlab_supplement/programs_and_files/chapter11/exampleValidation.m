% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
%
function exampleValidation(myInput)
  arguments
    % argument name, size, class, functions = default
    % https://www.mathworks.com/help/matlab/matlab_prog/argument-
    %   validation-functions.html
    myInput (1,1) double {mustBePositive} 
  end
  % The rest of the function goes here.
  disp(sqrt(myInput));

end

