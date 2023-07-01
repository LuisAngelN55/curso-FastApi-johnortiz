from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4 as uuid
from typing import Optional


class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    precio_compra : float
    precio_venta : float
    proveedor : str


app = FastAPI()

productos = []

@app.get('/')
def index():
    return { "mensaje": "Bienvenido a la api de productos" }

@app.get('/productos')
def obtener_producto():
    return productos


@app.post('/productos')
def crear_producto(producto: Producto):
    producto.id = str(uuid())
    productos.append(producto)
    return { 'mensaje': 'Producto creado satisfactoriamente'}


@app.get('/productos/{producto_id}')
def obtener_producto_por_id(producto_id: str):
    # for p in productos:
    #     if p.id == producto_id:
    #         return p
    filter(lambda p: p.id == producto_id, )
    
    return {'mensaje': f'El producto con el ID {producto_id} no fue encontrado'}