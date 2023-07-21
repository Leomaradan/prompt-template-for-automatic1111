import ui_extra_networks_template
from modules import script_callbacks, ui_extra_networks

def before_ui():
    ui_extra_networks.register_page(ui_extra_networks_template.ExtraNetworksPageTemplate())

script_callbacks.on_before_ui(before_ui)
