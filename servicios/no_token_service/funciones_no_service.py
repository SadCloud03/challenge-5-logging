from random import randint
from time import sleep
import logging.config
import logging
import pathlib
import json

def configuracion_inicial_no_token_service():
    config_path = pathlib.Path("config_no_service.json")
    with open(config_path) as config_p:
        config = json.load(config_p)
    logging.config.dictConfig(config=config)

def bucle_no_token_service(logger):
    while True:
        try:

            logger.info("this is an internal log of the service...")
            sleep(4)

        except Exception:
            logger.exception("unexpected error....")
            break
        