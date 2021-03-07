import sys

sys.path.extend(["/home/cody/PycharmProjects/VirtualPLC"])
from PipingSystems.valve.valve import Globe


class TestGlobe():
    def test_read_position(self):
        g = Globe(name="Globe1", flow_coeff=21)
        assert g.read_position() == "Globe1 is 0% open."

    def test_turn_handle(self):
        g = Globe(name="Globe1", flow_coeff=21)
        g.turn_handle(40)
        assert g.read_position() == "Globe1 is 40% open."

    def test_open(self):
        g = Globe(name="Globe1", flow_coeff=21)
        g.open()
        assert g.read_position() == "Globe1 is 100% open."

    def test_close(self):
        g = Globe(name="Globe1", flow_coeff=21)
        g.close()
        assert g.read_position() == "Globe1 is 0% open."
