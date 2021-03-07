% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% readWriteEx3.m
%
% Example writing a file using the 'fprintf' command.
% This is a better way (than readWriteEx2.m) 
% to write integer values, since 
% it places a space between them.
%
%
% Usage:
%   readWriteEx3
%
 
fname = 'exampledata.z';
myfile = fopen(fname, 'w');
if (myfile == -1)
    error(sprintf('File "%s" open did not work.', fname));
    return
end
fprintf(myfile, '%d ', 100:-1:0);
fclose(myfile);

disp('The file contents are:');
type exampledata.z
