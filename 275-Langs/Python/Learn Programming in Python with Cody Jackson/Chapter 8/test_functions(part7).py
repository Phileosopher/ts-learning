    # Gate Valve 2
    def test_v2_input_press(self):
        valve2.press_in = throttle1.press_out
        assert valve2.press_in == 10.331065759637188

    def test_v2_input_flow(self):
        valve2.flow_in = throttle1.flow_out
        assert valve2.flow_in == 50.0

    def test_v2_output_flow(self):
        valve2.flow_out = valve2.flow_in
        assert valve2.flow_out == 50.0
