   def test_t1_flow_in(self):
        throttle1.flow_in = pump1.flow
        assert throttle1.flow_in == 50.0

    def test_t1_flow_out(self):
        throttle1.flow_out = throttle1.flow_in
        assert throttle1.flow_out == 50.0

    def test_t1_press_drop(self):
        throttle1.press_drop(throttle1.flow_out)
        assert throttle1.deltaP == 5.668934240362812

    def test_t1_press_out(self):
        throttle1.get_press_out(throttle1.press_in)
        assert throttle1.press_out == 10.331065759637188
