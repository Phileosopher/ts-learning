def gravity_flow_rate(diameter, slope, rough_coeff=140):
    """Calculates approximate fluid flow due to gravity.

    Should be within 5% of actual value.

    Based on the Hazen-Williams equation (https://en.wikipedia.org/wiki/Hazen–Williams_equation). Assumes a 2 inch, polyethylene pipe
    """
    coeff = math.pow(rough_coeff, 1.852)
    diam = math.pow(diameter, 4.8704)
    root_flow = math.sqrt(((coeff * diam * slope) / 4.52))
    return root_flow
