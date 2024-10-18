import json
import csv
import clases
import funciones as func
import pruebas as pr
                
    
def main():

    tablas = func.leer_tablas("tablas.json")

    nodos = []

    for tabla in tablas:
        nodos.append(clases.Nodo(tabla))
    for nodo in nodos:
        print(nodo.nombre())

    matriz_ad = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]

    graph = clases.Grafo(matriz_ad, nodos)
    lista_indices = graph.buscar_papas("train")
    print(lista_indices)


    dic_rain = {
        ("none"): 0.7,
        ("light"): 0.2,
        ("heavy"): 0.1
    }
    rain_values = {'none', 'light', 'heavy'}
   # print(dic_rain)
    #rain = clases.Nodo("rain", dic_rain, rain_values)
   # print(rain.values)

    dic_maintenance = {
        ('none', 'yes'): 0.4,
        ('light', 'yes'): 0.2,
        ('heavy', 'yes'): 0.1,
        ('none', 'no'): 0.6,
        ('light', 'no'): 0.8,
        ('heavy', 'no'): 0.9
    }
  #  print(dic_maintenance)
    maintenance_values = {'yes', 'no'}
    #maintenance = clases.Nodo("maintenance", dic_maintenance, maintenance_values)

    dic_train = {
        ('none', 'yes', 'on time'): 0.8,
        ('none', 'no', 'on time'): 0.9,
        ('light', 'yes', 'on time'): 0.6,
        ('light', 'no', 'on time'): 0.7,
        ('heavy', 'yes', 'on time'): 0.4,
        ('heavy', 'no', 'on time'): 0.5,
        ('none', 'yes', 'delayed'): 0.2,
        ('none', 'no', 'delayed'): 0.1,
        ('light', 'yes', 'delayed'): 0.4,
        ('light', 'no', 'delayed'): 0.3,
        ('heavy', 'yes', 'delayed'): 0.6,
        ('heavy', 'no', 'delayed'): 0.5,
    }
    
   # print(dic_train)
    train_values = {'on time', 'delayed'}
    #train = clases.Nodo('train', dic_train, train_values)

    dic_appointment = {
        ('on time', 'attend'): 0.9,
        ('delayed', 'attend'): 0.6,
        ('on time', 'miss'): 0.1,
        ('delayed', 'miss'): 0.4,
    }

    appointment_values = {'attend', 'miss'}
    #appointment = clases.Nodo('appointment', dic_appointment, appointment_values)

    #print(dic_appointment)

    
    #tablitas = []  
    #tablitas.append(rain)
    #tablitas.append(maintenance)
    #tablitas.append(train)
    #tablitas.append(appointment)
    #print(tablitas[0].dic)
    
    #graph = clases.Grafo(matriz_ad, tablitas)
    #lista_indices = graph.buscar_papas("train")
    #print(lista_indices)
    


main()

