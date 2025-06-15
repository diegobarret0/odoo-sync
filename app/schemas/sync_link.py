from pydantic import BaseModel

class SyncLinkCreate(BaseModel):
    origin: str
    origin_model: str
    origin_id: int
    destiny: str
    destiny_model: str
    destiny_id: int
