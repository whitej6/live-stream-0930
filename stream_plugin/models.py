from django.db import models
from django.urls import reverse
from nautobot.core.models.generics import PrimaryModel
from nautobot.extras.utils import extras_features


@extras_features("custom_validators", "relationships", "graphql")
class Aquarium(PrimaryModel):
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    volume = models.IntegerField(editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Aquarium Model"
        verbose_name_plural = "Aquariums"

    def save(self, *args, **kwargs):
        self.volume = self.length * self.width * self.height / 231
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:stream_plugin:aquarium", args=[self.pk])
