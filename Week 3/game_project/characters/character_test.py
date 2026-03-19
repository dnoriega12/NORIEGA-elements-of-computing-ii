from pydantic import BaseModel

class Character(BaseModel):
    name: str
    level: int
    health: int
