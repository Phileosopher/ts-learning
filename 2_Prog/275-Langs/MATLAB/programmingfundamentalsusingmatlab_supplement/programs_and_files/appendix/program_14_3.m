% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_14_3.m

    disp('You can try this with your OS, or use its GUI:');
    disp('  cp HelloExample.java HelloExample2.java');
    disp('  vi HelloExample2.java');
    disp('  javac HelloExample2.java ');
    disp('Assuming this has been done, try the following.');
    disp('You will likely need to change the javaaddpath parameter.');
    % javaaddpath('/Users/mweeks/matlab_work/');
    javaaddpath('matlab_work/');
    myJavaObj2 = javaObject('HelloExample2');
    sayHello(myJavaObj2);
    sayHello(myJavaObj2);
    sayHello(myJavaObj2);

