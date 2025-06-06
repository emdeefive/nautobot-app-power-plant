"""Test NautobotAppPowerPlantExampleModel Filter."""

from nautobot.apps.testing import FilterTestCases

from nautobot_app_power_plant import filters, models
from nautobot_app_power_plant.tests import fixtures


class NautobotAppPowerPlantExampleModelFilterTestCase(FilterTestCases.FilterTestCase):
    """NautobotAppPowerPlantExampleModel Filter Test Case."""

    queryset = models.NautobotAppPowerPlantExampleModel.objects.all()
    filterset = filters.NautobotAppPowerPlantExampleModelFilterSet
    generic_filter_tests = (
        ("id",),
        ("created",),
        ("last_updated",),
        ("name",),
    )

    @classmethod
    def setUpTestData(cls):
        """Setup test data for NautobotAppPowerPlantExampleModel Model."""
        fixtures.create_nautobotapppowerplantexamplemodel()

    def test_q_search_name(self):
        """Test using Q search with name of NautobotAppPowerPlantExampleModel."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for NautobotAppPowerPlantExampleModel."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
