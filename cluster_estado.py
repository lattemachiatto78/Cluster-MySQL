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

def check_cluster_status():
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(**db_config)
        print("Conexión exitosa a la base de datos.")

        cursor = connection.cursor()

        # Consultar el estado del clúster
        cursor.execute("SHOW STATUS LIKE 'wsrep_cluster_size';")
        cluster_size = cursor.fetchone()
        if cluster_size:
            print(f"Tamaño del clúster: {cluster_size[1]}")
        else:
            print("No se pudo obtener el tamaño del clúster.")

        cursor.execute("SHOW STATUS LIKE 'wsrep_cluster_state';")
        cluster_state = cursor.fetchone()
        if cluster_state:
            print(f"Estado del clúster: {cluster_state[1]}")
        else:
            print("No se pudo obtener el estado del clúster.")

        # Consultar información de los nodos
        cursor.execute("SHOW STATUS LIKE 'wsrep_node_address';")
        node_address = cursor.fetchone()
        if node_address:
            print(f"Dirección del nodo actual: {node_address[1]}")
        else:
            print("No se pudo obtener la dirección del nodo actual.")

        cursor.execute("SHOW STATUS LIKE 'wsrep_connected';")
        connected = cursor.fetchone()
        if connected:
            print(f"Estado de conexión de nodos: {'Conectado' if connected[1] == 'ON' else 'Desconectado'}")
        else:
            print("No se pudo obtener el estado de conexión de nodos.")

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error al conectarse a la base de datos: {err}")

def main():
    check_cluster_status()

if __name__ == "__main__":
    main()