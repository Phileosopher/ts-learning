% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% readWriteEx5.m
%
% Example appending to a file.
% It uses 'fprintf' to write additional data.
%
%
% Usage:
%   readWriteEx5
%

fname = 'exampledata.z';
myfile = fopen(fname, 'a');
if (myfile == -1)
    error(sprintf('File "%s" open did not work.', fname));
    return
end
fprintf(myfile, '%d ', -1:-1:-10);
fclose(myfile);

disp('The file contents are:');
type exampledata.z
