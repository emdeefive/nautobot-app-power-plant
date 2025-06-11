"""
This job creates dummy data for DB to allow for quick cloning and iteration on backup_importer.

It creates the required objects for backup_importer runs and tests:
    Locations
    Manufacturers
    Device Types
    Platform
    Roles

"""

import itertools
from typing import List

from nautobot.apps.jobs import Job, register_jobs
from nautobot.dcim.models import (
    Location,
    LocationType,
    Platform,
    Manufacturer,
    DeviceType,
    InterfaceTemplate,
)
from nautobot.extras.models import (
    Status,
    Role,
    Secret,
    SecretsGroup,
    SecretsGroupAssociation,
    CustomField,
    CustomFieldChoice,
)
from django.contrib.contenttypes.models import ContentType

name = "Create Dummy Data"
SECRETS = [
    {
        "secret_name": "GITHUB_USER",
        "provider": "environment-variable",
        "secret_type": "username",
        "access_type": "HTTP(S)",
    },
    {
        "secret_name": "GITHUB_TOKEN",
        "provider": "environment-variable",
        "secret_type": "token",
        "access_type": "HTTP(S)",
    },
]
LOCATION_CONTENT_TYPES = [
    "dcim.device",
    "ipam.namespace",
    "ipam.prefix",
    "ipam.vlan",
    "ipam.vlangroup",
]
DEVICE_ROLES = ["GW", "SW", "S"]
INTERFACE_ROLES = [
    "Bridge",
    "Data and Voice",
    "Access",
    "Transit",
    "Layer3 Interface",
    "Null",
    "Management",
    "Layer3 Edge",
    "Loopback",
    "VXLAN",
    "Virtual",
    "Trunk",
]
DEVICE_MODELS = [
    {
        "manufacturer": "Arista",
        "platform": "EOS",
        "model": "CCS-720XP-48ZC2",
        "intf_lists": [
            [f"Ethernet{x}" for x in range(1, 53)],
            [
                f"Ethernet{x}/{y}"
                for x, y in (itertools.product(*[range(53, 55), range(1, 5)]))
            ],
        ],
    },
    {
        "manufacturer": "Arista",
        "platform": "EOS",
        "model": "DCS-7050SX3-48YC8",
        "intf_lists": [
            [f"Ethernet{x}" for x in range(1, 49)],
            [
                f"Ethernet{x}/{y}"
                for x, y in (itertools.product(*[range(49, 57), range(1, 5)]))
            ],
        ],
    },
    {
        "manufacturer": "Arista",
        "platform": "EOS",
        "model": "CCS-720XP-96ZC2",
        "intf_lists": [
            [f"Ethernet{x}" for x in range(1, 103)],
            [
                f"Ethernet{x}/{y}"
                for x, y in (itertools.product(*[range(97, 99), range(1, 5)]))
            ],
        ],
    },
]
CUSTOM_FIELDS = {
    "core": {
        "data": {
            "label": "Additional Config",
            "key": "additional_config",
            "type": "json",
            "weight": 100,
            "content_types": ["dcim.interface"],
            "required": False,
        },
    },
}

