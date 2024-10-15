print("bayes no te baias")

class Nodo: 

    def __init__ (self, name, dic, values):
        self.name = name
        self.dic  = dic
        self.values = values
    

class Grafo:

    def __init__(self, matriz_ad, nodos):
        self.matriz_ad = []
        self.nodos = nodos

    def cargar_datos():
        print("esta func es de Juan diego o Javier")
    


def main():

   dic_rain = {
        ("none"): 0.7,
        ("light"): 0.2,
        ("heavy"): 0.1
    }
   rain_values = {'none', 'light', 'heavy'}
   print(dic_rain)
   rain = Nodo("rain", dic_rain, rain_values)
   print(rain.values)

   dic_maintenance = {
       ('none', 'yes'): 0.4,
       ('light', 'yes'): 0.2,
       ('heavy', 'yes'): 0.1,
       ('none', 'no'): 0.6,
       ('light', 'no'): 0.8,
       ('heavy', 'no'): 0.9
   }
   print(dic_maintenance)
   mainte_values = {'yes','no'}
   maintenance = Nodo("maintenance", dic_maintenance, mainte_values)

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
   
   print(dic_train)
   train_values = {'on time', 'delayed'}

   train = Nodo('train', dic_train, train_values)



    #maintanance = Nodo()
    #rain = Nodo()
    #rain = Nodo()


main()