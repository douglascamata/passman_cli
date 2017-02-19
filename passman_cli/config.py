import os.path


def find_config(config):
    config_files = ["passman_cli.toml", "~/.config/passman_cli.toml"]
    if config:
        return config

    for config_file in config_files:
        if os.path.isfile(config_file):
            return config_file

    return None
