% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% readWriteEx7.m
%
% Example reading from a file with "fread", a little at a time.
%
%
% Usage:
%   readWriteEx7
%

fname = 'exampledata.z2';
myfile = fopen(fname, 'r');
if (myfile == -1)
    error(sprintf('File "%s" open did not work.', fname));
    return
end
% Loop as long as the end-of-file has not been reached.
while (~feof(myfile)) 
    % Read 10 characters at a time
    dataFromFile = fread(myfile, 10);
    disp(sprintf('%d ', dataFromFile));
end
fclose(myfile);

