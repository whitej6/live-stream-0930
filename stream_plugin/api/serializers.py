from nautobot.core.api.serializers import ValidatedModelSerializer

from stream_plugin import models


class AquariumSerializer(ValidatedModelSerializer):
    class Meta:
        model = models.Aquarium
        fields = "__all__"
