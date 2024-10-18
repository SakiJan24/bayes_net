import json
import funciones

def imprimir_tablas(tablas):
    for tabla in tablas:
        print(tabla["nombre"])
        for estado in tabla["contenido"]["estados"]:
            print(" ", end="")
            print(estado["estado"])
            for combinacion in estado["combinaciones"]:
                print("  ", end="")
                for heredado in combinacion["heredados"]:
                    print(heredado, end=", ")
                print("  ", end="")
                print(combinacion["probabilidad"])

if __name__ == "__main__" :
   matriz = funciones.leer_matriz_ad("matriz.csv")
   for linea in matriz:
       print (linea)