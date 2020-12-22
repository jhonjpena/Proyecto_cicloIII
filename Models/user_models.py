from pydantic import BaseModel

class ArticuloIn(BaseModel):
    id: int
    name: str

class ArticuloOut(BaseModel):
    id: int
    qty: int
