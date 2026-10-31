# TPI 2 - Satélites

Mateo Martin Mansilla

## Descripción

Programa de línea de comandos que lee un archivo JSON con los satélites activos
publicados por [CelesTrak](https://celestrak.org/), calcula la posición de cada
uno y permite consultarlos: resumir por tipo de órbita (LEO, MEO, GEO, HEO) y
listar los que están dentro de una zona geográfica.

## Instalación

```
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Consultas

Resumen por tipo de órbita (cantidad y altitud mínima, máxima y promedio):

```
python consultar_satelites.py datos/satelites.json resumen
```

Satélites dentro de una zona. Los argumentos son: longitud mínima, latitud
mínima, longitud máxima y latitud máxima (el borde cuenta como adentro):

```
python consultar_satelites.py datos/satelites.json zona -76.30 -46.13 -66.30 -36.13
```

Ese ejemplo es un cuadro centrado en Bariloche. Para armar otras zonas se puede
dibujar un rectángulo en [bboxfinder](https://bboxfinder.com/) y copiar el campo
"Box" reemplazando las comas por espacios.

```
