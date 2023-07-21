import os
from modules.paths_internal import data_path


def preload(parser):
    parser.add_argument("--template-dir", type=str, help="Path to directory with Template files.", default=os.path.join(data_path, 'templates'))
