print("bayes no te baias")

class Nodo: 
    def __init__(self, name, dic, values):
        self.name = name
        self.dic = dic
        self.values = values
    

class Grafo:
    def __init__(self, matriz_ad, nodos):
        self.matriz_ad = matriz_ad
        self.nodos = nodos

    def cargar_datos(self, name):  
        print("esta func es de Juan diego o Javier con el super json")
        
    def buscar_papas(self, name):
        print("entra")
        lista_indices = []
        for i in range(len(self.nodos)):
            if(self.nodos[i].name == name):
                for j in range(len(self.matriz_ad[i])):
                    if(self.matriz_ad[j][i] == 1):
                        lista_indices.append(j)
    
        return lista_indices
    
    def limpiar_cadena(self, cadena):
        print(cadena)
        #quitar el p( y el parentesis
        sub_cadena1 = 'P('
        sub_cadena2 = ')'
        sin_p_parentesis = cadena.replace(sub_cadena1, "")
        sin_p_parentesis_p = sin_p_parentesis.replace(sub_cadena2, "")
        el_split = sin_p_parentesis_p.split('^')

        return el_split
    def variables_principales(self, procesada):
        print("mahalo")
        if(len(procesada) > len(self.nodos)):
            print("se van a procesar mas cosas de los nodos que se tienen")
        # busco a que pertence cada cosa
        for i in range(len(procesada)):
            for j in range(len(self.nodos)):
                print("siu")
    
    def principal(self, cadena):
        #Leer cadena
        procesada = self.limpiar_cadena(cadena)
        #Definir variables principales

        #Calculo la probabilidad de cada una

        #busco los papas conforme a la variables principales
        print("esta es la funcion principal")


def main():
    dic_rain = {
        ("none"): 0.7,
        ("light"): 0.2,
        ("heavy"): 0.1
    }
    rain_values = {'none', 'light', 'heavy'}
   # print(dic_rain)
    rain = Nodo("rain", dic_rain, rain_values)
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
    maintenance = Nodo("maintenance", dic_maintenance, maintenance_values)

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
    train = Nodo('train', dic_train, train_values)

    dic_appointment = {
        ('on time', 'attend'): 0.9,
        ('delayed', 'attend'): 0.6,
        ('on time', 'miss'): 0.1,
        ('delayed', 'miss'): 0.4,
    }

    appointment_values = {'attend', 'miss'}
    appointment = Nodo('appointment', dic_appointment, appointment_values)

    #print(dic_appointment)

    matriz_ad = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    
    tablitas = []  
    tablitas.append(rain)
    tablitas.append(maintenance)
    tablitas.append(train)
    tablitas.append(appointment)
    print(tablitas[0].dic)
    
    graph = Grafo(matriz_ad, tablitas)
    lista_indices = graph.buscar_papas("train")
    print(lista_indices)
    

    print(graph.limpiar_cadena('P(light^delayed^miss)'))


main()

