import json
from datetime import datetime, timedelta

try:
    with open('myfile.json', 'r') as json_file:
        ourjson = json.load(json_file)
except FileNotFoundError:
    print("El archivo 'myfile.json' no se encontró.")
    exit()

# Acceder a las claves correctas
try:
    access_token = ourjson['access_token']
    refresh_token = ourjson['refresh_token']
    expires_in = ourjson['expires_in']
    refreshtokenexpires_in = ourjson['refreshtokenexpires_in']
except KeyError:
    print("El archivo 'myfile.json' no tiene la estructura esperada.")
    exit()

# Imprimir los valores
print("Valor del access token:", access_token)
print("Valor del refresh token:", refresh_token)
print("Tiempo de expiración del access token (en segundos):", expires_in)
print("Tiempo de expiración del refresh token (en segundos):", refreshtokenexpires_in)

# Calcular la fecha de caducidad de los tokens
current_time = datetime.now()
access_token_expiry = current_time + timedelta(seconds=expires_in)
refresh_token_expiry = current_time + timedelta(seconds=refreshtokenexpires_in)

print("Fecha de expiración del access token:", access_token_expiry)
print("Fecha de expiración del refresh token:", refresh_token_expiry)

