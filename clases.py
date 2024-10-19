class Nodo: 
    def __init__(self, dic):
        self.dic = dic
        self.name = self.nombre()
        self.values = self.estados_propios()
        self.tabla = self.combinaciones()

    def nombre(self):
        return self.dic["nombre"]
    
    def estados_propios(self):
        est_propios = []
        for estado in self.dic["contenido"]["estados"]:
            est_propios.append(estado["estado"])
        return est_propios
    
    def estados_heredados(self):
        est_heredados = set()
        for estado in self.dic["contenido"]["estados"]:
            for combinacion in estado["combinaciones"]:
                for heredado in combinacion["heredados"]:
                    est_heredados.add(heredado)
        return list(est_heredados)
    
    def proba_combinacion(self, est:str, ests_heredado:list):
        for estado in self.dic["contenido"]["estados"]:
            if(est == estado["estado"]):
                for combinacion in estado["combinaciones"]:
                    if set(combinacion["heredados"]) == set(ests_heredado):
                        return combinacion["probabilidad"]
        return -1
    
    def combinaciones(self):
        tabla = {}
        for estado in self.dic["contenido"]["estados"]:
            est = [estado["estado"]]
            for combinacion in estado["combinaciones"]:
                for heredado in combinacion["heredados"]:
                    est.append(heredado)
                
                linea = tuple(est), combinacion["probabilidad"]
                tabla[linea[0]] = linea[1]
        return tabla


            

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