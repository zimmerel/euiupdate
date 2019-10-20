import argparse
import logging
from typing import Dict

from euiupdate.config import CONFIG


class NullHandler(logging.Handler):
    def emit(self, record):
        ...


def get_logger(name: str = __name__) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.addHandler(NullHandler)
    return logger


def setup_args() -> argparse.Namespace[str, str]:
    # TODO Setup arg to take filepath and type directly from commandline
    parser = argparse.ArgumentParser(
        prog=CONFIG.app_name,
        description='Update ELVUI WoW Addon painlessly'
    )
    parser.add_argument(
        '-S', '--setup',
        type=str,
        help='Open prompts to add or change install location(s)'
    )
    return parser.parse_args()


def print_installs(installs: Dict[str, str]) -> None:
    logger = get_logger(__name__)

    def print_install(t: str, p: str):
        logger.info(f'{t} <---> {p}')

    if not installs:
        logger.info('No installations configured')
    else:
        logger.info('<-------> Configured Installs <------->')
        print_install('Type', 'Path')
        for type_, path in installs.items():
            print_install(type_, path)
