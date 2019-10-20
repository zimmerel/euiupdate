from euiupdate.installs import request_install
from euiupdate.config import CONFIG
from euiupdate.helpers import get_logger, setup_args, print_installs


def main():
    logger = get_logger(__name__)
    logger.info('Initializing...')

    print_installs(CONFIG.installs)

    args = setup_args()
    to_setup = args.setup or not CONFIG.installs

    while to_setup:
        request_install()
        to_continue = input('Would you like to continue setting up installs (Y/n)?')
        to_setup = to_continue.lower() == 'Y'

#     TODO Compare versions Download if newer


if __name__ == '__main__':
    main()
