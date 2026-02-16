
# formato nomal en el que los logs son enviados
```
    {
        "timestamp" : datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
        "level" : record.levelname,
        "logger" : record.name,
        "message" : record.getMessage(),
        "module" : record.module,
        "function" : record.funcName,
        "line" : record.lineno,
        "thread" : record.threadName
    }
```