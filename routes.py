from fastapi import APIRouter,  HTTPException
from pydantic import BaseModel
from algorithms import encrypt, decrypt, fibonacci
from db_queries import insert_query, get_data
import logging

route = APIRouter()
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


"""
•	Se debe invertir el sentido de la frase o sea, si la frase fuera’ juan’ quedaría ‘nauj’ 
a demás debe pedir dos números (a, b) como claves para las posiciones par e impar de cada letra de la palabra 
y se suma a cada letra en el alfabeto (a, b) posiciones. Así, si la clave escogida fuese (a=3,b=4), 
la primera letra ‘n’ (posición impar) pasaría a ser la ‘p’, mientras que la segunda letra‘a’ (posición par) pasaría a ser la ‘c’. 
Para las últimas letras del abecedario se debe continuar  desde el principio del abecedario.
"""

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


#• Crear un end point para consultar el numero de ventas de cada producto con su respectivo código y nombre ordenado de mayor a menor (sql)
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
        
#•	Crear un end point para consultar el cajero que ha vendido más productos. (sql)
@route.get("/cajero-que-vendio-mas")
async def reg_venta():
    try:
        query ="""
                    SELECT NomApels AS Cajero, 
                        (SELECT COUNT(*) 
                            FROM venta v 
                            WHERE v.cajero = c.codigo) AS Total_Ventas
                    FROM cajeros c
                    ORDER BY Total_Ventas DESC
                    LIMIT 1;
                """
        data = get_data(query)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    

#• Crear un end point para consultar el nombre de todos los productos vendidos con su respectivo código de cajero y máquina registradora.
@route.get("/todos-productos-vendidos")
async def reg_venta():
    try:
        query ="""
                    SELECT p.codigo AS Codigo_Producto, 
                        p.nombre AS Nombre_Producto, 
                        v.cajero AS Codigo_Cajero, 
                        v.maquina AS Codigo_Maquina
                    FROM venta v
                    JOIN productos p ON v.producto = p.codigo
                    JOIN cajeros c ON v.cajero = c.codigo
                    JOIN maquinas_registradoras m ON v.maquina = m.codigo;
                """
        data = get_data(query)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))   


#•	Crear un end point para consultar el valor total de las ventas realizadas en cada piso.(sql)
@route.get("/valor-total-ventas-piso")
async def reg_venta():
    try:
        query ="""
                    SELECT 
                        m.piso AS Piso,
                        (SELECT SUM(p.precio) 
                        FROM venta v
                        JOIN productos p ON v.producto = p.codigo
                        WHERE v.maquina = m.codigo) AS Valor_Total_Ventas
                    FROM maquinas_registradoras m;
                """
        data = get_data(query)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))