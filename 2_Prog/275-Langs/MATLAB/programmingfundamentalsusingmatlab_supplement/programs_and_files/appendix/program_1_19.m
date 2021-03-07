% Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
% 
% program_1_19.m

    % Set the number of hours worked to 60 hours
    hoursWorked = 60;
    % Rate of pay for this person is $8.75
    payRate = 8.75;
    % The tax rate is 20 percent
    taxRate = 0.20;
    % Charge for (monthly) parking is $30
    parking = 30;   
    % Figure out the amount due to the employee for this
    % pay period, after subtracting the parking charge
    subtotal = hoursWorked * payRate - parking;
    % Calculate taxes based on the amount earned, after parking
    taxes = subtotal * taxRate;
    % Calculate the pay amount in Dollars after taking out taxes
    pay = subtotal - taxes;

