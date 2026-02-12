from pathlib import Path
import sys 
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT_DIR))
from funciones_email import (configuracion_inicial_logs_email, bucle_emails_service)
import logging
import threading

logger = logging.getLogger("email")
            
def main():
    configuracion_inicial_logs_email()

    hilo = threading.Thread(
        target=bucle_emails_service,
        args=(logger,),
        daemon=True
        )
    
    hilo.start()
    
    while True:
        info = input("dale a enter para cortar\n") # si funciona pero es increiblemente uncany
        if info:
            logger.info(info)
        else:
            break
    
    

if __name__ == "__main__":
    main()