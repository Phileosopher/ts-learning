    def test_v2_press_drop(self):
        valve2.press_drop(valve2.flow_out)
        assert valve2.deltaP == 0.0625

    def test_v2_press_out(self):
        valve2.get_press_out(valve2.press_in)
        assert valve2.press_out == 10.268565759637188

    # Gate Valve 3
    def test_v3_input_press(self):
        valve3.press_in = valve2.press_out
        assert valve3.press_in == 10.268565759637188
