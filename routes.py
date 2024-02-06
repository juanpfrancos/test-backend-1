from fastapi import APIRouter,  HTTPException
from pydantic import BaseModel
import logging

route = APIRouter()

"""
•	Crear un end point tipo post para un algoritmo que valide si un número X pertenece a la serie fibonacci
•	Crear un end point para registrar productos
•	Crear un end point para registrar cajeros
•	Crear un end point para registrar máquinas registradoras
•	Crear un end point para registrar las ventas de un almacén
•	Crear un end point para consultar el numero de ventas de cada producto con su respectivo código y nombre ordenado de mayor a menor (sql)
•	Crear un end point para consultar el cajero que ha vendido más productos. (sql)
•	Crera un end point para consultar el nombre de todos los productos vendidos con su respectivo código de cajero y máquina registradora.(sql)
"""

"""
•	Se debe invertir el sentido de la frase o sea, si la frase fuera’ juan’ quedaría ‘nauj’ 
a demás debe pedir dos números (a, b) como claves para las posiciones par e impar de cada letra de la palabra 
y se suma a cada letra en el alfabeto (a, b) posiciones. Así, si la clave escogida fuese (a=3,b=4), 
la primera letra ‘n’ (posición impar) pasaría a ser la ‘p’, mientras que la segunda letra‘a’ (posición par) pasaría a ser la ‘c’. 
Para las últimas letras del abecedario se debe continuar  desde el principio del abecedario.
"""
class BodyFrases(BaseModel):
    frase: str
    a: str = None
    b: float

@route.post("/frases/encrypt")
async def calcular(body : BodyFrases):
    try:
        return {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
• Crear un end point tipo POST para desencriptar las frases encriptadas aplicando el algoritmo 
inverso para realizar este proceso
"""

@route.post("/frases/decrypt")
async def calcular(parametro: int):
    try:
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.post("/fibonacci")
async def calcular(parametro: int):
    try:
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.post("/productos")
async def calcular(parametro: int):
    try:
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@route.post("/cajeros")
async def calcular(parametro: int):
    try:
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.post("/cajas-registradoras")
async def calcular(parametro: int):
    try:
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.post("/ventas-almacen")
async def calcular(parametro: int):
    try:
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
