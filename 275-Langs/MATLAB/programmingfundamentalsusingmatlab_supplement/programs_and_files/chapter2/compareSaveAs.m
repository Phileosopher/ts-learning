% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%
% compareSaveAs.m
%
% Show an example plot that looks differently with saveas command
% than the File -> Save As option from the menu.
%
%
% Usage:
%   compareSaveAs    % Assumes that file compareSaveAs.fig is available.
%

myCurrentFig = openfig('compareSaveAs.fig');
imagefname = 'compareSaveAs1.jpg';
imagefname2 = 'compareSaveAs2.jpg';
% Save the plot automatically.
saveas(myCurrentFig, imagefname, 'jpg');
str = sprintf('Figure saved as ''%s''.', imagefname);
disp(str);
disp('Now use the ''File'' and ''Save As'' menu options to save it as ');
disp(imagefname2);
disp('Press a key when done.');
pause

x = imread(imagefname);
if (~exist(imagefname2, 'file'))
    str = sprintf('File ''%s'' not found.', imagefname2);
    disp(str);
    return
end
y = imread(imagefname2);

disp('images have the following sizes');
str = sprintf('saveas command %d x %d x %d', ...
   size(x));
disp(str);
str = sprintf('File - Save As %d x %d x %d', ...
   size(y));
disp(str);


