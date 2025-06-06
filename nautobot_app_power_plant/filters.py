"""Filtering for nautobot_app_power_plant."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from nautobot_app_power_plant import models


class NautobotAppPowerPlantExampleModelFilterSet(NameSearchFilterSet, NautobotFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for NautobotAppPowerPlantExampleModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.NautobotAppPowerPlantExampleModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = "__all__"
