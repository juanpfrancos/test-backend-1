from mysql.connector import Error
from db_cnn import connect_to_mysql

connection = connect_to_mysql()

def insert_query(query, data):
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print("Consulta ejecutada correctamente")
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")

def fetch_data(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error al obtener datos: {e}")
        return None
    finally:
        cursor.close()
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")
