% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% readWriteEx6.m
%
% Example writing to a file with "fwrite".
%
%
% Usage:
%   readWriteEx6
%

fname = 'exampledata.z2';
myfile = fopen(fname, 'w');
if (myfile == -1)
    error(sprintf('File "%s" open did not work.', fname));
    return
end
fwrite(myfile, 100:-1:48);
fclose(myfile);

disp('The file contents are:');
type exampledata.z2

