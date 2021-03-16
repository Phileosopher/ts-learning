    def gravity_flow(self, diameter, slope, pipe_coeff):
        if self.level > 0:
            self.flow_out = utility_formulas.gravity_flow_rate(diameter, slope, pipe_coeff)
        else:
            self.flow_out = 0.0


if __name__ == "__main__":
    tank1 = Tank("tank1", 10)
    print(tank1.level)
    tank1.static_tank_press = tank1.level
    print(tank1.static_tank_press)
    tank1.level = 8.0
    print(tank1.level)
    tank1.static_tank_press = tank1.level
    print(tank1.static_tank_press)
    tank1.level = "a"
    print(tank1.level)