class CreateDummyData(Job):
    """This job creates dummy data for DB to allow for quick cloning and iteration on backup_importer."""

    class Meta:
        """This job creates dummy data for DB to allow for quick cloning and iteration on backup_importer."""

        name = "Create Dummy Data"
        description = "This job creates dummy data for DB to allow for quick cloning and iteration on backup_importer."
        has_sensitive_variables = False
        read_only = False

    def run(self, **kwargs):  # pylint: disable=arguments-differ
        """This job creates dummy data for DB to allow for quick cloning and iteration on backup_importer."""

        self.created_secrets_group = self.create_secrets()

        self.create_locations()
        self.create_roles()

        for model in DEVICE_MODELS:
            d_type = self.create_device_types_and_intfs(model)
            self.create_intfs(model, d_type)

        self.create_custom_fields()

    def create_secrets(self) -> SecretsGroup:
        """Creates dummy secrets and secrets groups to be used for iterating on backup_importer.py job.

        Args:
            self: self

        Returns:
            created_secrets_group (SecretsGroup): SecretsGroup object that was created.
        """
        created_secrets_group, created = SecretsGroup.objects.get_or_create(
            name="Github"
        )
        if created:
            self.logger.info("Created SecretsGroup: `%s`", created_secrets_group)
            created_secrets_group.validated_save()

        for secret in SECRETS:
            created_secret, created = Secret.objects.get_or_create(
                name=secret["secret_name"],
                defaults={
                    "provider": secret["provider"],
                    "parameters": {"variable": secret["secret_name"]},
                },
            )
            if created:
                self.logger.info("Created Secret: `%s`", created_secret)
            else:
                created_secret.provider = secret["provider"]
                created_secret.parameters = {"variable": secret["secret_name"]}
            created_secret.validated_save()

            sg_ass, created = SecretsGroupAssociation.objects.get_or_create(
                secrets_group_id=created_secrets_group.id,
                secret_id=created_secret.id,
                secret_type=secret["secret_type"],
                access_type=secret["access_type"],
            )
            if created:
                self.logger.info("Created SecretsGroupAssociation: `%s`", sg_ass)
                sg_ass.validated_save()
        return created_secrets_group

    def create_locations(self) -> None:
        """Create dummy location to be used for iterating on backup_importer.py job.

        Args:
            self: self

        Returns:
            None: None
        """
        region_loc_type, created = LocationType.objects.get_or_create(name="Region")
        if created:
            self.logger.info("Created LocationType: `%s`", region_loc_type)
            region_loc_type.validated_save()

        site_loc_type, created = LocationType.objects.get_or_create(
            name="Site",
            parent=LocationType.objects.get(name="Region"),
        )
        if created:
            self.logger.info("Created LocationType: `%s`", site_loc_type)
        ct_ids = [
            ContentType.objects.get(model=ct.split(".")[1]).id
            for ct in LOCATION_CONTENT_TYPES
        ]
        site_loc_type.content_types.set(ct_ids)
        site_loc_type.validated_save()

        region, created = Location.objects.get_or_create(
            name="Region-1",
            status=Status.objects.get(name="Active"),
            location_type=LocationType.objects.get(name="Region"),
        )
        if created:
            self.logger.info("Created Location: `%s`", region)
            region.validated_save()
        site, created = Location.objects.get_or_create(
            name="Site-1",
            status=Status.objects.get(name="Active"),
            location_type=LocationType.objects.get(name="Site"),
            parent=Location.objects.get(name="Region-1"),
        )
        if created:
            self.logger.info("Created Location: `%s`", site)
            site.validated_save()

    def create_roles(self) -> None:
        """Create dummy roles to be used for iterating on backup_importer.py job.

        Args:
            self: self

        Returns:
            None: None
        """
        for role_name in DEVICE_ROLES:
            role, created = Role.objects.get_or_create(
                name=role_name,
            )
            role.content_types.add(ContentType.objects.get(model="device"))
            role.validated_save()
            if created:
                self.logger.info("Created Role: `%s`", role)

        for role_name in INTERFACE_ROLES:
            role, created = Role.objects.get_or_create(
                name=role_name,
            )
            role.content_types.add(ContentType.objects.get(model="interface"))
            role.validated_save()
            if created:
                self.logger.info("Created Role: `%s`", role)

    def create_device_types_and_intfs(self, model: List[dict]) -> DeviceType:
        """Create dummy Manufacturer, Platform, and DeviceType objects to be used for iterating on backup_importer.py job.

        Args:
            self: self
            model (List[dict]): List of dictionaries that contains relevant data for each model.

        Returns:
            device_type: DeviceType object that is created.
        """
        mfctr, created = Manufacturer.objects.get_or_create(name=model["manufacturer"])
        if created:
            self.logger.info("Created Manfacturer: `%s`", mfctr)
        mfctr.validated_save()

        platform, created = Platform.objects.get_or_create(
            name=model["platform"], manufacturer=mfctr
        )
        if created:
            self.logger.info("Created Platform: `%s`", platform)
        platform.validated_save()

        device_type, created = DeviceType.objects.get_or_create(
            model=model["model"], manufacturer=mfctr
        )
        if created:
            self.logger.info("Created DeviceType: `%s`", device_type)
        device_type.validated_save()
        return device_type

    def create_intfs(self, model: List[dict], d_type: DeviceType) -> None:
        """Create dummy InterfaceTemplates for DeviceType object to be used for iterating on backup_importer.py job.
        Uses interface type "25gbase-x-sfp28" because the interface type does not matter, it just needs to set to something.

        Args:
            self: self
            model (List[dict]): List of dictionaries that contains relevant data for each model.
            d_type (DeviceType): DeviceType object of the device model that interface templates are being created for.

        Returns:
            None: None
        """
        for intf_list in model["intf_lists"]:
            for intf in intf_list:
                intf_template, created = InterfaceTemplate.objects.get_or_create(
                    name=intf,
                    device_type=d_type,
                    defaults={"type": "25gbase-x-sfp28"},
                )
                if created:
                    self.logger.info(
                        "Created InterfaceTemplate `%s` for DeviceType `%s`",
                        intf_template.name,
                        d_type,
                    )
                intf_template.validated_save()

    def create_custom_fields(self):
        """Create CustomFields"""
        for values in CUSTOM_FIELDS.values():
            created_cf, created = CustomField.objects.get_or_create(
                label=values["data"]["label"],
                type=values["data"]["type"],
                key=values["data"]["key"],
                required=values["data"]["required"],
            )
            ct_objs = []
            for content_type_obj in values["data"]["content_types"]:
                ct_app_label = content_type_obj.split(".")[0]
                ct_model = content_type_obj.split(".")[1]
                ct_objs.append(ContentType.objects.get(app_label=ct_app_label, model=ct_model))
            created_cf.content_types.set(ct_objs)
            if values.get("choices", None):
                for choice in values["choices"]:
                    choice["custom_field"] = created_cf
                    CustomFieldChoice.objects.create(**choice)
            # Can only assign default choice after choices have been created
            created_cf.default = values["data"].get("default")
            created_cf.validated_save()
            if created:
                self.logger.info("Created Custom Field: `%s`", created_cf)

register_jobs(CreateDummyData)
