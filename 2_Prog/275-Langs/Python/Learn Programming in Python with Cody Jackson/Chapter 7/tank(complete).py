#!/usr/bin/env python3
"""
VirtualPLC tank.py

Purpose: Creates a generic Tank class for PLC-controlled SCADA systems.

Author: Cody Jackson

Date: 5/28/18
#################################
Version 0.2
    Added path extension to alleviate errors
Version 0.1
    Initial build
"""
import sys
sys.path.extend(["/home/cody/PycharmProjects/VirtualPLC"])
from Utilities import utility_formulas
import numbers


class Tank:
    """Generic storage tank."""
    def __init__(self, name="", level=0.0, fluid_density=1.94, spec_gravity=1.0, outlet_diam=0.0, outlet_slope=0.0):
        self.name = name
        self.__level = float(level)  # feet
        self.fluid_density = fluid_density  # slugs/ft3
        self.spec_grav = spec_gravity
        self.__tank_press = 0.0
        self.flow_out = 0.0
        self.pipe_diam = outlet_diam
        self.pipe_slope = outlet_slope
        self.pipe_coeff = 140

    @property
    def static_tank_press(self):
        """Return hydrostatic tank pressure."""
        return self.__tank_press

    @static_tank_press.setter
    def static_tank_press(self, level):
        """Calculate the static fluid pressure based on tank level."""
        try:
            if not isinstance(level, numbers.Number):
                raise TypeError("Numeric values only.")
            elif level <= 0:
                self.__tank_press = 0.0
            else:
                self.__tank_press = utility_formulas.static_press(self.level, self.fluid_density)
        except TypeError:
            raise  # Re-raise for testing

    @property
    def level(self):
        """Return fluid level in tank."""
        return self.__level

    @level.setter
    def level(self, level):
        """Set the level in the tank."""
        try:
            if not isinstance(level, numbers.Number):
                raise TypeError("Numeric values only.")
            elif level <= 0:
                self.__level = 0.0
            else:
                self.__level = level
        except TypeError:
            raise  # Re-raise error for testing
        finally:
            self.static_tank_press = self.level
            self.gravity_flow(self.pipe_diam, self.pipe_slope, self.pipe_coeff)

    def gravity_flow(self, diameter, slope, pipe_coeff):
        if self.level > 0:
            self.flow_out = utility_formulas.gravity_flow_rate(diameter, slope, pipe_coeff)
        else:
            self.flow_out = 0.0


if __name__ == "__main__":
    tank1 = Tank("tank1", 10)
    print(tank1.level)
    tank1.static_tank_press = tank1.level
    print(tank1.static_tank_press)
    tank1.level = 8.0
    print(tank1.level)
    tank1.static_tank_press = tank1.level
    print(tank1.static_tank_press)
    tank1.level = "a"
    print(tank1.level)

