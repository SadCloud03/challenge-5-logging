import logging
import json
import requests

class HTTPLogHandler(logging.Handler):
    def __init__(self, url, service_id, token, timeout=0.3): # Añadimos token
        super().__init__()
        self.url = url
        self.service_id = service_id
        self.token = token # Guardamos el token
        self.timeout = timeout

    def emit(self, record):
        try:
            formatted_data = json.loads(self.format(record))
            payload = {
                "service_id": int(self.service_id),
                "level": formatted_data.get("level"),
                "message": formatted_data.get("message"),
                "extra": formatted_data.get("extra")
            }

            # AÑADIMOS EL HEADER DE AUTHORIZATION
            headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            }

            requests.post(
                self.url, 
                json=payload, 
                headers=headers, # <--- IMPORTANTE
                timeout=self.timeout
            )
        except Exception:
            pass