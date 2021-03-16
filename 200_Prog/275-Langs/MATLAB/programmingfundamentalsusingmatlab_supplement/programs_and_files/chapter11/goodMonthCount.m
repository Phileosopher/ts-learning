% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
    for month_count = 0:30
        years=month_count/12;
        rounded_years=floor(years);
        excess_months=floor((years*12)-(rounded_years*12)); % fixed 

        str_month = sprintf('%d months is', month_count);
        str_years = sprintf(' %d rounded_years', ...
            rounded_years);
        str_xmonths = sprintf(' and %d excess_months', excess_months);
        disp(sprintf('%s %s %s',str_month, str_years, str_xmonths));
    end

