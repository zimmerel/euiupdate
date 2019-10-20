import os
from pathlib import Path
from appdirs import user_config_dir
from configparser import ConfigParser
from typing import Dict


class Config:
    app_name = 'elvui_update'
    app_author = 'zimmerel'

    config_dir = Path(user_config_dir(app_name, app_author))
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    config_filepath = config_dir / 'config.ini'
    if not config_filepath.exists():
        with open(str(config_filepath), 'w+') as file:
            file.write('[Installs]')

    file_config = ConfigParser()
    file_config.read(str(config_filepath))
    installs_section_name = 'Installs'
    install = file_config.get(installs_section_name, {}, fallback={})

    install_relative_location = Path('/Interface/AddOns/')
    elvui_dir = install_relative_location / 'ElvUI'
    options_dir = install_relative_location / 'ElvUI_OptionsUI'

    install_type_directories = {
        'retail': '_retail',
        'classic': '_classic'
    }
    supported_install_types = install_type_directories.keys()


class ProdConfig(Config):
    ...


class DevConfig(Config):
    ...


class TestConfig(Config):
    ...


def set_config(env=os.getenv('PYENV', 'dev')):
    environments = {
        'prod': ProdConfig,
        'dev': DevConfig,
        'test': TestConfig
    }
    return environments.get(env)


CONFIG = set_config()
