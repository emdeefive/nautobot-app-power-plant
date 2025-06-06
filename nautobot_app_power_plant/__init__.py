"""App declaration for nautobot_app_power_plant."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class NautobotAppPowerPlantConfig(NautobotAppConfig):
    """App configuration for the nautobot_app_power_plant app."""

    name = "nautobot_app_power_plant"
    verbose_name = "Nautobot App Power Plant"
    version = __version__
    author = "emdeefive"
    description = "Nautobot App Power Plant."
    base_url = "nautobot-app-power-plant"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}
    docs_view_name = "plugins:nautobot_app_power_plant:docs"


config = NautobotAppPowerPlantConfig  # pylint:disable=invalid-name
