from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    precio_compra : float
    precio_venta : float
    proveedor : str


app = FastAPI()

@app.get('/')
def index():
    return { "mensaje": "Bienvenido a la api de productos" }