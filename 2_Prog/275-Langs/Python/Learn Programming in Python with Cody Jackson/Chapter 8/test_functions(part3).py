class TestSystem:
    # Gate Valve 1
    def test_v1_press_in(self):
        assert valve1.press_in == 6.068373888888889

    def test_v1_flow_in(self):
        assert valve1.flow_in == 319.28008077388426

    def test_v1_flow_out(self):
        valve1.flow_out = valve1.flow_in
        assert valve1.flow_out == 319.28008077388426
