"""
 Set of common utility functions that can be used by any module.
"""

import logging
from pathlib import Path

import pandas as pd
import yaml

def config_parse(config_file):
    """
    Parse config file

    Args:
        config_file [str]: path to config file
    """
    with open(config_file, "rb") as f:
        config = yaml.safe_load(f)
    return config

