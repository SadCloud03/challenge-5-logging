from pydantic import BaseModel
from typing import Optional, Any, Dict, Union, List

#toco simular un JSONB (maldito PostgreSQL)
JSONB = Union[Dict[str, Any], List[Any], str, int, float, bool, None]

class LogIn(BaseModel):
    service_id: int   # <-- ¿Está llegando como int?
    level: str
    message: str
    extra: Optional[JSONB] = None # Usa Any temporalmente para debuguear