

class Satelite:

    def __init__(self, nombre, numero_catalogo, latitud,longitud, altitud):

        if not isinstance(nombre,str) or nombre.strip() =="":
            raise ValueError("El nombre no puede estar vacio")
        if not isinstance(numero_catalogo, int):
            raise ValueError("El numero de catalogo debe ser un numero entero")
        if not -90 <= latitud <= 90:
            raise ValueError("La latitud debe estar entre -90 y 90")
        if not -180 <= longitud <= 180:
            raise ValueError("la longitud debe estar entre -180 y 180")
        if altitud < 100:
            raise ValueError("La altitud debe ser de al menos 100km")
        
        self.nombre = nombre
        self.numero_catalogo= numero_catalogo
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

        def tipo_orbita(self):
            if self.altitud < 2000:
                return "LEO"
            if self.altitud < 34000:
                return "MEO"
            if self.altitud <= 37000:
                return "GEO"
            return "HEO"

        def descripcion(self):
            return (f"{self.nombre} - {self.numero_catalogo} - {self.tipo_orbita()} - {self.altitud} km")

        def esta_en_zona(self, longitud_min, latitud_min, longitud_max, latitud_max):
            #ingluimos los "bordes" al usar menor igual / mayor igual

            limite_latitud_min = self.latitud >= latitud_min
            limite_latitud_max = self.latitud <= latitud_max

            limite_longitud_min = self.longitud >= longitud_min
            limite_longitud_max = self.longitud <= longitud_max

            if(limite_longitud_min and limite_longitud_max
                                        and limite_latitud_min and limite_latitud_max):
                return True
            return False 