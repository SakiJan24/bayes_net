import ast
from itertools import permutations
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
      
        variables_principales = {}
        if(len(procesada) > len(self.nodos)):
            print("se van a procesar mas cosas de los nodos que se tienen")
        # busco a que pertence cada cosaenco
        for i in range(len(procesada)):
            for j in range(len(self.nodos)):
                for k in range (len(self.nodos[j].values)):
                    if(self.nodos[j].values[k] == procesada[i] ):
                        variables_principales[procesada[i]] = self.nodos[j].name
                
        return variables_principales
    
    def get_names(self):
        names = []
        for i in range(len(self.nodos)):
            names.append(self.nodos[i].name)
        return names



    def encontrar_y(self, procesada):
        las_procesadas = []
        las_procesadas.append(procesada)
        print("Resultado procesamiento cadena:", procesada)
        variables_principales = {}
        if(len(procesada) > len(self.nodos)):
            print("se van a procesar mas cosas de los nodos que se tienen")
        # busco a que pertence cada cosa
        for i in range(len(procesada)):
            for j in range(len(self.nodos)):
                #voy a dejar esto duplicado para despues revisarlo
                # es decir {Appointment:Apointment} puede ocurrir
              #  print('NODOS', self.nodos[j].name, "PROCESADA", procesada[i])
                if(self.nodos[j].name == procesada[i]):
                      #print('ENTRAA', procesada[i])
                      variables_principales[procesada[i]] = procesada[i]

                else:
                    for k in range (len(self.nodos[j].values)):
                        if(self.nodos[j].values[k] == procesada[i] ):
                            variables_principales[procesada[i]] = self.nodos[j].name
        
        print("El diccionario de variables principales es:", variables_principales)
        names = self.get_names()
        print('Nombres previos con los que se encuentra', names)
        if(len(names) > len(procesada)):
            for i in range(len(names)):
                if names[i] in variables_principales.values():
                    names[i] = "tachado"
        print('Literalmente se tachan los nombres que ya tienen variable y queda: ', names)
        
        for i in range(len(names)):
            for j in range(len(self.nodos)):
                if self.nodos[j].name == names[i]:
                    for k in range(len(self.nodos[j].values)):
                        #falta poner el if acá
                        # me saco una copia de values y le hago el tachao
                        copia_procesada = procesada.copy()
                        copia_procesada.append(self.nodos[j].values[k])
                        las_procesadas.append(copia_procesada)
        del las_procesadas[0]
        
        return las_procesadas, variables_principales
    
    def encontrar_x(self, procesa_con_y, principales_especial):
       # print("vamos muchachos")
        # Primero, reviso los posibles valores de X
        index1 = -1
        print("Variables Principales Especial para los faltantes", principales_especial)
        for i in range(len(self.nodos)):
            if index1 == -1:
                if self.nodos[i].name == procesa_con_y[0]:
                    index1 = i
            else:
                break
        #print("EL INDEX:", index1)
        dos_probas = []
        # Con esa cantidad hago un ciclo que va a duplicar los arreglos que venga
        for i in range(len(self.nodos[index1].values)):
            el_y = procesa_con_y.copy()
            #print("PROCESA_EN_Y",procesa_con_y )
            #el_y[i][0] = self.nodos[index1].values[i]
            #print("EL_Y EN I 0:",el_y )
            dos_probas.append(el_y)
    
        #print(dos_probas)
        # Necesito obtener las multiples formas en que podría insertarse X
        posibles_combinaciones = list(permutations(self.nodos[index1].values))
        posibles_combinaciones = [list(p) for p in posibles_combinaciones]
        #clearprint(posibles_combinaciones)
        dos_probas_final = []


        for i in range(len(posibles_combinaciones)):
            new_inner_array = []
            for j in range(len(dos_probas[i])):
                new_inner = dos_probas[i][j].copy()  
                new_inner[0] = posibles_combinaciones[i][j]  
                new_inner_array.append(new_inner)
            dos_probas_final.append(new_inner_array)
        # Luego, itero para aniadir el valor que le corresponde conforme a los valores encontrados
        # en values
        # Con eso aniadido, lo retorno 
        #print('DOS PROBAS FINAL', dos_probas_final)

        
        dos_probas_return = [sublist for inner_list in dos_probas_final for sublist in inner_list]
        #print("DOS PROBAS FINNN", dos_probas_return)

        # Sort the flattened list
        dos_probas_sorted = sorted(dos_probas_return)
        #print("DOS PROBAS FINNN", dos_probas_sorted)

        
        copia_values = self.nodos[index1].values.copy()
        el_split = {value: [] for value in copia_values}

        
        for proba in dos_probas_sorted:
            if proba[0] in el_split:
                el_split[proba[0]].append(proba)

        # Convert the split dictionary values to a list if needed
        dos_probas_sorted_split = list(el_split.values())
        print("Arreglo de probabilidades para sumar", dos_probas_sorted_split)

        return dos_probas_sorted_split  # or whatever you need to return

        
        
    def calcular_proba(self, principales, procesada):
        probabilidad = 1.0
        print("La procesada para calcular probabilidad es", procesada)
        # Itero por cada una de las palabras de procesada
        for i in range(len(procesada)):
            #En cada iteracion busca si tiene papas
            papas_raw = self.buscar_papas(principales[procesada[i]])
            papas = []
            # Los papas raw son solo los índices del arreglo de los papás
            #Entonces que obtener los nombres de esos papás para luego buscar
            for j in range(len(papas_raw)):
                papas.append(self.nodos[papas_raw[j]].name)

            #print("Papas el nodo",papas)
            inverted_principales = {value: key for key, value in principales.items()}
            #print("Variables principales Invertido: ", inverted_principales)
            if(len(papas) == 0):
                for j in range(len(self.nodos)):
                     #Si no tiene entonces solo busco el valor de la cadena
                    # en su tabla
                    if(self.nodos[j].name == principales[procesada[i]]):
                        #print("TAMPOCOOOOOOOOOOOOOOOOOOOOOOOO")
                        #print(self.nodos[j].tabla)
                        probabilidad = self.nodos[j].tabla[(procesada[i],)]*probabilidad
                        
                # Si tiene busco el valor de la cadena del papa en
                # principales y hago un append a los dados creo una
                # super tupla
            else:
                #print("prin prin")
                string_tuple = "()"
                converted_tuple = ast.literal_eval(string_tuple)
                # consigo los strings the los papas
                # itero sobre esos strings para generar la tupla de strings
                elemento0 = procesada[i]
                #elemento0 = inverted_principales[papas[0]]
                tupla_updated = converted_tuple + (elemento0,)
                #print("LO PAPURIKIS", papas)
                for j in range(0, len(papas)):
                    #print("el del YES:", papas[j])
                    #print(inverted_principales[papas[j]])
                    tupla_updated = tupla_updated + (inverted_principales[papas[j]],)
                #print("Tupla para la búsqueda en tablacl:",tupla_updated)


                #cuando ya tengo todos los string en la tupla, la convierto y accedo
                # Busco la probabilidad con la tupla y multiplico
                for j in range(len(self.nodos)):
                    #print("AAAAAAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    if(self.nodos[j].name == principales[procesada[i]]): 
                #        print(self.nodos[j].tabla)
                        probabilidad = self.nodos[j].tabla[tupla_updated]*probabilidad
                
                #print("LA SEÑORA PROBABILIDAD:", probabilidad )
                
                #falta capturar excepción de que los papas dan negatio

                # con la supertupla busco en el nodo y saco la probabilidad
                # para multiplicar por probabilidads
        
        
        
        return probabilidad
        
    def principal(self, cadena):
        #Leer cadena
        procesada = self.limpiar_cadena(cadena)

        # Aqui bifurca
        print("La cadena tiene variables ocultas [Y/n]")
        ocultas = input("$")

        if ocultas.lower() == 'n':
            #Definir variables principales
            principales = self.variables_principales(procesada)
            #Calculo la probabilidad de cada una
            probabilidad = self.calcular_proba(principales, procesada)

        elif ocultas.lower() == "y": 
            procesada_con_y = [] # aqui debe ir la funcion que calcula las n cadenas
            # en una matriz de strings que tiene los valores de las faltantes
            procesada_con_y, principales_especial = self.encontrar_y(procesada)
            #print("procesada con Y",procesada_con_y, principales_especial)
            procesada_con_y_x = self.encontrar_x(procesada_con_y, principales_especial)
            # Ya con la procesada en Y lo que hago es partir esto en n arreglos para los dos casos
            probabilidades = {}
            for i in range(len(procesada_con_y_x)):
                probabilidad_i = 0.0
                for j in range(len(procesada_con_y_x[i])):
                    principales = self.variables_principales(procesada_con_y_x[i][j])
                    probabilidad_i = probabilidad_i + self.calcular_proba(principales,procesada_con_y_x[i][j])
                probabilidades[procesada_con_y_x[i][j][0]] = probabilidad_i
            
            print("Probabilidades",probabilidades)
            # Hago un ciclo que calcula las probabilidades dado un valor, en la que no es Y pero es faltante
            # Añado esa probabilidad en dónde hay un diccionario clon una tupla para el caso específico
            
            for i in range(len(procesada_con_y)):
                print("ejecuto principales")
                print("ejecuto probabilidad")
        
        else:
            print("Ingrese un valor valido")
        #busco los papas conforme a la variables principales
        print("esta es la funcion principal")
