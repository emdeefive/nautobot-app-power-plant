"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:nautobot_app_power_plant:nautobotapppowerplantexamplemodel_list",
        name="Nautobot App Power Plant",
        permissions=["nautobot_app_power_plant.view_nautobotapppowerplantexamplemodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_app_power_plant:nautobotapppowerplantexamplemodel_add",
                permissions=["nautobot_app_power_plant.add_nautobotapppowerplantexamplemodel"],
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
