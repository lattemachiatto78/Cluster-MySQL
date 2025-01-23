#!/usr/bin/env python3

import requests
import mysql.connector

# Configuración de conexión a la base de datos
db_config = {
    'user': 'root',                  # Cambia por tu usuario de MySQL
    'password': 'tu_contraseña',     # Cambia por tu contraseña de MySQL
    'host': '192.168.1.189',         # Dirección IP del servidor MySQL
    'port': 9000,                    # Puerto 9000
    'database': 'tu_base_de_datos'   # Cambia por el nombre de tu base de datos
}

# Lista de servidores de WordPress
wordpress_servers = [
    'http://192.168.1.200',  # Cambia por la IP de tu primer servidor de WordPress
    'http://192.168.1.201',  # Cambia por la IP de tu segundo servidor de WordPress
    # Agrega más servidores si es necesario
]

def check_wordpress(server):
    try:
        response = requests.get(server)
        if response.status_code == 200:
            print(f"Servidor WordPress activo: {server}")
            return True
        else:
            print(f"Servidor WordPress no responde: {server}, Código de estado: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error al conectarse al servidor WordPress {server}: {e}")
        return False

def check_database():
    try:
        connection = mysql.connector.connect(**db_config)
        print("Conexión exitosa a la base de datos.")
        
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION();")
        db_version = cursor.fetchone()
        print("Versión de MySQL:", db_version)

        cursor.execute("SHOW DATABASES;")
        databases = cursor.fetchall()
        print("Bases de datos disponibles:")
        for db in databases:
            print(f"- {db[0]}")

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error al conectarse a la base de datos: {err}")

def main():
    print("Verificando servidores de WordPress...")
    for server in wordpress_servers:
        check_wordpress(server)

    print("\nVerificando conexión a la base de datos...")
    check_database()

if __name__ == "__main__":
    main()
