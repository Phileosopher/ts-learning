#!/usr/bin/env python3
"""
VirtualPLC valve.py

Purpose: Creates a generic Valve class for PLC-controlled SCADA systems.

Classes:
    Valve: Generic superclass
    Gate: Valve subclass; provides for an open/close valve
    Globe: Valve subclass; provides for a throttling valve
    Relief: Valve subclass; provides for a pressure-operated open/close valve

Author: Cody Jackson

Date: 4/9/18
#################################
Version 0.1
    Initial build
"""

import math


class Valve:
    """Generic class for valves.

    Cv is the valve flow coefficient: number of gallons per minute at 60F through a fully open valve with a press. drop
    of 1 psi. For valves 1 inch or less in diameter, Cv is typically < 5.

    Variables: name, position, Cv, deltaP, flow_in, flow_out, press_out, press_in

    Methods: calc_coeff(), press_drop(), valve_flow_out(), get_press_out(), get_position(), change_position(), open(),
    close()
    """

    def __init__(self, name="", sys_flow_in=0.0, sys_flow_out=0.0, drop=0.0, position=0, flow_coeff=0.0, press_in=0.0):
        """Initialize valve.

        :param sys_flow_out: Fluid flow out of the valve
        :param drop: Pressure drop across the valve
        :param press_in: Pressure at valve inlet
        :param name: Instance name
        :param sys_flow_in: Flow rate into the valve
        :param position: Percentage valve is open
        :param flow_coeff: Affect valve has on flow rate; assumes a 2 inch, wide open valve
        """
        self.name = name
        self.__position = int(position)  # Truncate float values for ease of calculations
        self.Cv = float(flow_coeff)
        self.flow_in = float(sys_flow_in)
        self.deltaP = float(drop)
        self.flow_out = float(sys_flow_out)
        self.press_out = 0.0
        self.press_in = press_in

    def calc_coeff(self, diameter):
        """Roughly calculate Cv based on valve diameter.

        :param diameter: Valve diameter

        :return: Update valve flow coefficient
        """
        self.Cv = 15 * math.pow(diameter, 2)

    def press_drop(self, flow_out, spec_grav=1.0):
        """Calculate the pressure drop across a valve, given a flow rate.

        Pressure drop = ((system flow rate / valve coefficient) ** 2) * spec. gravity of fluid

        Cv of valve and flow rate of system must be known.

        Specific gravity of water is 1.

        :param flow_out: System flow rate into the valve
        :param spec_grav: Fluid specific gravity; default assumes fluid is water

        :except ZeroDivisionError: Valve coefficient not provided

        :return: Update pressure drop across valve
        :rtype: float
        """
        try:
            x = (flow_out / self.Cv)
            self.deltaP = math.pow(x, 2) * spec_grav
        except ZeroDivisionError:
            return "The valve coefficient must be > 0."

    def valve_flow_out(self, flow_coeff, press_drop, spec_grav=1.0):
        """Calculate the system flow rate through a valve, given a pressure drop.

        Flow rate = valve coefficient / sqrt(spec. grav. / press. drop)

        :param flow_coeff: Valve flow coefficient
        :param press_drop: Pressure drop (psi)
        :param spec_grav: Fluid specific gravity

        :except ValueError: Valve coefficient or deltaP <= 0

        :return: Update system flow rate
        :rtype: float
        """
        try:
            if flow_coeff <= 0 or press_drop <= 0:
                raise ValueError("Input values must be > 0.")
            else:
                x = spec_grav / press_drop
                self.flow_out = flow_coeff / math.sqrt(x)
                return self.flow_out
        except ValueError:
            raise  # Re-raise error for testing

    def get_press_out(self, press_in):
        """Get the valve outlet pressure, calculated from inlet pressure.

        :param press_in:  Pressure at valve inlet

        :return: Pressure at valve outlet
        :rtype: float
        """
        if press_in:
            self.press_in = press_in  # In case the valve initialization didn't include it, or the value has changed
        self.press_drop(self.flow_out)
        self.press_out = self.press_in - self.deltaP

    @property
    def position(self):
        """Get position of valve, in percent open."""
        return self.__position

    @position.setter
    def position(self, new_position):
        """Change the valve's position.

        If new position is not an integer, an error is raised.

        :param new_position: Value indicating valve's position.

        :except TypeError: Non-integer value provided.

        :return: Update valve position
        :rtype: int
        """
        try:
            if type(new_position) != int:
                raise TypeError("Integer values only.")
            else:
                self.__position = new_position
        except TypeError:
            raise  # Re-raise for testing

    def open(self):
        """Open the valve"""
        self.__position = 100
        self.flow_out = self.flow_in
        self.press_out = self.press_in

    def close(self):
        """Close the valve"""
        self.__position = 0
        self.flow_out = 0
        self.press_out = 0
        self.deltaP = 0


