import ui_extra_networks_template
from modules import script_callbacks, ui_extra_networks, shared

def pages_hide():
    tab_hide = [x.lower().strip() for x in shared.opts.ui_extra_networks_tab_hide.split(",")]
    tab_show = []

    for network in ui_extra_networks.extra_pages:
        title = network.title.lower().strip()

        if title in tab_hide:
            continue
        tab_show.append(network)

    return tab_show

def before_ui():
    ui_extra_networks.register_page(ui_extra_networks_template.ExtraNetworksPageTemplate())

    ui_extra_networks.extra_pages = pages_hide()

script_callbacks.on_before_ui(before_ui)

shared.options_templates.update(shared.options_section(('extra_networks', "Extra Networks"), {
    "ui_extra_networks_tab_hide": shared.OptionInfo("", "Hide Extra networks tab").needs_restart()
}))