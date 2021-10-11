from django.contrib.contenttypes import fields
from nautobot.extras.filters import CreatedUpdatedFilterSet
from nautobot.utilities.filters import BaseFilterSet, TagFilter

from stream_plugin import models


class AquariumFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    tags = TagFilter()

    class Meta:
        model = models.Aquarium
        fields = ["id", "length", "height", "width", "volume", "name", "description", "volume"]
