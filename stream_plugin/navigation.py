from nautobot.extras.plugins import PluginMenuButton, PluginMenuItem
from nautobot.utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link="plugins:stream_plugin:aquarium_list",
        link_text="Aqariums",
        buttons=(
            PluginMenuButton(
                link="plugins:stream_plugin:aquarium_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.BLUE,
                permissions=["stream_plugin.add_aquarium"],
            ),
        ),
    ),
)
