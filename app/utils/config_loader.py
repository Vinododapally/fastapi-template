import os

from app.logger.logger import logger


def config_loader():
    env = os.getenv('APP_ENV', 'development')
    if env == 'prod':
        logger.info("Application is running in production mode")
        from app.config.prod_config import env as config
    elif env == 'preprod':
        logger.info("Application is running in pre-production mode")
        from app.config.ppd_config import env as config
    elif env == 'qa':
        logger.info("Application is running in QA mode")
        from app.config.qa_config import env as config
    else:
        logger.info("Application is running in development mode")
        from app.config.dev_config import env as config
    return config

# Load the configuration based on the environment variable
config= config_loader()

