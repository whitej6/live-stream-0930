import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ButtonsColumn, ToggleColumn

from stream_plugin import models


LENGTH = "<a href='/foo'> bar</a>"


class AquariumTable(BaseTable):
    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(models.Aquarium, buttons=("edit", "delete"))

    class Meta(BaseTable.Meta):

        model = models.Aquarium
        fields = ["pk", "name", "description", "length", "width", "height", "volume", "tags"]
