% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 

function keypress_call(obj1, obj2)

a = get(gcf, 'CurrentCharacter');
disp(sprintf('keypress: %c', a));

