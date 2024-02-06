from fastapi import APIRouter,  HTTPException
from pydantic import BaseModel
from algorithms import encrypt, decrypt
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

@route.post("/frases/encrypt")
async def encrypt_end(body : BodyFrases):
    try:
        result = encrypt(body)
        return { "encrypted": result, }
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail=str(e))

"""
• Crear un end point tipo POST para desencriptar las frases encriptadas aplicando el algoritmo 
inverso para realizar este proceso
"""
  
@route.post("/frases/decrypt")
async def decrypt_end(body : BodyFrases):
    try:
        result = decrypt(body)
        return { "decrypted": result, }
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
