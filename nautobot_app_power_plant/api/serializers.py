"""API serializers for nautobot_app_power_plant."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from nautobot_app_power_plant import models


class NautobotAppPowerPlantExampleModelSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """NautobotAppPowerPlantExampleModel Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.NautobotAppPowerPlantExampleModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
