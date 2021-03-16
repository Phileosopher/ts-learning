% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% 
% Some csv files have problems with -1768 values showing up as
% faulty temperature readings. Assuming that these values are always 
% wrong, remove them from the .csv file.
%
%
% Usage:
%    fixCSV('badfile.csv', 'newname.csv');
%

function fixCSV(filename, fname2)

y1 = csvread(filename);

% Assume that the first value is OK
for k=2:length(y1)

    if (y1(k, 1) <= -1000)
        y1(k,1) = y1(k-1,1);
        y1(k,3) = y1(k-1,3);   % Copy the heat status
    end
    if (y1(k, 4) <= -1000)
        y1(k,4) = y1(k-1,4);
        y1(k,6) = y1(k-1,6);   % Copy the heat status
    end
end

csvwrite(fname2, y1);


