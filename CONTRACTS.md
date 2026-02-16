# 📝 Contrato de Interfaz - Sistema de Logging Distribuido

Este documento establece el estándar de comunicación entre los **Servicios Satélites** (Emisores) y el **Backend de Monitoreo** (Receptor).

---

## 1. Especificaciones del Endpoint

* **URL:** `http://<host>:<port>/logs`
* **Método:** `POST`
* **Content-Type:** `application/json`

## 2. Seguridad (Headers)

Todas las peticiones deben estar autenticadas. De lo contrario, el servidor responderá con un error **422** o **401**.

| Header | Valor | Ejemplo |
| :--- | :--- | :--- |
| `Authorization` | `Bearer <token>` | `Bearer mi_token_secreto_123` |
| `Content-Type` | `application/json` | `application/json` |

---

## 3. Cuerpo de la Petición (Payload)

El esquema de datos sigue la estructura definida en los modelos de Pydantic.

### Esquema JSON

| Campo | Tipo | Requerido | Descripción |
| :--- | :--- | :--- | :--- |
| `service_id` | `Integer` | **Sí** | ID del servicio registrado en la base de datos. |
| `level` | `String` | **Sí** | Nivel de severidad: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. |
| `message` | `String` | **Sí** | Descripción textual del evento. |
| `extra` | `JSONB` | No | Objeto dinámico (dict o list) para metadatos adicionales. |

### Ejemplo de Petición Válida

```json
{
  "service_id": 1,
  "level": "ERROR",
  "message": "Falla al procesar envío de correo",
  "extra": {
    "user_email": "usuario@ejemplo.com",
    "retry_count": 3,
    "error_code": "SMTP_TIMEOUT_504"
  }
}
```

### Notas de Implementación

* **Manejo de JSONB:** El campo extra se almacena como un tipo JSONB en PostgreSQL. Esto permite realizar consultas avanzadas sobre las llaves internas del objeto.

* **No Bloqueante:** Los servicios deben implementar el HTTPLogHandler con un timeout máximo de 0.5 segundos para asegurar que el sistema de logging no afecte el rendimiento del servicio principal.

* **Resiliencia:** Si el servidor de logs no está disponible, el servicio debe capturar la excepción silenciosamente para evitar el cierre inesperado del proceso simulado.