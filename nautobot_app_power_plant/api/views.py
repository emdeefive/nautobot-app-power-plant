"""API views for nautobot_app_power_plant."""

from nautobot.apps.api import NautobotModelViewSet

from nautobot_app_power_plant import filters, models
from nautobot_app_power_plant.api import serializers


class NautobotAppPowerPlantExampleModelViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """NautobotAppPowerPlantExampleModel viewset."""

    queryset = models.NautobotAppPowerPlantExampleModel.objects.all()
    serializer_class = serializers.NautobotAppPowerPlantExampleModelSerializer
    filterset_class = filters.NautobotAppPowerPlantExampleModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
