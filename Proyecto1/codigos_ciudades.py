import difflib

# Diccionario de códigos de ciudad

ciudades = {
    "TLC": "Toluca",
    "MTY": "Monterrey",
    "MEX": "Ciudad de México",
    "TAM": "Tampico",
    "GDL": "Guadalajara",
    "CJS": "Ciudad Juárez",
    "CUN": "Cancún",
    "TIJ": "Tijuana",
    "HMO": "Hermosillo",
    "CME": "Ciudad del Carmen",
    "MID": "Mérida",
    "CTM": "Chetumal",
    "VER": "Veracruz",
    "OAX": "Oaxaca",
    "HUX": "Huatulco",
    "PVR": "Puerto Vallarta",
    "PXM": "Puerto Escondido",
    "ACA": "Acapulco",
    "ZIH": "Zihuatanejo",
    "AGU": "Aguascalientes",
    "VSA": "Villahermosa",
    "CZM": "Cozumel",
    "CUU": "Chihuahua",
    "TRC": "Torreón",
    "QRO": "Querétaro",
    "BJX": "León",
    "PBC": "Puebla",
    "SLP": "San Luis Potosí",
    "ZCL": "Zacatecas"
}

# Función para encontrar el código de la ciudad aunque se escriba de manera incorrecta
def encontrar_codigo_ciudad(nombre_ciudad):
    # Buscar coincidencia cercana en el nombre de la ciudad
    nombres_ciudades = list(ciudades.values())
    nombre_correcto = difflib.get_close_matches(nombre_ciudad, nombres_ciudades, n=1, cutoff=0.7)
    
    if nombre_correcto:
        for codigo, nombre in ciudades.items():
            if nombre == nombre_correcto[0]:
                return codigo
    else:
        return "Ciudad no encontrada"

