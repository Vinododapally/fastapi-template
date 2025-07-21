import logging


def configure_logging(level=logging.INFO):
    """
    Configures the logging settings for the application.

    Args:
        level (int): The logging level to set. Default is logging.INFO.
    """
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=level
    )

class Logger:

    @staticmethod
    def get_logger(name):
        """
        Returns a logger with the specified name.

        Args:
            name (str): The name of the logger.

        Returns:
            logging.Logger: A logger instance.
        """
        return logging.getLogger(name)


configure_logging(logging.INFO)

logger = Logger.get_logger(__name__)