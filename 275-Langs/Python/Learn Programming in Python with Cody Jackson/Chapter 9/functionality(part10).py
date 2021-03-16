# Gate valve 7
def gate7_open():
    ffc.gate7.open()
    ffc.pump3.head_in = utility_formulas.press_to_head(ffc.gate7.press_out)

def gate7_close():
    ffc.gate7.close()
    ffc.pump3.head_in = 0.0

# Gate valve 8
def gate8_open():
    ffc.gate8.open()

def gate8_close():
    ffc.gate8.close()
