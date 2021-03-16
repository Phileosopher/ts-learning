# Gate valve 5
def gate5_open():
    ffc.gate5.open()
    ffc.pump1.head_in = utility_formulas.press_to_head(ffc.gate5.press_out)

def gate5_close():
    ffc.gate5.close()
	ffc.pump1.head_in = 0.0

# Gate valve 6
def gate6_open():
    ffc.gate6.open()
    ffc.pump2.head_in = utility_formulas.press_to_head(ffc.gate6.press_out)

def gate6_close():
    ffc.gate6.close()
    ffc.pump2.head_in = 0.0
