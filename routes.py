from fastapi import APIRouter,  HTTPException
from pydantic import BaseModel
from algorithms import encrypt, decrypt, fibonacci
from db_queries import insert_query, get_data
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

class Productos(BaseModel):
    nombre: str
    precio: int

class Cajeros(BaseModel):
    nombre: str

class Maquina(BaseModel):
    piso: int

class Ventas(BaseModel):
    producto_id: int
    cajero_id: int
    maquina_id: int

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
async def calcular(number: int):
    try:
        result = fibonacci(number)
        return { "fibonacci": result, }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.post("/productos")
async def reg_product(producto: Productos):
    try:
        query = "INSERT INTO productos (codigo, nombre, precio) VALUES (%s, %s, %s)"
        data = (None, producto.nombre, producto.precio)
        insert_query(query, data)
        return {"message": "Success!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@route.post("/cajeros")
async def reg_cajero(cajero: Cajeros):
    try:
        query = "INSERT INTO cajeros (codigo, NomApels) VALUES (%s, %s)"
        data = (None, cajero.nombre)
        insert_query(query, data)
        return {"message": "Success!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.post("/cajas-registradoras")
async def reg_caja(maq: Maquina):
    try:
        query = "INSERT INTO maquinas_registradoras (codigo, piso) VALUES (%s, %s)"
        data = (None, maq.piso)
        insert_query(query, data)
        return {"message": "Success!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.post("/ventas-almacen")
async def reg_venta(venta: Ventas):
    try:
        query = "INSERT INTO venta (producto, cajero, maquina) VALUES (%s, %s, %s)"
        data = (venta.producto_id, venta.cajero_id, venta.maquina_id)
        insert_query(query, data)
        return {"message": "Success!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#•	Crear un end point para consultar el numero de ventas de cada producto con su respectivo código y nombre ordenado de mayor a menor (sql)
@route.get("/ventas-productos")
async def reg_venta():
    try:
         
        query ="""
                SELECT 
                    productos.codigo, 
                    productos.nombre, 
                    (SELECT COUNT(*) FROM venta WHERE venta.producto = productos.codigo) AS total_ventas
                FROM 
                    productos
                ORDER BY 
                    total_ventas DESC;
                """
        data = get_data(query)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
"""
•	Crear un end point para consultar el numero de ventas de cada producto con su respectivo código y nombre ordenado de mayor a menor (sql)
•	Crear un end point para consultar el cajero que ha vendido más productos. (sql)
•	Crera un end point para consultar el nombre de todos los productos vendidos con su respectivo código de cajero y máquina registradora.(sql)
•	Crear un end point para consultar el valor total de las ventas realizadas en cada piso.(sql)
"""