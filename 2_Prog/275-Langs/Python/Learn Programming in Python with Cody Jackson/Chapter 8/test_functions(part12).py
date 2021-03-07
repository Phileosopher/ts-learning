    def test_t2_press_out(self):
        recirc1.get_press_out(recirc1.press_in)
        assert recirc1.press_out == 28.119183673469387

    # Gate Valve 4
    def test_v4_input_press(self):
        valve4.press_in = recirc1.press_out
        assert valve4.press_in == 28.119183673469387

    def test_v4_input_flow(self):
        valve4.flow_in = recirc1.flow_out
        assert valve4.flow_in == 28.8
