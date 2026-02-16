from pathlib import Path
import sys 
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT_DIR))
from funciones_no_service import (configuracion_inicial_no_token_service, bucle_no_token_service)
import logging
import threading

logger = logging.getLogger("envios")

def main():
    configuracion_inicial_no_token_service()

    hilo = threading.Thread(
        target=bucle_no_token_service,
        args=(logger,),
        daemon=True)

    hilo.start()

    while True:
        try:
            info = input("para conrtar ctrol+c, para introducir tu propio info escribe\n") # si funciona pero es increiblemente uncany
            if info:
                logger.info(info)
            else:
                break
        except KeyboardInterrupt:
            logger.info("no token service stopped by user")
            break

if __name__ == "__main__":
    main()