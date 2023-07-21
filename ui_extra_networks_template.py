import json
import os
import prompt_template
import html

from modules import shared, ui_extra_networks


class ExtraNetworksPageTemplate(ui_extra_networks.ExtraNetworksPage):

    def __init__(self):
        super().__init__('Templates')

    def refresh(self):
        prompt_template.list_available_templates()

    def list_items(self):
        for index, (name, template_file) in enumerate(prompt_template.available_templates.items()):
            path, ext = os.path.splitext(template_file.filename)

            onclick = '"' + html.escape(f"""return cardClickedAddOnly({json.dumps(template_file.prompt)}, {"true" if self.allow_negative_prompt else "false"})""") + '"'

            yield {
                "name": name,
                "filename": path,
                "preview": self.find_preview(path),
                "description": self.find_description(path),
                "search_term": self.search_terms_from_path(template_file.filename),
                "onclick": onclick,
                "local_preview": f"{path}.{shared.opts.samples_format}",
                "sort_keys": {'default': index, **self.get_sort_keys(template_file.filename)},
            }

    def allowed_directories_for_previews(self):
        return [shared.cmd_opts.template_dir]

