from DB.user_db import ArticuloInDB
from DB.user_db import update_Articulo, get_Articulo
from DB.transaction_db import TransactionInDB
from DB.transaction_db import save_transaction
from Models.user_models import ArticuloIn, ArticuloOut
from Models.transaction_models import TransactionIn, TransactionOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

""" Trae la cantidad de un articulo """ 

@api.get("/item/qty/{item}")
async def get_qty(item: str):
    item_in_db = get_Articulo(item)
    if item_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El artículo no existe en la base de datos")
    item_out = ArticuloOut(**item_in_db.dict())
    return item_out


""" Realiza la transacción de salida del inventario para un articulo """

@api.put("/item/transaction/")
async def make_transaction(transaction_in: TransactionIn):
    item_in_db = get_Articulo(transaction_in.articulo)
    if item_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El articulo no existe")
    if item_in_db.qty < transaction_in.value:
        raise HTTPException(status_code=400,
                            detail="No hay inventario disponible para el artículo")

    item_in_db.qty = item_in_db.qty - transaction_in.value
    update_Articulo(item_in_db)

    transaction_in_db = TransactionInDB(**transaction_in.dict(), 
                            actual_balance = item_in_db.qty)
    transaction_in_db = save_transaction(transaction_in_db)

    transaction_out = TransactionOut(**transaction_in_db.dict())
    return transaction_out