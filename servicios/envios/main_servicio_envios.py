from pathlib import Path
import sys 
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT_DIR))
from funciones_envios import (configuracion_inicial_logs_envios, bucle_envios_service)
import logging
import threading

logger = logging.getLogger("envios")

def main():
    configuracion_inicial_logs_envios()

    hilo = threading.Thread(
        target=bucle_envios_service,
        args=(logger,),
        daemon=True)

    hilo.start()

    while True:
        info = input("dale a enter para cortar\n")
        if info:
            logger.info("info")
        else:
            break 

if __name__ == "__main__":
    main()