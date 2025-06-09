"""API views for nautobot_app_power_plant."""

from nautobot.apps.api import NautobotModelViewSet

from nautobot_app_power_plant import filters, models
from nautobot_app_power_plant.api import serializers


class UPSModelViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """UPSModel viewset."""

    queryset = models.UPSModel.objects.all()
    serializer_class = serializers.UPSModelSerializer
    filterset_class = filters.UPSModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
