"""Views for nautobot_app_power_plant."""

from nautobot.apps.views import NautobotUIViewSet
from nautobot.apps.ui import (
    ButtonColorChoices,
    ObjectDetailContent,
    ObjectFieldsPanel,
    ObjectsTablePanel,
    SectionChoices,
    StatsPanel,
)

from nautobot_app_power_plant import filters, forms, models, tables
from nautobot_app_power_plant.api import serializers


class UPSModelUIViewSet(NautobotUIViewSet):
    """ViewSet for UPSModel views."""

    bulk_update_form_class = forms.UPSModelBulkEditForm
    filterset_class = filters.UPSModelFilterSet
    filterset_form_class = forms.UPSModelFilterForm
    form_class = forms.UPSModelForm
    lookup_field = "pk"
    queryset = models.UPSModel.objects.all()
    serializer_class = serializers.UPSModelSerializer
    table_class = tables.UPSModelTable
    base_template = "generic/object_retrieve.html"

    object_detail_content = ObjectDetailContent(
        panels=[
            ObjectFieldsPanel(
                weight=100,
                section=SectionChoices.LEFT_HALF,
                fields="__all__",
            )
        ],
    )