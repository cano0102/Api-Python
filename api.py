import requests
import json

url = "https://api-colombia.com/api/v1/Department"

try:
    respuesta = requests.get(url, timeout=10)

    if respuesta.status_code == 200:
        
        datos = respuesta.json()

        for atraccion in datos:
            atraccion_dato = {
                "id": atraccion_dato.get("id","Id no encontrado"),
                "Poblacion": atraccion_dato.get("population","Poblacion no encontrada"),
                "Nombre": atraccion.get("name", "Nombre no disponible"), 
            }
        print(f"Nombre: {atraccion_dato['Nombre']}, Descripción: {atraccion_dato['Descripcion']}")

    else:
        print(f"Error en la solicitud: Código {respuesta.status_code}")

except requests.exceptions.RequestException as error:
    print(f"Error de conexión: {error}")
