from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get('/')
def readRoot():
    return { "Hello": "World"}

@app.get('/hola')
def readRoot():
    return { "Hola": "Mundo"}

@app.get('/item/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return { 'item_id': item_id, 'q': q }

@app.get('/calculadora')
def calcular(operando1: float, operando2: float):
    return { 'suma': operando1 + operando2 }