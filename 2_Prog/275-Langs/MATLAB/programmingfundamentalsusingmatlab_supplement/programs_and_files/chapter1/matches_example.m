% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
%

     % Two strings with different capitalization
     str1 = 'One';
     str2 = 'one';
     if (strcmp(str1, str2))
         disp('Equal');
     elseif (matches(str1, str2, 'IgnoreCase', true))
         disp('Same letters, but different capitalization');
     else
         disp('Not equal');
     end

