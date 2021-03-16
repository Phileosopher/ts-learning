% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% readWriteEx4.m
%
% Example reading a file with the 'fscanf' command.
% Open a file called 'exampledata.z' for reading,
% store data in variable mydata.
%
%
% Usage:
%   readWriteEx4
%

fname = 'exampledata.z';
myfile = fopen(fname, 'r');
if (myfile == -1)
    error(sprintf('File "%s" open did not work.', fname));
    return
end
mydata = fscanf(myfile, '%d ');
fclose(myfile);

disp('This was read from the file:');
disp(mydata);
