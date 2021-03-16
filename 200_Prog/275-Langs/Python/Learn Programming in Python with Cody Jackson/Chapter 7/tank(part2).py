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
