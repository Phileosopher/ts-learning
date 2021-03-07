    @staticmethod
    def diff_press_ft(in_press_ft, out_press_ft):
        """Calculate differential head across pump, converted from feet."""
        in_press = utility_formulas.head_to_press(in_press_ft)
        out_press = utility_formulas.head_to_press(out_press_ft)
        delta_p = out_press - in_press
        return delta_p

    @staticmethod
    def diff_press_psi(press_in, press_out):
        """Calculate differential pump head."""
        delta_p = abs(press_out - press_in)  # Account for Pout < Pin
        return delta_p
