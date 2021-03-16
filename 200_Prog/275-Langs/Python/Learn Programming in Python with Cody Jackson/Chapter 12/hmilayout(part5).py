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
