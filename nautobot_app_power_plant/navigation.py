"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:nautobot_app_power_plant:upsmodel_list",
        name="UPS",
        permissions=["nautobot_app_power_plant.view_upsmodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_app_power_plant:upsmodel_add",
                permissions=["nautobot_app_power_plant.add_upsmodel"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Nautobot App Power Plant", items=tuple(items)),),
    ),
)
