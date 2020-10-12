import logging
import logging.config

import functions


def main():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('exampleApp.functions.func_key')

    logger.info("Program started")
    functions.func_key(8)
    logger.info("Done!")


if __name__ == '__main__':
    main()
