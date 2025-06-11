# template_content.py
from nautobot.extras.plugins import PluginTemplateExtension

from nautobot_app_power_plant.models import UPSModel

class PowerPanelUPS(PluginTemplateExtension):
    """Template extension to display associated UPS object on the right side of the page."""

    model = "dcim.powerpanel"
    template = "nautobot_app_power_plant/power_panel_ups.html"

    def right_page(self):
        obj = self.context["object"]
        ups = UPSModel.objects.get(power_panel=obj)
        if not ups:
            return "nautobot_app_power_plant/blank.html"
        #return ups.name
        return self.render(
            self.template,
            extra_context={
                "object": obj.name,
                "ups": ups,
            },
        )


template_extensions = [PowerPanelUPS]