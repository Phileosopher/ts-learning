    def start_pump(self, speed, flow, out_press=0.0, out_ft=0.0):
        """System characteristics when a pump is initially started.

        Assumes all valves fully open, i.e. maximum flow rate.

        """
        self.speed = speed
        self.flow = flow
        if out_press > 0.0:
            self.outlet_pressure = out_press
        elif out_ft > 0.0:
            self.outlet_pressure = utility_formulas.head_to_press(out_ft)
        else:
            return "Outlet pump pressure required."
        delta_p = self.outlet_pressure - utility_formulas.head_to_press(self.head_in)
        self.power = self.pump_power(self.flow, delta_p)

        return self.speed, self.flow, self.outlet_pressure, self.power
