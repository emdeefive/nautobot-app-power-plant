"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from nautobot_app_power_plant import models
from nautobot_app_power_plant.tests import fixtures


class NautobotAppPowerPlantExampleModelViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the NautobotAppPowerPlantExampleModel views."""

    model = models.NautobotAppPowerPlantExampleModel
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }

    update_data = {
        "name": "Test 2",
        "description": "Updated model",
    }

    @classmethod
    def setUpTestData(cls):
        fixtures.create_nautobotapppowerplantexamplemodel()
