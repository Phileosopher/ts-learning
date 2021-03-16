    def test_v4_output_flow(self):
        valve4.flow_out = valve4.flow_in
        assert valve4.flow_out == 28.8

    def test_v4_press_drop(self):
        valve4.press_drop(valve4.flow_out)
        assert valve4.deltaP == 0.020736000000000004

    def test_v4_press_out(self):
        valve4.get_press_out(valve4.press_in)
        assert valve4.press_out == 28.098447673469387
