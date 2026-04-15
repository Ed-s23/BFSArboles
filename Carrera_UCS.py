#! Viaje por carretera con búsqueda de costo uni 

from arbol import Nodo

def compara(x, y):
    return x.get_costo() - y.get_costo()

def buscar_solucion_USC(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodods_frontera = []
    nodo_inical.set_costo(0)
    nodods_frontera.append(nodo_inicial)

    while (not solucionado) and len(nodods_frontera):
        #Ordennar lista 
        nodods_frontera = sorted(nodods_frontera, cmp = compara)
        nodo = nodods_frontera[0]
        #!Extraer el nodo y añadirlo a visitados
        nodos_visitados.append(nodods_frontera.pop(0))
        if nodo.get_datos() == solucion:
            #Solucion encontrada
            solucionado = True
            return nodo
        else :
            #Expandir nodos hijos, ciudades con coneccion 
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                costo = conexiones[dato_nodo][un_hijo]
                hijo.set_costo(nodo.get_costo() + costo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    #Si esta en lista se sustituye con:
                    #EL nuevo valor del costo si es menor