class Gate(Valve):
    """Open/closed valve.

    Subclasses Valve.

    Methods:
        read_position()
        turn_handle()
    """
    def read_position(self):
        """Identify the position of the valve.

        :return: Indication of whether the valve is open or closed.
        :rtype: str
        """
        if self.position == 0:
            return "{name} is closed.".format(name=self.name)
        elif self.position == 100:
            return "{name} is open.".format(name=self.name)
        else:  # bad condition
            return "Warning! {name} is partially open.".format(name=self.name)

    def turn_handle(self, new_position):
        """Change the status of the valve.
        
        :param new_position: New valve position

        :return: Update valve position
        """
        if new_position == 0:
            self.close()
        elif new_position == 100:
            self.open()
        else:  # Shouldn't get here
            return "Warning: Invalid valve position."


class Globe(Valve):
    """Throttling valve.

    Subclasses Valve.

    Methods:
        read_position()
        turn_handle()
    """

    def read_position(self):
        """Identify the position of the valve."""
        return "{name} is {position}% open.".format(name=self.name, position=self.position)

    def turn_handle(self, new_position):
        """Change the status of the valve.
        
        :param new_position: New valve position

        :return: Update outlet flow rate, valve pressure drop, and pressure out.
        """
        if new_position == 100:
            self.open()
        elif new_position == 0:
            self.close()
        else:
            self.position = new_position
            self.flow_out = self.flow_in * self.position / 100
            self.press_drop(self.flow_out)
            self.get_press_out(self.press_in)


class Relief(Valve):
    """Pressure relieving valve.

    Assumes full open when open set point reached and fully closed when close set point reached. Does not affect flow
    rate or system pressure; those parameters must be adjusted elsewhere.

    Subclasses Valve.

    Methods:
        read_position()
        set_open_pressure()
        set_close_pressure()
        read_open_pressure()
        read_close_pressure()
        valve_operation()
    """

    def __init__(self, name="", sys_flow_in=0.0, sys_flow_out=0.0, drop=0.0, position=0, flow_coeff=0.0,
                 press_in=0.0, open_press=0, close_press=0):
        """Inherits base initialization and adds valve open/close pressure values."""
        super(Relief, self).__init__(name, sys_flow_in, sys_flow_out, drop, position, flow_coeff, press_in)
        self.setpoint_open = open_press
        self.setpoint_close = close_press

    def read_position(self):
        """Identify the status of the valve.

        :return: The open/closed status of the valve.
        :rtype: str
        """
        if self.position == 0:
            return "{name} is closed.".format(name=self.name)
        elif self.position == 100:
            return "{name} is open.".format(name=self.name)
        else:   # bad condition
            return "Warning! {name} is partially open.".format(name=self.name)

    def set_open_pressure(self, open_set):
        """Set the pressure setpoint where the valve opens.

        :param: open_set: Opening set point

        :return: Update the opening set point
        """
        self.setpoint_open = open_set

    def read_open_pressure(self):
        """Read the high pressure setpoint."""
        return self.setpoint_open

    def read_close_pressure(self):
        """Read the low pressure setpoint."""
        return self.setpoint_close

    def set_close_press(self, close_set):
        """Set the pressure setpoint where the valve closes.

        :param close_set: Closing set point

        :return: Update the closing set point
        """
        self.setpoint_close = close_set

    def valve_operation(self, press_in):
        """Open the valve if pressure is too high; close the valve when pressure lowers.

        :param press_in: Valve input pressure

        :return: Update valve position
        """
        if press_in >= self.setpoint_open:
            self.open()
        elif press_in <= self.setpoint_close:
            self.close()


if __name__ == "__main__":
    # Functional test_valves
    # name="", sys_flow_in=0.0, position=0, flow_coeff=0.0, drop=0.0, open_press=0, close_press=0
    gate1 = Gate("Pump inlet")
    print("{} created".format(gate1.name))
    print(gate1.read_position())
    gate1.turn_handle(100)
    print(gate1.read_position())
    gate1.close()
    print(gate1.read_position())
    gate1.open()
    print(gate1.read_position())

    globe1 = Globe("\nThrottle valve", flow_coeff=21, press_in=10, sys_flow_in=15)
    print("{} created".format(globe1.name))
    print(globe1.read_position())
    globe1.open()
    print(globe1.read_position())
    globe1.close()
    print(globe1.read_position())
    globe1.turn_handle(40)
    print(globe1.read_position())

    relief1 = Relief("\nPressure relief", open_press=25, close_press=20)
    print("{} created".format(relief1.name))
    print(relief1.read_position())
    print("The open setpoint is {} psi.".format(relief1.read_open_pressure()))
    print("The close setpoint is {} psi.".format(relief1.read_close_pressure()))
    relief1.set_open_pressure(75)
    relief1.set_close_press(73)
    print("The open setpoint is {} psi.".format(relief1.read_open_pressure()))
    print("The close setpoint is {} psi.".format(relief1.read_close_pressure()))
    relief1.valve_operation(75)
    print(relief1.read_position())
    relief1.valve_operation(73)
    print(relief1.read_position())

