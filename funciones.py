import json
import csv

def leer_tablas(nombre_archivo):
    with open(nombre_archivo, "r") as file:
        tablas = json.load(file)
        return tablas