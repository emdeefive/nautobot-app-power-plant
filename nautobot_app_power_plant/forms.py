"""Forms for nautobot_app_power_plant."""

from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from nautobot_app_power_plant import models


class UPSModelForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """UPSModel creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.UPSModel
        fields = "__all__"


class UPSModelBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """UPSModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.UPSModel.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class UPSModelFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.UPSModel
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name.",
    )
    name = forms.CharField(required=False, label="Name")
