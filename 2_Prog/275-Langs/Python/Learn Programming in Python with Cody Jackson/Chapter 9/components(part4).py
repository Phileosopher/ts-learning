# Pump inlet manifold
# 16 inch to 4 inch connections
gate1 = valve.Gate("Gate valve 1", sys_flow_in=tank1.flow_out, press_in=tank1.static_tank_press)
gate1.calc_coeff(16)

gate2 = valve.Gate("Gate valve 2", sys_flow_in=tank2.flow_out, press_in=tank2.static_tank_press)
gate2.calc_coeff(16)

gate3 = valve.Gate("Gate valve 3")
gate3.calc_coeff(16)

gate4 = valve.Gate("Gate valve 4")
gate4.calc_coeff(16)

gate5 = valve.Gate("Gate valve 5")
gate5.calc_coeff(4)
