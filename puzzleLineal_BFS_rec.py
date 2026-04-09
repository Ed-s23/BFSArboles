
 #! Puzzle lineal con búsqueda en profundidad recursiva 
from arbol import Nodo

def buscar_solucion_DFS_rec(nodo_inicial, solucion, visitados):
   
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial
    else: 
      #! Expandir nodos sucesores(hijos)
        dato_nodo = nodo_inicial.get_datos()
    
        hijo_izq = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
        hijo_der = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
        hijo_cent = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
        hijo_izquierdo = Nodo(hijo_izq)
        hijo_izquierdo.set_padre(nodo_inicial)
         
        hijo_derecho = Nodo(hijo_der)
        hijo_derecho.set_padre(nodo_inicial)
        
        hijo_central = Nodo(hijo_cent)
        hijo_central.set_padre(nodo_inicial)
        
        nodo_inicial.set_hijos([hijo_izquierdo, hijo_derecho, hijo_central])

        for nodo_hijo in nodo_inicial.get_hijos():
            if nodo_hijo.get_datos() not in visitados:
                #! Llamada Rcursiva
                sol = buscar_solucion_DFS_rec(nodo_hijo, solucion, visitados)
                if sol is not None:
                    return sol
        
        return None

if __name__ == "__main__":
    estado_inicial = [4, 3, 2, 1]
    solucion = [1, 2, 3, 4]
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    
    nodo_objetivo = buscar_solucion_DFS_rec(nodo_inicial, solucion, visitados)
    #!Mostrar resultado
    if nodo_objetivo:
        resultado = []
        nodo_actual = nodo_objetivo
        while nodo_actual is not None:
            resultado.append(nodo_actual.get_datos())
            nodo_actual = nodo_actual.get_padre()
        
        resultado.reverse()
        for paso in resultado:
            print(paso)
