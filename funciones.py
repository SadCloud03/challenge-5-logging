import sqlite3
from datetime import datetime, timezone

def revisar_log(datos):
    contenido_json = [
        "timestamp", 
        "service", 
        "severity",
        "message"
        ]

    for elemento in contenido_json:
        if elemento not in datos:
            return False, f"el campo {elemento} no se encuetra en los datos enviados"
    
    try:
        datetime.fromisoformat(datos["timestamp"].replace("Z", "+00:00"))
    except ValueError:
        return False, "[timestamp] : invalido"
    
    if datos["severity"] not in ["INFO","WARNING","ERROR"]:
        return False, "[severity] : invalido"
    
    return True, "[status] : OK"



def guardar_log(datos):
    conexion = sqlite3.connect("data_base_logs.db")
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO ServiceLogs(timestamp, service, severity, message, received_at)
    VALUES (?, ?, ?, ?, ?)""", (
        datos["timestamp"], 
        datos["service"], 
        datos["severity"], 
        datos["message"], 
        datetime.now(timezone.utc).isoformat()
    ))

    conexion.commit()
    return cursor.lastrowid