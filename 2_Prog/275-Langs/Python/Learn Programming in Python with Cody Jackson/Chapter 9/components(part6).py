# Pump outlet manifold
relief1 = valve.Relief("Relief 1", sys_flow_in=pump1.flow, flow_coeff=0.81)
relief2 = valve.Relief("Relief 2", sys_flow_in=pump2.flow, flow_coeff=0.81)
relief3 = valve.Relief("Relief 3", sys_flow_in=pump3.flow, flow_coeff=0.81)

throttle1 = valve.Globe("Flow Control 1", sys_flow_in=pump1.flow, press_in=pump1.outlet_pressure, flow_coeff=165)
throttle2 = valve.Globe("Flow Control 2", sys_flow_in=pump1.flow, press_in=pump1.outlet_pressure, flow_coeff=165)
throttle3 = valve.Globe("Flow Control 3", sys_flow_in=pump1.flow, press_in=pump1.outlet_pressure, flow_coeff=165)

gate8 = valve.Gate("Gate valve 8", sys_flow_in=throttle3.flow_out, press_in=throttle3.press_out)
gate8.calc_coeff(4)

gate9 = valve.Gate("Gate valve 9", sys_flow_in=throttle1.flow_out, press_in=throttle1.press_out)
gate9.calc_coeff(4)

gate10 = valve.Gate("Gate valve 10", sys_flow_in=throttle3.flow_out, press_in=throttle3.press_out)
gate10.calc_coeff(4)

if __name__ == "__main__":
    pass
