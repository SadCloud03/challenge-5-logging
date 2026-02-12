
from funciones import (
    configuracion_inicial_logs, 
    bucle_emails_service
)
import logging
import threading

logger = logging.getLogger()

            
def main():
    configuracion_inicial_logs()

    hilo = threading.Thread(
        target=bucle_emails_service,
        args=(logger,),
        daemon=True
        )
    
    hilo.start()
    
    while True:
        info = input("escribi algo") # si funciona pero es increiblemente uncany
        if info:
            logger.info(info)
        else:
            break
    
    

if __name__ == "__main__":
    main()