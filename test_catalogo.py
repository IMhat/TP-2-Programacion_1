import catalogo
from satelite import Satelite

# Dos registros reales de datos/satelites.json
CALSPHERE_1 = {
    "OBJECT_NAME": "CALSPHERE 1",
    "OBJECT_ID": "1964-063C",
    "EPOCH": "2026-10-14T14:21:25.466688",
    "MEAN_MOTION": 13.76730837,
    "ECCENTRICITY": 0.00243553,
    "INCLINATION": 90.2208,
    "RA_OF_ASC_NODE": 74.5342,
    "ARG_OF_PERICENTER": 291.4443,
    "MEAN_ANOMALY": 198.023,
    "EPHEMERIS_TYPE": 0,
    "CLASSIFICATION_TYPE": "U",
    "NORAD_CAT_ID": 900,
    "ELEMENT_SET_NO": 999,
    "REV_AT_EPOCH": 8785,
    "BSTAR": 0.00056429819,
    "MEAN_MOTION_DOT": 5.64e-06,
    "MEAN_MOTION_DDOT": 0,
}
 
CALSPHERE_2 = {
    "OBJECT_NAME": "CALSPHERE 2",
    "OBJECT_ID": "1964-063E",
    "EPOCH": "2026-10-14T11:27:54.596736",
    "MEAN_MOTION": 13.52908228,
    "ECCENTRICITY": 0.00169509,
    "INCLINATION": 90.2317,
    "RA_OF_ASC_NODE": 78.5946,
    "ARG_OF_PERICENTER": 237.821,
    "MEAN_ANOMALY": 195.4493,
    "EPHEMERIS_TYPE": 0,
    "CLASSIFICATION_TYPE": "U",
    "NORAD_CAT_ID": 902,
    "ELEMENT_SET_NO": 999,
    "REV_AT_EPOCH": 87239,
    "BSTAR": 5.6971978e-05,
    "MEAN_MOTION_DOT": 4.7e-07,
    "MEAN_MOTION_DDOT": 0,
}

def crear_satelites_de_prueba():
    return [
        Satelite("A", 1, -40, -70, 500), #leo
        Satelite("B", 2, -41, -71, 1500), #leo
        Satelite("C", 3, 0, 0, 20000), # meo
        Satelite("D", 4, 0, 10, 35786), # geo
        Satelite("E", 5, 10, 20, 40000) # heo
    ]

#test de lectura

def test_leer_registros():
    registros = catalogo.leer_registros("datos/satelites.json")

    assert len(registros) > 0
    assert isinstance(registros[0], dict)
    assert "OBJECT_NAME" in registros[0]


#test crear catalogo

def test_crear_catalogo():
    satelites = catalogo.crear_catalogo([CALSPHERE_1, CALSPHERE_2])

    assert len(satelites) == 2
    assert satelites[0].nombre == "CALSPHERE 1"
    assert satelites[0].numero_catalogo == 900
    assert satelites[1].nombre == "CALSPHERE 2"
    assert satelites[1].numero_catalogo == 902

def test_crear_catalogo_devuelve_objetos_satelite():
    satelites = catalogo.crear_catalogo([CALSPHERE_1])

    assert isinstance(satelites[0], Satelite)

def test_crear_catalogo_con_lista_vacia():
    assert catalogo.crear_catalogo([]) == []

#test resumir por orbita

def test_resumir_por_orbita_cantidades():
    resumen = catalogo.resumir_por_orbita(crear_satelites_de_prueba())

    assert resumen["LEO"]["cantidad"] == 2
    assert resumen["MEO"]["cantidad"] == 1
    assert resumen["GEO"]["cantidad"] == 1
    assert resumen["HEO"]["cantidad"] == 1

def test_resumir_por_orbita_minimo_max_promedio():
    resumen = catalogo.resumir_por_orbita(crear_satelites_de_prueba())

    assert resumen["LEO"]["minimo"] == 500
    assert resumen["LEO"]["maximo"] == 1500
    assert resumen["LEO"]["promedio"] == 1000

def test_resumir_por_orbita_lista_vacia():
    assert catalogo.resumir_por_orbita([]) == {}

#test satelites en zona

def test_satelites_en_zona():
    satelites = crear_satelites_de_prueba()

    en_la_zona = catalogo.satelites_en_zona(satelites, -76, -46, -66, -36)

    assert len(en_la_zona) == 2
    assert en_la_zona[0].nombre == "A"
    assert en_la_zona[1].nombre == "B"

def test_satelites_en_zona_incluye_el_borde():
    satelites = crear_satelites_de_prueba()
    # punto justo donde esta el satelite A
    en_la_zona = catalogo.satelites_en_zona(satelites, -70, -40, -70, -40)

    assert len(en_la_zona) == 1
    assert en_la_zona[0].nombre == "A"

    