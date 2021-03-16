if __name__ == "__main__":
    # Functional test_valves
    # name="", flow_rate=0.0, pump_head_in=0.0, press_out=0.0, pump_speed=0, hp=0.0, displacement=0.0
    pump1 = CentrifPump("Pumpy", 75, 12, 25, 125)
    print("{} created.".format(pump1.name))
    print(pump1.get_speed_str())
    print(pump1.get_flow_str())
    print(pump1.get_power_str())
    print(pump1.get_press_str())
    pump1.adjust_speed(50)
    print(pump1.get_speed_str())
    print(pump1.get_flow_str())
    print(pump1.get_power_str())
    print(pump1.get_press_str())
    pump1.adjust_speed(0)
    print(pump1.get_speed_str())
    print(pump1.get_flow_str())
    print(pump1.get_power_str())
    print(pump1.get_press_str())
