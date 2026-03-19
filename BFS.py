from arbol import Nodo

def buscar_solucion_BFS(estado_inicial, solucion_objetivo):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)
    while not solucionado and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion_objetivo:
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = [] 
            
            #! Para guardar los hijos generados

            # !OPERADOR izquierdo  
            hijo_izq_datos = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo_izq_datos)
            if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)
                lista_hijos.append(hijo_izquierdo)

            # !OPERADOR CENTRAL
            hijo_cen_datos = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo_cen_datos)
            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)
                lista_hijos.append(hijo_central)

            #! OPERADOR DERECHO 
            hijo_der_datos = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecho = Nodo(hijo_der_datos)
            if not hijo_derecho.en_lista(nodos_visitados) and not hijo_derecho.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecho)
                lista_hijos.append(hijo_derecho)

            nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    inicial = [4, 2, 3, 1]
    objetivo = [1, 2, 3, 4]
    nodo_solucion = buscar_solucion_BFS(inicial, objetivo)

    resultado = []
    nodo = nodo_solucion
    while nodo is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    
    resultado.reverse()
    print("Resultado")
    for paso in resultado:
        print(paso)