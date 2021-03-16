class Valve:
    """Generic class for valves.

    Cv is the valve flow coefficient: number of gallons per minute at 60F through a fully open valve with a press. drop of 1 psi. For valves 1 inch or less in diameter, Cv is typically < 5.

    Variables: name, position, Cv, deltaP, flow_in, flow_out, press_out, press_in

    Methods: calc_coeff(), press_drop(), valve_flow_out(), get_press_out(), open(), close()
    """
