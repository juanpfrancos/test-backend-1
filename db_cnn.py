import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        print("Conectando a la base de datos MySQL")
        connection = mysql.connector.connect(
            host='sql.freedb.tech', port=3306, user='freedb_jp_user', password='3Nfywuv8&27KKQM', database='freedb_yemi_db'
            #host='127.0.0.1', port=3306, user='root', password='', database='yemi_db'
        )
        print("Conexión exitosa a la base de datos MySQL")
        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
            return connection
    except Error as e:
        print(f"Error al conectarse a MySQL: {e}")
        return None
