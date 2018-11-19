import os

import pytoml as toml

with open(os.path.join(os.path.dirname(__file__), '../config.toml')) as fp_in:
    CONFIG = toml.load(fp_in)
