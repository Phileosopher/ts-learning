gate6 = valve.Gate("Gate valve 6", sys_flow_in=gate3.flow_out + gate4.flow_out,
                   press_in=gate3.press_out + gate4.press_out)
gate6.calc_coeff(4)

gate7 = valve.Gate("Gate valve 7")
gate7.calc_coeff(4)

# Fuel pumps @ 1480 rpm
pump1 = pump.PositiveDisplacement("Pump 1", flow_rate_out=0.0,                     pump_head_in=utility_formulas.press_to_head(gate5.press_out), displacement=0.24)

pump2 = pump.PositiveDisplacement("Pump 2", flow_rate_out=0.0, pump_head_in=utility_formulas.press_to_head(gate6.press_out), displacement=0.24)

pump3 = pump.PositiveDisplacement("Pump 3", flow_rate_out=0.0, pump_head_in=utility_formulas.press_to_head(gate7.press_out), displacement=0.24)
