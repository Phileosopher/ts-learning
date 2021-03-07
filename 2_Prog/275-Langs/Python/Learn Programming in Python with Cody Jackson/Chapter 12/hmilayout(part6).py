    def clear(self):
        self.table.data = []

class HMIApp(App):
    def build(self):
        return HMILayout()

if __name__ == "__main__":
    HMIApp().run()
