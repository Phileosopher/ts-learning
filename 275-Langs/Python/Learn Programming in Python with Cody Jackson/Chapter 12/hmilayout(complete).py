import Models.FuelFarm.components as components
import Models.FuelFarm.functionality as functionality

from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.config import Config

import kivy
kivy.require("1.10.0")

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
        else:
            if device.group not in ["pump1", "pump2", "pump3"]:
                exec("functionality.{}_close()".format(device.group))  # Dynamically call valve close()
            else:
                exec("functionality.{}_off()".format(device.group))  # Dynamically call pump off()

    def populate(self):
        # Make dictionaries to populate table
        tank_properties1 = {}
        tank_properties2 = {}

        valve_properties1 = {}
        valve_properties2 = {}
        valve_properties3 = {}
        valve_properties4 = {}
        valve_properties5 = {}
        valve_properties6 = {}
        valve_properties7 = {}
        valve_properties8 = {}
        valve_properties9 = {}
        valve_properties10 = {}

        pump_properties1 = {}
        pump_properties2 = {}
        pump_properties3 = {}

        # Convert instances to dictionaries
        for key, value in vars(components.tank1).items():
            tank_properties1[key] = value
        for key, value in vars(components.tank2).items():
            tank_properties2[key] = value

        for key, value in vars(components.gate1).items():
            valve_properties1[key] = value
        for key, value in vars(components.gate2).items():
            valve_properties2[key] = value
        for key, value in vars(components.gate3).items():
            valve_properties3[key] = value
        for key, value in vars(components.gate4).items():
            valve_properties4[key] = value
        for key, value in vars(components.gate5).items():
            valve_properties5[key] = value
        for key, value in vars(components.gate6).items():
            valve_properties6[key] = value
        for key, value in vars(components.gate7).items():
            valve_properties7[key] = value
        for key, value in vars(components.gate8).items():
            valve_properties8[key] = value
        for key, value in vars(components.gate9).items():
            valve_properties9[key] = value
        for key, value in vars(components.gate10).items():
            valve_properties10[key] = value

        for key, value in vars(components.pump1).items():
            pump_properties1[key] = value
        # if valve_properties5["flow_out"] == 0.0:  # if inlet valve closed, ensure no flow through pump
        #     pump_properties1["_Pump__flow_rate_out"] = pump_properties1["_Pump__outlet_pressure"] = 0.0

        for key, value in vars(components.pump2).items():
            pump_properties2[key] = value
        if valve_properties6["flow_out"] == 0.0:
            pump_properties2["_Pump__flow_rate_out"] = pump_properties2["_Pump__outlet_pressure"] = 0.0

        for key, value in vars(components.pump3).items():
            pump_properties3[key] = value
        if valve_properties7["flow_out"] == 0.0:
            pump_properties3["_Pump__flow_rate_out"] = pump_properties3["_Pump__outlet_pressure"] = 0.0

        # Populate table
        self.table.data = [{"value": "Tank"}, {"value": "Level"}, {"value": "Pressure Out"}, {"value": "Flow Out"},
                           {"value": ""}, {"value": ""},
                           # Tank 1
                           {"value": tank_properties1["name"]},
                           {"value": str(tank_properties1["_Tank__level"])},
                           {"value": "{:.2f}".format((tank_properties1["_Tank__tank_press"]))},
                           {"value": "{:.2f}".format((tank_properties1["flow_out"]))},
                           {"value": ""},
                           {"value": ""},
                           # Tank 2
                           {"value": tank_properties2["name"]},
                           {"value": str(tank_properties2["_Tank__level"])},
                           {"value": "{:.2f}".format((tank_properties2["_Tank__tank_press"]))},
                           {"value": "{:.2f}".format((tank_properties2["flow_out"]))},
                           {"value": ""},
                           {"value": ""},

                           # Spacer row
                           {"value": ""}, {"value": ""}, {"value": ""}, {"value": ""}, {"value": ""}, {"value": ""},

                           {"value": "Valve"}, {"value": "Position"}, {"value": "Pressure In"}, {"value": "Flow In"},
                           {"value": "Pressure Out"}, {"value": "Flow Out"},
                           # Valve 1
                           {"value": valve_properties1["name"]},
                           {"value": str(valve_properties1["_Valve__position"])},
                           {"value": "{:.2f}".format((valve_properties1["press_in"]))},
                           {"value": "{:.2f}".format((valve_properties1["flow_in"]))},
                           {"value": "{:.2f}".format((valve_properties1["press_out"]))},
                           {"value": "{:.2f}".format((valve_properties1["flow_out"]))},
                           # Valve 2
                           {"value": valve_properties2["name"]},
                           {"value": str(valve_properties2["_Valve__position"])},
                           {"value": "{:.2f}".format((valve_properties2["press_in"]))},
                           {"value": "{:.2f}".format((valve_properties2["flow_in"]))},
                           {"value": "{:.2f}".format((valve_properties2["press_out"]))},
                           {"value": "{:.2f}".format((valve_properties2["flow_out"]))},
                           # Valve 3
                           {"value": valve_properties3["name"]},
                           {"value": str(valve_properties3["_Valve__position"])},
                           {"value": "{:.2f}".format((valve_properties3["press_in"]))},
                           {"value": "{:.2f}".format((valve_properties3["flow_in"]))},
                           {"value": "{:.2f}".format((valve_properties3["press_out"]))},
                           {"value": "{:.2f}".format((valve_properties3["flow_out"]))},
                           # Valve 4
                           {"value": valve_properties4["name"]},
                           {"value": str(valve_properties4["_Valve__position"])},
                           {"value": "{:.2f}".format((valve_properties4["press_in"]))},
                           {"value": "{:.2f}".format((valve_properties4["flow_in"]))},
                           {"value": "{:.2f}".format((valve_properties4["press_out"]))},
                           {"value": "{:.2f}".format((valve_properties4["flow_out"]))},
                           # Valve 5
                           {"value": valve_properties5["name"]},
                           {"value": str(valve_properties5["_Valve__position"])},
                           {"value": "{:.2f}".format((valve_properties5["press_in"]))},
                           {"value": "{:.2f}".format((valve_properties5["flow_in"]))},
                           {"value": "{:.2f}".format((valve_properties5["press_out"]))},
                           {"value": "{:.2f}".format((valve_properties5["flow_out"]))},
                           # Valve 6
                           {"value": valve_properties6["name"]},
                           {"value": str(valve_properties6["_Valve__position"])},
                           {"value": "{:.2f}".format((valve_properties6["press_in"]))},
                           {"value": "{:.2f}".format((valve_properties6["flow_in"]))},
                           {"value": "{:.2f}".format((valve_properties6["press_out"]))},
                           {"value": "{:.2f}".format((valve_properties6["flow_out"]))},
                           # Valve 7
                           {"value": valve_properties7["name"]},
                           {"value": str(valve_properties7["_Valve__position"])},
                           {"value": "{:.2f}".format((valve_properties7["press_in"]))},
                           {"value": "{:.2f}".format((valve_properties7["flow_in"]))},
                           {"value": "{:.2f}".format((valve_properties7["press_out"]))},
                           {"value": "{:.2f}".format((valve_properties7["flow_out"]))},
                           # Valve 8
                           {"value": valve_properties8["name"]},
                           {"value": str(valve_properties8["_Valve__position"])},
                           {"value": "{:.2f}".format((valve_properties8["press_in"]))},
                           {"value": "{:.2f}".format((valve_properties8["flow_in"]))},
                           {"value": "{:.2f}".format((valve_properties8["press_out"]))},
                           {"value": "{:.2f}".format((valve_properties8["flow_out"]))},
                           # Valve 9
                           {"value": valve_properties9["name"]},
                           {"value": str(valve_properties9["_Valve__position"])},
                           {"value": "{:.2f}".format((valve_properties9["press_in"]))},
                           {"value": "{:.2f}".format((valve_properties9["flow_in"]))},
                           {"value": "{:.2f}".format((valve_properties9["press_out"]))},
                           {"value": "{:.2f}".format((valve_properties9["flow_out"]))},
                           # Valve 10
                           {"value": valve_properties10["name"]},
                           {"value": str(valve_properties10["_Valve__position"])},
                           {"value": "{:.2f}".format((valve_properties10["press_in"]))},
                           {"value": "{:.2f}".format((valve_properties10["flow_in"]))},
                           {"value": "{:.2f}".format((valve_properties10["press_out"]))},
                           {"value": "{:.2f}".format((valve_properties10["flow_out"]))},

                           # Spacer row
                           {"value": ""}, {"value": ""}, {"value": ""}, {"value": ""}, {"value": ""}, {"value": ""},

                           {"value": "Pump"}, {"value": "Speed"}, {"value": "Wattage"}, {"value": "Pressure Out"},
                           {"value": "Flow Out"}, {"value": ""},
                           # Pump 1
                           {"value": pump_properties1["name"]},
                           {"value": "{:.2f}".format((pump_properties1["_Pump__speed"]))},
                           {"value": "{:.2f}".format((pump_properties1["_Pump__wattage"]))},
                           {"value": "{:.2f}".format((pump_properties1["_Pump__outlet_pressure"]))},
                           {"value": "{:.2f}".format((pump_properties1["_Pump__flow_rate_out"]))},
                           {"value": ""},
                           # Pump 2
                           {"value": pump_properties2["name"]},
                           {"value": "{:.2f}".format((pump_properties2["_Pump__speed"]))},
                           {"value": "{:.2f}".format((pump_properties2["_Pump__wattage"]))},
                           {"value": "{:.2f}".format((pump_properties2["_Pump__outlet_pressure"]))},
                           {"value": "{:.2f}".format((pump_properties2["_Pump__flow_rate_out"]))},
                           {"value": ""},
                           # Pump 3
                           {"value": pump_properties3["name"]},
                           {"value": "{:.2f}".format((pump_properties3["_Pump__speed"]))},
                           {"value": "{:.2f}".format((pump_properties3["_Pump__wattage"]))},
                           {"value": "{:.2f}".format((pump_properties3["_Pump__outlet_pressure"]))},
                           {"value": "{:.2f}".format((pump_properties3["_Pump__flow_rate_out"]))},
                           {"value": ""},
                           ]

    def clear(self):
        self.table.data = []


class HMIApp(App):
    def build(self):
        return HMILayout()


if __name__ == "__main__":
    HMIApp().run()
