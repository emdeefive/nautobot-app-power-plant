"""Django API urlpatterns declaration for nautobot_app_power_plant app."""

from nautobot.apps.api import OrderedDefaultRouter

from nautobot_app_power_plant.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("nautobot-app-power-plant-example-models", views.NautobotAppPowerPlantExampleModelViewSet)

app_name = "nautobot_app_power_plant-api"
urlpatterns = router.urls
