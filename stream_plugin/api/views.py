from nautobot.core.api.views import ModelViewSet

from stream_plugin import models, filters
from stream_plugin.api import serializers


class AquariumViewSet(ModelViewSet):
    queryset = models.Aquarium.objects.all()
    serializer_class = serializers.AquariumSerializer
    filterset_class = filters.AquariumFilterSet
