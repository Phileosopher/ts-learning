% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% readWriteEx1.m
%
% Trying to open a file that does not exist.
% This should fail and show an error message.
%
%
% Usage:
%   readWriteEx1
%

fname = 'Idonotexist';
[myfile, myerror] = fopen(fname, 'r');
if (myfile == -1)
    disp(myerror);
else
    disp('The file opened OK.');
    fclose(myfile);
end
