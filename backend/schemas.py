from pydantic import BaseModel
from typing import Optional, Dict

class LogIn(BaseModel):
    level: str
    message: str
    extra: Optional[dict] = None