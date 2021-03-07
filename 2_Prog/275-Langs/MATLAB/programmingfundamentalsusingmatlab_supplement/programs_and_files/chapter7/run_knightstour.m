% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% 
%
% Start the knight's tour
%

row = 1;
col = 1;

% board = zeros(3,3);   % No. It cannot get the center square.
% board = zeros(4,4);   % No.
  board = zeros(5,5);   % Works for 5x5
% board = zeros(8,8);

%board(row, col) = 1;

[solved, solution] = knightstour(row, col, 1, board);

% >> [solved, solution] = knightstour(1, 1, 1, zeros(8,8))
% 
% solved =
% 
%      1
% 
% 
% solution =
% 
%      1    38    55    34     3    36    19    22
%     54    47     2    37    20    23     4    17
%     39    56    33    46    35    18    21    10
%     48    53    40    57    24    11    16     5
%     59    32    45    52    41    26     9    12
%     44    49    58    25    62    15     6    27
%     31    60    51    42    29     8    13    64
%     50    43    30    61    14    63    28     7
