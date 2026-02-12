from random import randint
from time import sleep
import logging.config
import logging
import pathlib
import json

def configuracion_inicial_logs_envios():
    config_path = pathlib.Path("config_envios.json")
    with open(config_path) as config_p:
        config = json.load(config_p)
    logging.config.dictConfig(config=config)

def bucle_envios_service(logger):
    while True:
        try:
            desicion = randint(0,3)
            if desicion == 1:
                logger.info("pedido enviado a DB con exito...")
            elif desicion == 2:
                logger.warning("DB query tomo mas tiempo de lo esperado...")
            else:
                logger.error("error de generacion de id de pedido...")
            sleep(2)
        except:
            logger.exception("error inesperado....")
            break
        