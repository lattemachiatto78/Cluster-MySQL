#!/usr/bin/env python3

import mysql.connector

# Configuración de conexión a la base de datos
db_config = {
    'user': 'root',                  # Cambia por tu usuario de MySQL
    'password': 'tu_contraseña',     # Cambia por tu contraseña de MySQL
    'host': '192.168.1.189',         # Dirección IP del servidor MySQL
    'port': 9000,                    # Puerto 9000
    'database': 'tu_base_de_datos'   # Cambia por el nombre de tu base de datos
}

def run_query(query):
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(**db_config)
        print("Conexión exitosa a la base de datos.")

        cursor = connection.cursor()
        cursor.execute(query)
        
        # Obtener resultados
        if query.strip().lower().startswith("select"):
            results = cursor.fetchall()
            print("Resultados de la consulta:")
            for row in results:
                print(row)
        else:
            connection.commit()  # Para consultas que modifican la base de datos
            print("Consulta ejecutada con éxito.")

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error al conectarse a la base de datos: {err}")

def main():
    print("Bienvenido al sistema de consultas de la base de datos.")
    while True:
        query = input("Introduce tu consulta SQL (o 'salir' para terminar): ")
        if query.lower() == 'salir':
            break
        run_query(query)

if __name__ == "__main__":
    main()
