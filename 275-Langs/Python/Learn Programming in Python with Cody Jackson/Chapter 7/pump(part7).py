    def pump_power(self, flow_rate, diff_head, fluid_spec_weight=62.4):
        """Calculate pump power in kW.

        Formula from https://www.engineeringtoolbox.com/pumps-power-d_505.html.
        Because imperial values are converted to metric, the calculation isn't exactly the formula listed on the site; view the site's source code to see the formula used.
		"""
        flow_rate = flow_rate / 15852
        density = fluid_spec_weight / 0.0624
        head = diff_head / 3.2808
        hyd_power = (100 * (flow_rate * density * GRAVITY * head) / 1000) / 100
        self.power = hyd_power
        return self.power
