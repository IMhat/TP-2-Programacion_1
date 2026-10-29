import json
from funciones_base import obtener_posicion
from satelite import Satelite

def leer_registros(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        registros = json.load(archivo)
    return registros

def crear_catalogo(registros):
    satelites = []

    for registro in registros: 
        latitud,longitud,altitud = obtener_posicion(registro)

        nombre= registro ["OBJECT_NAME"]
        numero_catalogo = registro["NORAD_CAT_ID"]

        satelite = Satelite(nombre, numero_catalogo, latitud, longitud, altitud)
        satelites.append(satelite)

    return satelites


def resumir_por_orbita(satelites):

    altitudes_por_tipo = {}
    for satelite in satelites:
        tipo = satelite.tipo_orbita()
        if tipo not in altitudes_por_tipo:
            altitudes_por_tipo[tipo] = []
        altitudes_por_tipo[tipo].append(satelite.altitud)

    resumen = {}
    for tipo, altitudes in altitudes_por_tipo():
        cantidad = len(altitudes)
        resumen[tipo] = {
            "cantidad": cantidad,
            "minimo": min(altitudes),
            "maximo": max(altitudes),
            "promedio": sum(altitudes) / cantidad,
        }

    return resumen

def satelites_en_zona(satelites, longitud_min, longitud_max, latitud_min, latitud_max):
    en_la_zona = []

    for satelite in satelites:
        if satelite.esta_en_zona(longitud_min, latitud_min, longitud_max,  latitud_max):
            en_la_zona.append(satelite)

    return en_la_zona
