"""Test UPSModel Filter."""

from nautobot.apps.testing import FilterTestCases

from nautobot_app_power_plant import filters, models
from nautobot_app_power_plant.tests import fixtures


class UPSModelFilterTestCase(FilterTestCases.FilterTestCase):
    """UPSModel Filter Test Case."""

    queryset = models.UPSModel.objects.all()
    filterset = filters.UPSModelFilterSet
    generic_filter_tests = (
        ("id",),
        ("created",),
        ("last_updated",),
        ("name",),
    )

    @classmethod
    def setUpTestData(cls):
        """Setup test data for UPSModel Model."""
        fixtures.create_nautobotapppowerplantexamplemodel()

    def test_q_search_name(self):
        """Test using Q search with name of UPSModel."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for UPSModel."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
