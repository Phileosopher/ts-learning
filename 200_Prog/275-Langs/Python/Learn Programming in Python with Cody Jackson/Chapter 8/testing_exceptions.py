   def test_tank_level_str(self):
        tank1 = Tank()
        with pytest.raises(TypeError) as excinfo:
            tank1.level = "a"
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Numeric values only."
