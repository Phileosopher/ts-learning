    def test_v1_press_drop(self):
        valve1.press_drop(valve1.flow_out)
        assert valve1.deltaP == 2.5484942494744516

    def test_v1_press_out(self):
        valve1.get_press_out(valve1.press_in)
        assert valve1.press_out == 3.5198796394144374

    # Centrifugal Pump
    def test_pump1_input_press(self):
        pump1.head_in = utility_formulas.press_to_head(valve1.press_out)
        assert pump1.head_in == 8.119222584669064
