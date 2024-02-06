from fastapi import APIRouter,  HTTPException
from pydantic import BaseModel
import logging

route = APIRouter()

"""
•	Se debe invertir el sentido de la frase o sea, si la frase fuera’ juan’ quedaría ‘nauj’ 
a demás debe pedir dos números (a, b) como claves para las posiciones par e impar de cada letra de la palabra 
y se suma a cada letra en el alfabeto (a, b) posiciones. Así, si la clave escogida fuese (a=3,b=4), 
la primera letra ‘n’ (posición impar) pasaría a ser la ‘p’, mientras que la segunda letra‘a’ (posición par) pasaría a ser la ‘c’. 
Para las últimas letras del abecedario se debe continuar  desde el principio del abecedario.
"""
class BodyFrases(BaseModel):
    frase: str
    a: int
    b: int


def encrypt(body):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    inverted = body.frase[::-1]
    a = body.a
    b = body.b
    encrypted = ''
    flag = 1
    for i in inverted:
        if flag % 2 != 0:
            actual_position = alphabet.index(i)
            new_position = actual_position + a
            encrypted = encrypted + alphabet[new_position]
        else:
            actual_position = alphabet.index(i)
            new_position = actual_position + b
            encrypted = encrypted + alphabet[new_position]
        flag += 1
    return encrypted

@route.post("/frases/encrypt")
async def calcular(body : BodyFrases):
    try:
        result = encrypt(body)
        response = {
            "encrypted": result,
        }
        return response
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail=str(e))

"""
• Crear un end point tipo POST para desencriptar las frases encriptadas aplicando el algoritmo 
inverso para realizar este proceso
"""

@route.post("/frases/decrypt")
async def calcular(parametro: int):
    try:
        print()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.post("/fibonacci")
async def calcular(parametro: int):
    try:
        print()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.post("/productos")
async def calcular(parametro: int):
    try:
        print()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@route.post("/cajeros")
async def calcular(parametro: int):
    try:
        print()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.post("/cajas-registradoras")
async def calcular(parametro: int):
    try:
        print()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.post("/ventas-almacen")
async def calcular(parametro: int):
    try:
        print()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
