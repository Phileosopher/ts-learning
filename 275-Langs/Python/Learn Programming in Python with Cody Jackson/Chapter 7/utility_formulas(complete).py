#!/usr/bin/env python3

import math

GRAVITY = 32.174  # ft/s^2
WATER_SPEC_WEIGHT = 62.4  # lb/ft^3
WATER_DENSITY = 1.94  # slugs/ft^3
WATER_SPEC_GRAV = 1.0


def gravity_flow_rate(diameter, slope, rough_coeff=140):
    """Calculates approximate fluid flow due to gravity.

    Should be within 5% of actual value.

    Based on the Hazen-Williams equation (https://en.wikipedia.org/wiki/Hazen–Williams_equation). Assumes a 2 inch,
    polyethylene pipe.

    :param diameter: Pipe diameter, in inches
    :param slope: Slope of pipe, from reservoir to measure point
    :param rough_coeff: Roughness coefficient of pipe

    :return: Approximate fluid flow rate, in gpm
    """
    coeff = math.pow(rough_coeff, 1.852)
    diam = math.pow(diameter, 4.8704)
    root_flow = math.sqrt(((coeff * diam * slope) / 4.52))
    return root_flow


def static_press(height, density=WATER_DENSITY):
    """Calculate static pressure for any fluid.

    :param height: Fluid height, in feet
    :param density: Fluid density. Default assumes water.

    :return: Fluid pressure, in psi
    """
    press = density * GRAVITY * height / 144
    return press


def press_to_head(press, spec_grav=WATER_SPEC_GRAV):
    """Calculate fluid head from pressure.

    :param press: Fluid pressure, in psi
    :param spec_grav: Specific gravity of fluid

    :return: Fluid head, in feet
    """
    head = (74.215 * press) / (spec_grav * GRAVITY)
    return head


def head_to_press(head, spec_grav=WATER_SPEC_GRAV):
    """Calculate pressure from fluid head.

    :param head: Fluid head, in feet
    :param spec_grav: Specific gravity of fluid

    :return: Fluid pressure, in psi
    """
    press = (spec_grav * GRAVITY * head) / 74.215
    return press


if __name__ == "__main__":
    print(gravity_flow_rate(2, 0.6))
    print(static_press(150))
    print(press_to_head(65.0))
    print(head_to_press(150))

