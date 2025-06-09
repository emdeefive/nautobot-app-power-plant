"""Models for Nautobot App Power Plant."""

# Django imports
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Nautobot imports
from nautobot.apps.models import PrimaryModel, extras_features

# If you want to choose a specific model to overload in your class declaration, please reference the following documentation:
# how to chose a database model: https://docs.nautobot.com/projects/core/en/stable/plugins/development/#database-models
# If you want to use the extras_features decorator please reference the following documentation
# https://docs.nautobot.com/projects/core/en/stable/development/core/model-checklist/#extras-features
class PowerPlantModel(PrimaryModel):  # pylint: disable=too-many-ancestors
    """Abstract Model for Nautobot Power Plan Models."""

    # name = models.CharField(max_length=25, unique=True)
    # description = models.CharField(max_length=200, blank=True)
    # additional model fields

    class Meta:
        """Meta class."""

        # Option for fixing capitalization (i.e. "Snmp" vs "SNMP")
        # verbose_name = "Nautobot App Power Plant"

        abstract = True

        # Option for fixing plural name (i.e. "Chicken Tenders" vs "Chicken Tendies")
        # verbose_name_plural = "Nautobot App Power Plants"

    def __str__(self):
        """Stringify instance."""
        return self.name

@extras_features(
    "custom_fields",
    "custom_links",
    "custom_validators",
    "export_templates",
    "graphql",
    "relationships",
    "webhooks",
)
class UPSModel(PowerPlantModel):
    """Model for DNS SOA Records. An SOA Record defines a DNS Zone."""

    ordering = ["name"]
    name = models.CharField(max_length=25, help_text="Name of UPS", unique=True)
    description = models.TextField(help_text="Description of the UPS.", blank=True)
    location = models.CharField(
        max_length=200,
        help_text="Location of the UPS.",
        null=False,
        default="Unknown Location",
    )
    capacity = models.PositiveIntegerField(
        help_text="Capacity of the UPS in VA.",
        validators=[MinValueValidator(1)],
        default=1,
    )
    manufacturer = models.CharField(
        max_length=100,
        help_text="Manufacturer of the UPS.",
        null=False,
        default="Unknown Manufacturer",
    )
    model_number = models.CharField(
        max_length=100,
        help_text="Model number of the UPS.",
        null=False,
        default="Unknown Model Number",
    )
    serial_number = models.CharField(
        max_length=100,
        help_text="Serial number of the UPS.",
        null=False,
        default="Unknown Serial Number",
    )
    firmware_version = models.CharField(
        max_length=100,
        help_text="Firmware version of the UPS.",
        null=True,
        blank=True,
    )
    last_maintenance_date = models.DateField(
        help_text="Date of the last maintenance performed on the UPS.",
        null=True,
        blank=True,
    )
    last_test_date = models.DateField(
        help_text="Date of the last test performed on the UPS.",
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=50,
        help_text="Status of the UPS (e.g., Active, Inactive, Maintenance).",
        null=False,
        default="Active",
        choices=[
            ("Active", "Active"),
            ("Inactive", "Inactive"),
            ("Maintenance", "Maintenance"),
            ("Faulty", "Faulty"),
        ],
    )
    notes = models.TextField(
        help_text="Additional notes about the UPS.",
        blank=True,
    )

    class Meta:
        """Meta attributes for UPSModel."""

        verbose_name = "UPS Model"
        verbose_name_plural = "UPS Model"

