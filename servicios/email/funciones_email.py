from random import randint
import logging
import logging.config
import pathlib
import json
from time import sleep

def configuracion_inicial_logs_email():
    config_path = pathlib.Path("config_email.json")
    with open(config_path) as config_p:
        config = json.load(config_p)
    logging.config.dictConfig(config=config)


def bucle_emails_service(logger):
    while True:
        try:
            desicion = randint(0,3)
            if desicion == 1:
                logger.info("successfull email send..")
            elif desicion == 2:
                logger.warning("email send with delay...")
            else:
                logger.error("unexpected error on sending email....")
            sleep(2)
        except:
            logger.exception("unexpected error....")
            break
        