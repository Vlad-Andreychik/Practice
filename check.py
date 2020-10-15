import functions
import logging


# TODO[agorozhanko 14.10.2020]: код не компилируется
# TODO[vandreychyk 15.10.2020]: исправлено
def main():
    logging.basicConfig(filename='config.log',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger('functions.printMax')

    logger.info("Program started")
    functions.printMax(4, 6)
    logger.info("Done!")


if __name__ == '__main__':
    main()
