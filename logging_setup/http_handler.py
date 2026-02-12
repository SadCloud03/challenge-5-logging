import logging
import requests

class HTTPLogHandler(logging.Handler):
    def __init__(self, url, timeout=0.3):
        super().__init__()
        self.url = url
        self.timeout = timeout

    def emit(self, record):
        try:
            payload = self.format(record=record)
            requests.post(
                self.url,
                data=payload,
                headers={"Content-Type" : "application/json"},
                timeout=self.timeout
            )
        except Exception:
            pass #esto no rompe la app 