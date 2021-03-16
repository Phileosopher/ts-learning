# Fix the drawing to a set size and prevent scaling
Config.set("graphics", "width", "1112")
Config.set("graphics", "height", "849")
Config.set("graphics", "resizable", False)

class HMILayout(PageLayout):
    # Methods are associated with their class; each class would have its own .kv file
    @staticmethod
    def on_state(device):  # Get the status of the device
        if device.state == "down":
            if device.group not in ["pump1", "pump2", "pump3"]:
                exec("functionality.{}_open()".format(device.group))  # Dynamically call valve open()
            else:
                exec("functionality.{}_on()".format(device.group))  # Dynamically call pump on()
