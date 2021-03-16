    def test_v3_input_flow(self):
        valve3.flow_in = valve2.flow_out
        assert valve3.flow_in == 50.0

    def test_v3_output_flow(self):
        valve3.flow_out = valve3.flow_in
        assert valve3.flow_out == 50.0

    def test_v3_press_drop(self):
        valve3.press_drop(valve3.flow_out)
        assert valve3.deltaP == 0.0625

    def test_v3_press_out(self):
        valve3.get_press_out(valve3.press_in)
        assert valve3.press_out == 10.206065759637188
