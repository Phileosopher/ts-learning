       pump_properties3 = {}

        # Convert instances to dictionaries
        for key, value in vars(components.tank1).items():
            tank_properties1[key] = value
        for key, value in vars(components.tank2).items():
            tank_properties2[key] = value

        for key, value in vars(components.gate1).items():
            valve_properties1[key] = value
        for key, value in vars(components.gate2).items():
            valve_properties2[key] = value
        for key, value in vars(components.gate3).items():
            valve_properties3[key] = value
