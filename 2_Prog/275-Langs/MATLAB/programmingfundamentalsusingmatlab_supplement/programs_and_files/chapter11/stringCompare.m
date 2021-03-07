% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% How can we compare two strings when one is longer?
%

str1 = 'abcdefghijklm';
str2 = 'abcdefghijklm;';
disp(sprintf('comparing "%s" to "%s" results in:', str1, str2));
strcmp(str1, str2)

disp('Now compare them, but only up to the length of the first string.');
maxlen = length(str1);
strcmp(str1, str2(1:maxlen))
if ((length(str2) >= maxlen) && (strcmp(str1, str2(1:maxlen))))
    disp('The strings appear to be the same.');
else
    disp('The strings appear to be different.');
end

