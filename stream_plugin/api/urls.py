from nautobot.core.api import OrderedDefaultRouter

from stream_plugin.api import views


router = OrderedDefaultRouter()
router.register("aquarium", views.AquariumViewSet)

urlpatterns = router.urls
