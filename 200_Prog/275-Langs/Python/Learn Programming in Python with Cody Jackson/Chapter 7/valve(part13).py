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
