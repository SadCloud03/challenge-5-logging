
from funciones import (
    configuracion_inicial_logs, 
    bucle_emails_service
)
from pseudoDB import lista_gmails
import requests
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
        seguir = input("escribi algo") # si funciona pero es increiblemente uncany
        if seguir:
            logger.info("sigue el proceso")
        else:
            break
    
    

if __name__ == "__main__":
    main()