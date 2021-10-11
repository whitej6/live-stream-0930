from django.urls import path
from nautobot.extras.views import ObjectChangeLogView

from stream_plugin import views, models

urlpatterns = [
    path("aquarium/", views.AquariumListView.as_view(), name="aquarium_list"),
    path("aquarium/add/", views.AquariumEditView.as_view(), name="aquarium_add"),
    path("aquarium/<uuid:pk>/", views.AquariumDetailView.as_view(), name="aquarium"),
    path("aquarium/<uuid:pk>/edit/", views.AquariumEditView.as_view(), name="aquarium_edit"),
    path("aquarium/<uuid:pk>/delete/", views.AquariumDeleteView.as_view(), name="aquarium_delete"),
    path(
        "aquarium/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="aquarium_changelog",
        kwargs={"model": models.Aquarium},
    ),
]
