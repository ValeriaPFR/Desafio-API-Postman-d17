#Desacargado a partir del descargable denominado python_request

"""import requests

url = "https://reqres.in/api/users"

payload = {}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
"""
# Las librerías que se usarán son las siguientes. Por convención se ubican al inicio del archivo
import requests
import json

# Fuente de datos de la API
url = "https://reqres.in/"
#Requerimientos a partir de la sección users de la API
url = "https://reqres.in/api/users"

#Filtros de información. Se agrega el criterio de búsqueda entre las llaves. 
# Se dejan  vacíos los filtros para no aplicar  ninguno y mostrar todos los registros
payload = {}
headers = {}

# Primer requerimiento, obtener información de los ususarios de la API
# Se utiliza la librería requests de Python para realizar una solicitud HTTP-GET a la URL especificada.
request = requests.request("GET", url, headers={}, data={})
#Los datos se cargan en formato JSON
info_users = json.loads(request.text)
#Imprimir los datos de usuarios
print(info_users)
print(request)

# Segundo requerimiento, crear un usuario que tenga de nombre 'Ignacio' y de trabajo 'Profesor'.
# Guarde el diccionario de respuesta en una variable llamada 'created_user' e imprimir.
#Usuario creado al final, posición 7

info_ignacio = {"6": {"id": 7, "first_name": "Ignacio", "work": "Profesor"}}
created_user = requests.post(url, json= info_ignacio)
print(created_user.text)
print(created_user)

# Tercer requerimiento. Actualice un usuario llamado 'morpheus' para que tenga un campo llamado residence
# igual a zion. Guarde el diccionario de respuesta en una variable llamada
# updated_user e imprímala en pantalla.
# Acceder a los elementos de users posición 1, actuaizar mediante el método PUT 
# en Postman se utiliza para actualizar recursos existentes en el servidor

url_put = "https://reqres.in/api/users/1"
info_morpheus = {"first_name": "morpheus", "residence": "zion"}
updated_user = requests.put(url_put, info_morpheus)
print(updated_user.text)
print(updated_user)

# Cuarto requerimiento. Eliminar un usuario llamado 'Tracey'. 
# Imprima el código de respuesta en pantalla.

Tracey = requests.delete("https://reqres.in/api/users/6")
print(Tracey)