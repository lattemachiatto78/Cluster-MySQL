#!/usr/bin/env python3
# Este es un script en Python para conectarse a un clúster de MySQL a través de un balanceador,
# realizar consultas a la base de datos y mostrar información del clúster.

import mysql.connector
from mysql.connector import Error

# Configuración del clúster
db_config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': 'direccion_del_balanceador',  # Cambia esto por la dirección de tu balanceador
    'database': 'nombre_de_tu_base_de_datos'
}

def connect_to_database(config):
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Conectado a MySQL Server version", db_info)
            return connection
    except Error as e:
        print("Error al conectarse a la base de datos:", e)
        return None

def query_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        print("Estás conectado a la base de datos:", db_name[0])
        
        # Realiza aquí tus consultas SQL
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tablas en la base de datos:")
        for table in tables:
            print(table[0])
            
        # Aquí puedes agregar más consultas para obtener información del clúster
    except Error as e:
        print("Error al realizar la consulta:", e)
    finally:
        cursor.close()

def main():
    connection = connect_to_database(db_config)
    if connection:
        query_database(connection)
        connection.close()

if __name__ == "__main__":
    main()
