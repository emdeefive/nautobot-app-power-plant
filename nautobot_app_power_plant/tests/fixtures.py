"""Create fixtures for tests."""

from nautobot_app_power_plant.models import NautobotAppPowerPlantExampleModel


def create_nautobotapppowerplantexamplemodel():
    """Fixture to create necessary number of NautobotAppPowerPlantExampleModel for tests."""
    NautobotAppPowerPlantExampleModel.objects.create(name="Test One")
    NautobotAppPowerPlantExampleModel.objects.create(name="Test Two")
    NautobotAppPowerPlantExampleModel.objects.create(name="Test Three")
