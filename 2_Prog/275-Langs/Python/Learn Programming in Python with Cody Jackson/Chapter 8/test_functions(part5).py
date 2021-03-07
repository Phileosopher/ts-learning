
    def test_pump1_start_pump(self):
        pump1.start_pump(1750, 50, 16)
        assert pump1.speed == 1750
        assert pump1.flow == 50.0
        assert pump1.outlet_pressure == 16
        assert pump1.power == 0.11770474358069433

    # Globe valve 1
    def test_t1_press_in(self):
        throttle1.press_in = pump1.outlet_pressure
        assert throttle1.press_in == 16
