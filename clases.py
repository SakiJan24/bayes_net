import ast

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
            for combinacion in estado["combinaciones"]:
                est = [estado["estado"]]
                for heredado in combinacion["heredados"]:
                    est.append(heredado)
                linea = tuple(est), combinacion["probabilidad"]
                tabla[linea[0]] = linea[1]
        return tabla


            

class Grafo:
    def __init__(self, matriz_ad, nodos):
        self.matriz_ad = matriz_ad
        self.nodos = nodos
    
    def buscar_papas(self, name):
        print("entra")
        lista_indices = []
        for i in range(len(self.nodos)):
            if(self.nodos[i].nombre() == name):
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
        variables_principales = {}
        if(len(procesada) > len(self.nodos)):
            print("se van a procesar mas cosas de los nodos que se tienen")
        # busco a que pertence cada cosa
        for i in range(len(procesada)):
            for j in range(len(self.nodos)):
                for k in range (len(self.nodos[j].values)):
                    if(self.nodos[j].values[k] == procesada[i] ):
                        variables_principales[procesada[i]] = self.nodos[j].name
                
        return variables_principales
    
    def calcular_proba(self, principales, procesada):
        probabilidad = 1.0
        print("La procesada", procesada)
        # Itero por cada una de las palabras de procesada
        for i in range(len(procesada)):
            #En cada iteracion busca si tiene papas
            papas_raw = self.buscar_papas(principales[procesada[i]])
            papas = []
            # Los papas raw son solo los índices del arreglo de los papás
            #Entonces que obtener los nombres de esos papás para luego buscar
            for j in range(len(papas_raw)):
                papas.append(self.nodos[papas_raw[j]].name)

            print(papas)
            inverted_principales = {value: key for key, value in principales.items()}
            print("PRINCIPALES INVERTIDO: ", inverted_principales)
            if(len(papas) == 0):
                for j in range(len(self.nodos)):
                     #Si no tiene entonces solo busco el valor de la cadena
                    # en su tabla
                    if(self.nodos[j].name == principales[procesada[i]]):
                        print("TAMPOCOOOOOOOOOOOOOOOOOOOOOOOO")
                        print(self.nodos[j].tabla)
                        probabilidad = self.nodos[j].tabla[(procesada[i],)]*probabilidad
                        
                # Si tiene busco el valor de la cadena del papa en
                # principales y hago un append a los dados creo una
                # super tupla
            else:
                print("prin prin")
                string_tuple = "()"
                converted_tuple = ast.literal_eval(string_tuple)
                # consigo los strings the los papas
                # itero sobre esos strings para generar la tupla de strings
                elemento0 = procesada[i]
                #elemento0 = inverted_principales[papas[0]]
                tupla_updated = converted_tuple + (elemento0,)
                print("LO PAPURIKIS", papas)
                for j in range(0, len(papas)):
                    print("el del YES:", papas[j])
                    print(inverted_principales[papas[j]])
                    tupla_updated = tupla_updated + (inverted_principales[papas[j]],)
                print("Tuplat updated:",tupla_updated)


                #cuando ya tengo todos los string en la tupla, la convierto y accedo
                # Busco la probabilidad con la tupla y multiplico
                for j in range(len(self.nodos)):
                    #print("AAAAAAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    if(self.nodos[j].name == principales[procesada[i]]): 
                        print(self.nodos[j].tabla)
                        probabilidad = self.nodos[j].tabla[tupla_updated]*probabilidad
                
                print("LA SEÑORA PROBABILIDAD:", probabilidad )
                
                
                #falta capturar excepción de que los papas dan negatio
                        
                
                
               

                
                # con la supertupla busco en el nodo y saco la probabilidad
                # para multiplicar por probabilidads
        
        
        
        return probabilidad
        
    def principal(self, cadena):
        #Leer cadena
        procesada = self.limpiar_cadena(cadena)
        #Definir variables principales
        principales = self.variables_principales(procesada)
        #Calculo la probabilidad de cada una
        probabilidad = self.calcular_proba(principales, procesada)

        #busco los papas conforme a la variables principales
        print("esta es la funcion principal")
