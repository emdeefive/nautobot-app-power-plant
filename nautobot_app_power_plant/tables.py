"""Tables for nautobot_app_power_plant."""

import django_tables2 as tables
from nautobot.apps.tables import BaseTable, ButtonsColumn, ToggleColumn

from nautobot_app_power_plant import models


class UPSModelTable(BaseTable):
    # pylint: disable=R0903
    """Table for list view."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    power_panel = tables.Column(linkify=True, verbose_name="Power Panel")
    actions = ButtonsColumn(
        models.UPSModel,
        # Option for modifying the default action buttons on each row:
        buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        # pk_field="pk",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.UPSModel
        fields = (
            "pk",
            "name",
            "description",
            "power_panel",  # Display the name of the related power panel
            "location",
            "capacity",
            "manufacturer",
            "model_number",
            "serial_number",
            "firmware_version",
            "last_maintenance_date",
            "last_test_date",
            "status",
            "notes",
        )

        # Option for modifying the columns that show up in the list view by default:
        default_columns = (
            "pk",
            "name",
            "description",
            "power_panel",
            "capacity",
            "manufacturer",
            "model_number",
            "serial_number",
        )
