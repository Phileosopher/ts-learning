    # Globe Valve 2
    def test_t2_input_press(self):
        recirc1.press_in = pump2.outlet_pressure
        assert recirc1.press_in == 30

    def test_t2_input_flow(self):
        recirc1.flow_in = pump2.flow
        assert recirc1.flow_in == 28.8

    def test_t2_output_flow(self):
        recirc1.flow_out = recirc1.flow_in
        assert recirc1.flow_out == 28.8

    def test_2_press_drop(self):
        recirc1.press_drop(recirc1.flow_out)
        assert recirc1.deltaP == 1.8808163265306124
