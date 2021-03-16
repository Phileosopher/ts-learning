# Storage tanks
# Assumes 36 ft tall tank w/ 1 million gallon capacity = 27778 gallons per foot
# Assumes 16 inch diam transfer piping
tank1 = tank.Tank("Tank 1", level=36.0, fluid_density=DENSITY, spec_gravity=SPEC_GRAVITY, outlet_diam=16, outlet_slope=0.25)
tank1.static_tank_press = tank1.level
tank1.gravity_flow(tank1.pipe_diam, tank1.pipe_slope, tank1.pipe_coeff)

tank2 = tank.Tank("Tank 2", level=36.0, fluid_density=DENSITY, spec_gravity=SPEC_GRAVITY, outlet_diam=16, outlet_slope=0.25)
tank2.static_tank_press = tank2.level
tank2.gravity_flow(tank2.pipe_diam, tank2.pipe_slope, tank2.pipe_coeff)
