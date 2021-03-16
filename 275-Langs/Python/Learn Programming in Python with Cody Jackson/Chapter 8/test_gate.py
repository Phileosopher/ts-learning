import sys
sys.path.extend(["/home/cody/PycharmProjects/VirtualPLC"])
from PipingSystems.valve.valve import Gate


class TestGate():
    def test_read_position(self):
        g = Gate(name="Gate1")
        assert g.read_position() == "Gate1 is closed."
        g.open()
        assert g.read_position() == "Gate1 is open."
        g.position = 50
        assert g.read_position() == "Warning! Gate1 is partially open."

    def test_turn_handle(self):
        g = Gate(name="Gate1")
        g.turn_handle(100)
        assert g.read_position() == "Gate1 is open."
        g.turn_handle(0)
        assert g.read_position() == "Gate1 is closed."
        assert g.turn_handle(50) == "Warning: Invalid valve position."
