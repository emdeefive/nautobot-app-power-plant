"""Views for nautobot_app_power_plant."""

from nautobot.apps.views import NautobotUIViewSet

from nautobot_app_power_plant import filters, forms, models, tables
from nautobot_app_power_plant.api import serializers


class NautobotAppPowerPlantExampleModelUIViewSet(NautobotUIViewSet):
    """ViewSet for NautobotAppPowerPlantExampleModel views."""

    bulk_update_form_class = forms.NautobotAppPowerPlantExampleModelBulkEditForm
    filterset_class = filters.NautobotAppPowerPlantExampleModelFilterSet
    filterset_form_class = forms.NautobotAppPowerPlantExampleModelFilterForm
    form_class = forms.NautobotAppPowerPlantExampleModelForm
    lookup_field = "pk"
    queryset = models.NautobotAppPowerPlantExampleModel.objects.all()
    serializer_class = serializers.NautobotAppPowerPlantExampleModelSerializer
    table_class = tables.NautobotAppPowerPlantExampleModelTable
