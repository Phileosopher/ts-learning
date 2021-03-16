    # Gear Pump
    def test_pump2_input_press(self):
        pump2.head_in = utility_formulas.press_to_head(valve3.press_out)
        assert pump2.head_in == 23.542088964737797

    def test_pump2_output(self):
        pump2.adjust_speed(300)
        assert pump2.speed == 300
        assert pump2.flow == 28.8
        assert pump2.power == 0.10753003776038036

    # Relief Valve 1
    def test_relief1_input_press(self):
        relief1.press_in = pump2.outlet_pressure
        assert relief1.press_in == 30
