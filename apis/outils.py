"""
This python module stores useful functions for working with rest apis
"""
import os
import yaml


CURRENT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(CURRENT)

# Function to load yaml configuration file
def load_config(config_name):
    """
    Sets the configuration file path
    Args:
    config_name: Name of the configuration file in the directory
    Returns:
    Configuration file
    """
    with open(os.path.join(ROOT, config_name), encoding="utf-8") as conf:
        config = yaml.safe_load(conf)
    return config
