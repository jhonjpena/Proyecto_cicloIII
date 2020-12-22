from pydantic import BaseModel
from typing import Dict

class ArticuloInDB(BaseModel):
    id: int
    name: str


database_Articulos = Dict[str, ArticuloInDB]
database_Articulos = {"Item 1": ArticuloInDB(**{"id":1, "name":"Mesa"}),
                      "Item 2": ArticuloInDB(**{"id":2, "name":"Silla"}),
                      "Item 3": ArticuloInDB(**{"id":3, "name":"Sofa"}),
                      "Item 4": ArticuloInDB(**{"id":4, "name":"Escritorio"})
}

"""print(database_Articulos)"""

def get_Articulo(item: str):
    if item in database_Articulos.keys():
        return database_Articulos[item]
    else:
        return None

def update_Articulo(item_in_db: ArticuloInDB):
    database_Articulos[item_in_db.id] = item_in_db
    return item_in_db

