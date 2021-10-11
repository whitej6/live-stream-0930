from nautobot.core.views import generic

from stream_plugin import filters, models, tables, forms


class AquariumListView(generic.ObjectListView):
    queryset = models.Aquarium.objects.all()
    filterset = filters.AquariumFilterSet
    filterset_form = forms.AquariumFilterForm
    table = tables.AquariumTable
    action_buttons = ("add",)


class AquariumEditView(generic.ObjectEditView):
    queryset = models.Aquarium.objects.all()
    model_form = forms.AquariumForm


class AquariumDetailView(generic.ObjectView):
    # template_name = "stream_plugin/aquarium2.html"
    queryset = models.Aquarium.objects.all()


class AquariumDeleteView(generic.ObjectDeleteView):
    queryset = models.Aquarium.objects.all()
