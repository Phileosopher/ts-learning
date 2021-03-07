% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Census data
%
% Educational Attainment of the Population 25 Years and Over, by Selected
% Characteristics:  2007
%Total	Educational Attainment								
%	"None - 8th grade"	"9th - 11th grade"	"High school graduate"	
%   "Some college no degree"  "Associate's degree"	"Bachelor's degree" 
%   "Master's degree" "Professional degree" "Doctoral degree"
% (cilivian labe force only)
%
% Source: 
% http://www.census.gov/population/www/socdemo/education/cps2007.html
%
% Also, for each level, find the total percentage of the population.
%


empl= [125537	4444	7504	36821	21569	12409	27793	10491	2473	2033];
unemp= [4987	318	751	1793	926	388	581	175	42	13];

% Find percent unemployed
pct = unemp ./ (empl + unemp);

plot(1:length(pct),pct,'b*-')
title('unemployment decreases as education increases');
ylabel('unemployment percentage');
xlabel('education level (<=8th grade up to Doctorate)');


totals = empl + unemp;
disp(' ');
disp('For 2007, here are the percentages of education level.');
disp(sprintf('None - 8th grade       %4.1f%%', totals(2)*100/totals(1)));
disp(sprintf('9th - 11th grade       %4.1f%%', totals(3)*100/totals(1)));
disp(sprintf('High school graduate   %4.1f%%', totals(4)*100/totals(1)));
disp(sprintf('Some college no degree %4.1f%%', totals(5)*100/totals(1)));
disp(sprintf('Associate''s degree     %4.1f%%', totals(6)*100/totals(1)));	
disp(sprintf('Bachelor''s degree      %4.1f%%', totals(7)*100/totals(1)));
disp(sprintf('Master''s degree        %4.1f%%', totals(8)*100/totals(1)));
disp(sprintf('Professional degree    %4.1f%%', totals(9)*100/totals(1)));
disp(sprintf('Doctoral degree        %4.1f%%', totals(10)*100/totals(1)));
disp(' ');

