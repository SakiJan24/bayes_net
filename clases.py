class Nodo: 
    def __init__(self, dic):
        self.dic = dic

    def nombre(self):
        return self.dic["nombre"]

    
    

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
            if(self.nodos[i].nombre() == name):
                for j in range(len(self.matriz_ad[i])):
                    if(self.matriz_ad[j][i] == 1):
                        lista_indices.append(j)
    
        return lista_indices