% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
%
% Use the example handle class "exClass".
%

figure();
axis([0 10 0 10]);

% Create an instance of the class.
myobject = exClass(1, 2, 'blue');

% Use one of the methods
myobject.draw();

% Now change some things about the object.
myobject = myobject.setColor('green');
myobject = myobject.setRow(2);

% Show that the changes took place.
myobject.draw();

pause

close
figure()
axis([0 10 0 10]);
myobjects(1) = exClass(1, 2, 'blue');
myobjects(2) = exClass(2, 2, 'green');
myobjects(3) = exClass(1, 3, 'red');
myobjects(4) = exClass(2, 3, 'yellow');
for k=1:length(myobjects)
    myobjects(k).draw();
end

