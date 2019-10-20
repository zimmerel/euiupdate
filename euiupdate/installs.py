from euiupdate.config import CONFIG
from euiupdate.helpers import get_logger


def request_install_dir() -> str:
    """Asks user for install location"""
    return input('Please enter an install location for WoW.')


def request_install_type() -> str:
    logger = get_logger(__name__)
    install_type = input('What type of install is this - ([r]etail, [c]lassic)?').lower()
    if install_type in ('c', 'classic'):
        return 'classic'
    elif install_type in ('r', 'retail'):
        return 'retail'
    else:
        logger.info('Invalid selection')
        return request_install_type()


def request_install():
    """Combine dir and type into one function call"""
    install_location = request_install_dir()
    install_type = request_install_type()

    CONFIG.installs[install_type] = install_location
