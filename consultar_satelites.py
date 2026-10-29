import sys

from catalogo import (
    crear_catalogo,
    leer_registros,
    resumir_por_orbita,
    satelites_en_zona
)

ORDEN_ORBITAS = ["LEO", "MEO", "GEO", "HEO"]

def mostrar_resumen(satelites):
    resumen = resumir_por_orbita(satelites)

    for tipo in ORDEN_ORBITAS:
        if tipo not in resumen:
            continue

        datos = resumen[tipo]
        print(f"{tipo}: {datos['cantidad']} satelites "
              f"minimo {datos['minimo']} km "
              f"maximo {datos['maximo']} km "
              f"promedio {datos['promedio']} km")


def mostrar_zona(satelites, longitud_min, latitud_min, longitud_max, latitud_max):
    en_la_zona = satelites_en_zona( satelites, longitud_min, latitud_min, longitud_max, latitud_max)

    print(f"Satelites en la zona: {len(en_la_zona)}")
    for satelite in en_la_zona:
        print(satelite.descripcion())

def main():
    if len(sys.argv) < 3:
        return

    ruta = sys.argv[1]
    consulta = sys.argv[2]

    if consulta == "resumen":
        satelites = crear_catalogo(leer_registros(ruta))
        mostrar_resumen(satelites)

    elif consulta == "zona":
        if len(sys.argv) != 7:
            print("La consulta zona necesita 4 valores: "
                  "longitud minima, latitud minima, longitud maxima y latitud maxima.")
            return

        try:
            longitud_min = float(sys.argv[3])
            latitud_min = float(sys.argv[4])
            longitud_max = float(sys.argv[5])
            latitud_max = float(sys.argv[6])
        except ValueError:
            print("Los limties de la zona deben ser numeros.")
            return

        satelites = crear_catalogo(leer_registros(ruta))
        mostrar_zona(satelites, longitud_min, latitud_min,longitud_max,latitud_max)

    else:
        print(f"Consulta desconocida: {consulta}")

if __name__ == "__main__":
    main()
