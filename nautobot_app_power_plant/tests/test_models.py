"""Test UPSModel."""

from nautobot.apps.testing import ModelTestCases

from nautobot_app_power_plant import models
from nautobot_app_power_plant.tests import fixtures


class TestUPSModel(ModelTestCases.BaseModelTestCase):
    """Test UPSModel."""

    model = models.UPSModel

    @classmethod
    def setUpTestData(cls):
        """Create test data for UPSModel Model."""
        super().setUpTestData()
        # Create 3 objects for the model test cases.
        fixtures.create_nautobotapppowerplantexamplemodel()

    def test_create_nautobotapppowerplantexamplemodel_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        nautobotapppowerplantexamplemodel = models.UPSModel.objects.create(name="Development")
        self.assertEqual(nautobotapppowerplantexamplemodel.name, "Development")
        self.assertEqual(nautobotapppowerplantexamplemodel.description, "")
        self.assertEqual(str(nautobotapppowerplantexamplemodel), "Development")

    def test_create_nautobotapppowerplantexamplemodel_all_fields_success(self):
        """Create UPSModel with all fields."""
        nautobotapppowerplantexamplemodel = models.UPSModel.objects.create(name="Development", description="Development Test")
        self.assertEqual(nautobotapppowerplantexamplemodel.name, "Development")
        self.assertEqual(nautobotapppowerplantexamplemodel.description, "Development Test")
