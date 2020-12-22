from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
    articulo: str
    value: int

class TransactionOut(BaseModel):
    id_transaction: int
    articulo: str
    date: datetime
    value: int
    actual_balance: int
