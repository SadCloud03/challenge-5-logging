import json 
import logging
from datetime import datetime, timezone

class JsonFormater(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp" : datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            "level" : record.levelname,
            "logger" : record.name,
            "message" : record.getMessage(),
            "module" : record.module,
            "function" : record.funcName,
            "line" : record.lineno,
            "thread" : record.threadName
        }

        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
        
        return json.dumps(log_record, ensure_ascii=False)