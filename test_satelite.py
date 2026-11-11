import pytest
from satelite import Satelite

def crear_satelite(latitud =-40.0, longitud=-70.0,altitud=419.7):
    return Satelite("ISS (ZARYA)", 25544, latitud,longitud,altitud)

#datos guardados

def test_guarda_los_datos():
    satelite = crear_satelite()

    assert satelite.nombre == "ISS (ZARYA)"
    assert satelite.numero_catalogo == 25544
    assert satelite.latitud == -40.0
    assert satelite.longitud == -70.0
    assert satelite.altitud == 419.7


#validaciones

def test_nombre_vacio_es_invalido():
    with pytest.raises(ValueError):
        Satelite("",1,0,0,500)

def test_nombre_solo_espacios_es_invalido():
    with pytest.raises(ValueError):
        Satelite("  ", 1, 0, 0, 500)

def test_numero_de_catalogo_decimal_es_invalido():
    with pytest.raises(ValueError):
        Satelite("A", 1.567, 0, 0, 500)

def test_numero_de_catalogo_texto_es_invalido():
    with pytest.raises(ValueError):
        Satelite("A", "25544", 0, 0, 500)

def test_latitud_fuera_de_rango_es_invalida():
    with pytest.raises(ValueError):
        crear_satelite(latitud=90.1)
    with pytest.raises(ValueError):
        crear_satelite(latitud=-90.1)
    
def test_latitud_en_los_limites_es_valida():
    assert crear_satelite(latitud=90).latitud == 90
    assert crear_satelite(latitud=-90).latitud == -90
 
 
def test_longitud_fuera_de_rango_es_invalida():
    with pytest.raises(ValueError):
        crear_satelite(longitud=180.1)
    with pytest.raises(ValueError):
        crear_satelite(longitud=-180.1)
 
 
def test_longitud_en_los_limites_es_valida():
    assert crear_satelite(longitud=180).longitud == 180
    assert crear_satelite(longitud=-180).longitud == -180
 
 
def test_altitud_menor_a_100_es_invalida():
    with pytest.raises(ValueError):
        crear_satelite(altitud=99.9)
 
 
def test_altitud_de_100_es_valida():
    assert crear_satelite(altitud=100).altitud == 100
