"""Forms for nautobot_app_power_plant."""

from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from nautobot_app_power_plant import models


class NautobotAppPowerPlantExampleModelForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """NautobotAppPowerPlantExampleModel creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.NautobotAppPowerPlantExampleModel
        fields = "__all__"


class NautobotAppPowerPlantExampleModelBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """NautobotAppPowerPlantExampleModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.NautobotAppPowerPlantExampleModel.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class NautobotAppPowerPlantExampleModelFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.NautobotAppPowerPlantExampleModel
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name.",
    )
    name = forms.CharField(required=False, label="Name")
