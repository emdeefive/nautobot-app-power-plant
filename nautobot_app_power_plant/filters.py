"""Filtering for nautobot_app_power_plant."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from nautobot_app_power_plant import models


class UPSModelFilterSet(NameSearchFilterSet, NautobotFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for UPSModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.UPSModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = "__all__"
