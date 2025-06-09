"""Create fixtures for tests."""

from nautobot_app_power_plant.models import UPSModel


def create_nautobotapppowerplantexamplemodel():
    """Fixture to create necessary number of UPSModel for tests."""
    UPSModel.objects.create(name="Test One")
    UPSModel.objects.create(name="Test Two")
    UPSModel.objects.create(name="Test Three")
