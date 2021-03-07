% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% readWriteEx2.m
%
% Example writing a file using 'fprintf'.
% This is not a good example, since the numbers run together.
%
%
% Usage:
%   readWriteEx2
%
 
fname = 'exampledata.z';
myfile = fopen(fname, 'w');
if (myfile == -1)
    error(sprintf('File "%s" open did not work.', fname));
    return
end
fprintf(myfile, '%d', 100:-1:0);
fclose(myfile);

disp('The file contents are:');
type exampledata.z
