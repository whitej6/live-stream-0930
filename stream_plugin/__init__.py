from django.apps import config
from nautobot.extras.plugins import PluginConfig


__version__ = "0.0.1"


class MyAquariumPlugin(PluginConfig):
    name = "stream_plugin"
    verbose_name = "This is my fun stream plugin"
    author = "whitej6"
    description = "Plugin to manage crazy big aquariums"
    base_url = "aquapy"
    required_settings = []
    default_settings = {}
    min_version = "1.1.0"
    max_version = "1.9999"
    caching_config = {}


config = MyAquariumPlugin
