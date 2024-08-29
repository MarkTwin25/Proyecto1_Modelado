import pytest
from codigos_ciudades import encontrar_codigo_ciudad

def test_encontrar_ciudades():
    assert encontrar_codigo_ciudad("Toluca") == "TLC"
    assert encontrar_codigo_ciudad("Monterrey") == "MTY"
    assert encontrar_codigo_ciudad("Ciudad de México") == "MEX"
    assert encontrar_codigo_ciudad("Tampico") == "TAM"
    assert encontrar_codigo_ciudad("Guadalajara") == "GDL"
    assert encontrar_codigo_ciudad("Ciudad Juárez") == "CJS"
    assert encontrar_codigo_ciudad("Cancún") == "CUN"
    assert encontrar_codigo_ciudad("Tijuana") == "TIJ"
    assert encontrar_codigo_ciudad("Hermosillo") == "HMO"
    assert encontrar_codigo_ciudad("Ciudad del Carmen") == "CME"
    assert encontrar_codigo_ciudad("Mérida") == "MID"
    assert encontrar_codigo_ciudad("Chetumal") == "CTM"
    assert encontrar_codigo_ciudad("Veracruz") == "VER"
    assert encontrar_codigo_ciudad("Oaxaca") == "OAX"
    assert encontrar_codigo_ciudad("Huatulco") == "HUX"
    assert encontrar_codigo_ciudad("Puerto Vallarta") == "PVR"
    assert encontrar_codigo_ciudad("Puerto Escondido") == "PXM"
    assert encontrar_codigo_ciudad("Acapulco") == "ACA"
    assert encontrar_codigo_ciudad("Zihuatanejo") == "ZIH"
    assert encontrar_codigo_ciudad("Aguascalientes") == "AGU"
    assert encontrar_codigo_ciudad("Villahermosa") == "VSA"
    assert encontrar_codigo_ciudad("Cozumel") == "CZM"
    assert encontrar_codigo_ciudad("Chihuahua") == "CUU"
    assert encontrar_codigo_ciudad("Torreón") == "TRC"
    assert encontrar_codigo_ciudad("Querétaro") == "QRO"
    assert encontrar_codigo_ciudad("León") == "BJX"
    assert encontrar_codigo_ciudad("Puebla") == "PBC"
    assert encontrar_codigo_ciudad("San Luis Potosí") == "SLP"
    assert encontrar_codigo_ciudad("Zacatecas") == "ZCL"

def test_ciudades_erroneas():
    assert encontrar_codigo_ciudad("Toluka") == "TLC"
    assert encontrar_codigo_ciudad("Monterreyy") == "MTY"
    assert encontrar_codigo_ciudad("Ciudad de Méxicoo") == "MEX"

def test_minusculas():
    assert encontrar_codigo_ciudad("toluca") == "TLC"
    assert encontrar_codigo_ciudad("monterrey") == "MTY"
    assert encontrar_codigo_ciudad("ciudad de méxico") == "MEX"


def test_min_mayus():
    assert encontrar_codigo_ciudad("ToLuca") == "TLC"
    assert encontrar_codigo_ciudad("MoNterey") == "MTY"
    assert encontrar_codigo_ciudad("veraCruzz") == "VER"
