import pandas as pd
import numpy as np
import requests
# Importar diccionario de ciudades del archivo Codigos.py
from codigos_ciudades import ciudades, encontrar_codigo_ciudad


Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
KEY_OPENWEATHER = 'cbf49df61a4df6c077edcf1844d67f5f'

# Leer el dataset limpio
df = pd.read_csv('dataset1_clean.csv')

cache = {} # "ciudad": "clima"

def revisar_cache(ciudad):
    if ciudad in cache:
        #print(f"Usando caché para {ciudad}")
        return cache[ciudad]
    return None

def dar_clima_ciudades(ciudad1: str, ciudad2: str):
    ciudad1 = encontrar_codigo_ciudad(ciudad1)
    ciudad2 = encontrar_codigo_ciudad(ciudad2)

    resultado1 = ""
    resultado2 = ""

    if ciudad1 == "Ciudad no encontrada" or ciudad2 == "Ciudad no encontrada":
        #print("Ciudad no encontrada")
        return "Ciudad no encontrada"
    else:
        clima1 = revisar_cache(ciudad1)
        clima2 = revisar_cache(ciudad2)
        
        if clima1 is None:
            params1 = {
                "lat": df.loc[df["origin"] == ciudad1]["origin_latitude"].values[0],
                "lon": df.loc[df["origin"] == ciudad1]["origin_longitude"].values[0],
                "appid": KEY_OPENWEATHER
            }
            response1 = requests.get(Endpoint, params=params1)
            clima1 = response1.json()
            cache[ciudad1] = clima1["weather"][0]["description"]
            #print(f'El clima de: {ciudad1}: {clima1["weather"][0]["description"]}')
            resultado1 = f'El clima de: {ciudad1}: {clima1["weather"][0]["description"]}'

        else:
            #print(f"El clima de {ciudad1} es {clima1} cache1")
            resultado1 = f"Cache: El clima de {ciudad1} es {clima1}"

        if clima2 is None:
            params2 = {
                "lat": df.loc[df["origin"] == ciudad2]["origin_latitude"].values[0],
                "lon": df.loc[df["origin"] == ciudad2]["origin_longitude"].values[0],
                "appid": KEY_OPENWEATHER
            }
            response2 = requests.get(Endpoint, params=params2)
            clima2 = response2.json()
            cache[ciudad2] = clima2["weather"][0]["description"]   

            #print(f'El clima de: {ciudad2}: {clima2["weather"][0]["description"]}')
            resultado2 = f'El clima de: {ciudad2}: {clima2["weather"][0]["description"]}'
        else:
            #print(f"El clima de {ciudad2} es {clima2} cache2")
            resultado2 = f"Cache: El clima de {ciudad2} es {clima2}"
        
        return resultado1, resultado2