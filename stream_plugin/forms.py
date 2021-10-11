from django import forms
from nautobot.extras.models import Tag
from nautobot.extras.forms import CustomFieldFilterForm
from nautobot.utilities.forms import BootstrapMixin, TagFilterField
from nautobot.utilities.forms.fields import DynamicModelMultipleChoiceField

from stream_plugin import models


class AquariumFilterForm(BootstrapMixin, CustomFieldFilterForm):
    model = models.Aquarium
    tags = TagFilterField(model)
    name = forms.CharField(required=False)
    length = forms.IntegerField(required=False)
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
    volume = forms.IntegerField(required=False)
    created = forms.DateField(required=False)


class AquariumForm(BootstrapMixin, forms.ModelForm):
    tags = DynamicModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = models.Aquarium
        fields = ["name", "description", "length", "width", "height", "tags"]
