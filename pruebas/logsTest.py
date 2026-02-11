import logging
import logging.config
import logging.handlers
import pathlib
import json

def setup_logging():
    config_file = pathlib.Path("logConfig/config.json")
    with open(config_file) as f_in:
        config = json.load(f_in)
        logging.config.dictConfig(config=config)

logger = logging.getLogger() # este nombre debe de ser el mismo que luego se define en loggers

# ------ esto es mas o menos todo lo que va en config.json -------
# logging_config = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "simple": {
#             "format": "%(levelname)s: %(message)s",
#         }
#     },
#     "handlers": {
#         "stderr": {
#             "class": "logging.StreamHandler",
#             "level" : "WARNING",
#             "formatter": "simple",
#             "stream": "ext://sys.stderr",
#         },
#         "file": {
#             "class": "logging.handlers.RotatingFileHandler",
#             "level": "DEBUG",
#             "formatter": "simple",
#             "filename": "logs/order_runner.log", # esto se crea en la raiz de donde se encuentra el archivo o programa
#             "maxBytes": 10000,
#             "backupCount": 3
#         }
#     },
#     "loggers" : {
#         "server": { # si getLogger("algo") se debe de definir ese logger explicitamente en dictConfig, o __name__ para usar root
#             "level": "DEBUG", 
#             "handlers": [
#                 "stderr",
#                 "file",
#             ]
#         }
#     },
# } # recordar de revisar la escritura de todo esto

def main(): 
    setup_logging()
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")

if __name__ == "__main__":
    main()
