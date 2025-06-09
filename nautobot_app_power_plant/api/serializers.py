"""API serializers for nautobot_app_power_plant."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from nautobot_app_power_plant import models


class UPSModelSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """UPSModel Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.UPSModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
