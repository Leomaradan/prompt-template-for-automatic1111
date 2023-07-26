import os

from modules import shared

class PromptTemplate:
    def __init__(self, filename, name):
        self.filename = filename
        self.name = name

        self.prompt = self.read_template()

    def read_template(self):
        with open(self.filename, "r") as f:
            return f.read()


def list_available_templates():
    available_templates.clear()

    os.makedirs(shared.cmd_opts.template_dir, exist_ok=True)

    candidates = list(shared.walk_files(shared.cmd_opts.template_dir, allowed_extensions=[".template", ".tpl"]))
    for filename in sorted(candidates, key=str.lower):
        if os.path.isdir(filename):
            continue

        name = os.path.splitext(os.path.basename(filename))[0]

        entry = PromptTemplate(filename, name)

        available_templates[name] = entry
    print(f"Prompt template found ({len(available_templates.keys())}): {', '.join(available_templates.keys())}")

available_templates = {}

list_available_templates()