"""Django urlpatterns declaration for nautobot_app_power_plant app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter


from nautobot_app_power_plant import views


app_name = "nautobot_app_power_plant"
router = NautobotUIViewSetRouter()

# The standard is for the route to be the hyphenated version of the model class name plural.
# for example, ExampleModel would be example-models.
router.register("nautobot-app-power-plant-example-models", views.NautobotAppPowerPlantExampleModelUIViewSet)


urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("nautobot_app_power_plant/docs/index.html")), name="docs"),
]

urlpatterns += router.urls
