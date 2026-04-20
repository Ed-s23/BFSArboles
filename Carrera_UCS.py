

from arbol import Nodo

def buscar_solucion_USC(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    
    # CORRECCIÓN 1: Crear el nodo inicial
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_costo(0)
    nodos_frontera.append(nodo_inicial)

    #while len(nodos_frontera) != 0:
    while (not solucionado) and len(nodos_frontera):
        # CORRECCIÓN 2: Usar key en lugar de cmp
        nodos_frontera = sorted(nodos_frontera, key=lambda x:x.get_costo())  
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            return nodo
        
        dato_nodo = nodo.get_datos()
        for un_hijo, costo in conexiones[dato_nodo].items():
            hijo = Nodo(un_hijo)
            hijo.set_costo(nodo.get_costo() + costo)
            hijo.set_padre(nodo) 
            # CORRECCIÓN 4: Asignar padre

            if not hijo.en_lista(nodos_visitados):
                # CORRECCIÓN 3: Lógica de frontera limpia
                en_frontera = False
                for n in nodos_frontera:
                    if n.get_datos() == hijo.get_datos():
                        en_frontera = True
                        if hijo.get_costo() < n.get_costo():
                            nodos_frontera.remove(n)
                            nodos_frontera.append(hijo)
                        break
                
                if not en_frontera:
                    nodos_frontera.append(hijo)
    return None

#if __name__ == "__main__":
    # ... (tu diccionario de conexiones se mantiene igual)
 #   nodo_solucion = buscar_solucion_USC(conexiones, 'jiloyork', 'ags')

    
    # # CORRECCIÓN 5: Mostrar resultado correctamente
    # if nodo_solucion:
    #     resultado = []
    #     nodo = nodo_solucion
    #     while nodo is not None:
    #         resultado.append(f"{nodo.get_datos()}({nodo.get_costo()})")
    #         nodo = nodo.get_padre()
        
    #     resultado.reverse()
    #     print(" -> ".join(resultado))
    # else:
    #     print("No se encontró solución")

if __name__ == "__main__":
    conexiones = {
        'jiloyork':{'cdmx':125, 'qro': 513 },
        'morelos':{'qro':524 },
        'cdmx':{'jiloyork':125, 'qro':423, 'hgo':491},
        'hgo':{'cdmx': 491, 'qro':356, 'mexicali':309, 'mty': 345},
        'qro':{'slp':203, 'morelos':514,  'jiloyork':513, 'cdmx':423, 'mty':603,\
                'sonora':437, 'hgo':356, 'mexicali':313, 'ags':599},
        'slp':{'ags':390, 'qro':599 },
        'ags': {'slp':490, 'qro':203},
        'sonora': {'qro':437, 'mexicali':394,},
        'mexicali':{'mty':296, 'hgo':309, 'qro':313},
        'mty':{'mexicali':296, 'qro':603, 'hgo': 346}
    }
    estado_inicial = 'jiloyork'
    solucion = 'ags'
    nodo_solucion = buscar_solucion_USC(conexiones, estado_inicial, solucion)
    # CORRECCIÓN 5: Mostrar resultado correctamente
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
          
            resultado.append(f"{nodo.get_datos()}({nodo.get_costo()})")
           # resultado.append(estado_inicial)
            nodo = nodo.get_padre()

        resultado.reverse()
        print(" Camino  ",(resultado))
    else:
        print("No se encontró solución")
