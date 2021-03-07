% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Use the example handle class "exHandleClass".
%

figure();
axis([0 10 0 10]);

% Create an instance of the class.
myobject = exHandleClass(1, 2, 'blue');

% Use one of the methods
myobject.draw();

% Now change some things about the object.
set(myobject, 'color', 'green');
set(myobject, 'myRow', 2);

disp(get(myobject, 'color'));

% Show that the changes took place.
myobject.draw();

% This also works
myobject.set('color', 'yellow');
newColumn = myobject.get('myCol') + 1;
myobject.set('myCol', newColumn);
myobject.draw();

