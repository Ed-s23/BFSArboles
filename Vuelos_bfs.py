
#!reslolucion del problema de los Vuelos usando BFS
from arbol import Nodo

def buscar_solucion_BFS (conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial= Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while(not solucionado) and len(nodos_frontera)!=0:
        nodo = nodos_frontera[0]
        # ? Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos()== solucion:
            #? Solucion encontrada
            solucionado= True
            return nodo
        else:
            #? Expandir los nodos hijo(ciudades con conexion)
            dato_nodo = nodo.get_datos()
            lista_hijos= []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                hijo.set_padre(nodo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados)and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

    return None
if __name__ == "__main__":
    conexiones= {
        'jiloyork':['Celaya','CDMX', 'Queretaro'],
        'Sonora':['Zacatecas','Sinaloa' ],
        'Guanajuato': ['AguasCalientes' ],
        'Oaxaca':['Queretaro'],
        'Sinaloa':['Celaya', 'Sonora','jiloyork'],
        'CDMX':['Queretaro', 'Sonora'],
        #'Queretaro':{'Monterrey'},
        'Celaya':['jiloyork', 'Sinaloa'],
        'Zacatecas':['Sonora', 'Monterrey', 'Queretaro'],
        'Monterrey':['Zacatecas','Sinaloa'],
        'Tamaulipas':['Queretaro'],
        'Queretaro':['Tamaulipas', 'Zacatecas', 'Sinaloa', 'jiloyork', 'Oaxaca']

    }
    estado_inicial = 'jiloyork'
    solucion= 'Zacatecas'
    nodo_solucion= buscar_solucion_BFS(conexiones, estado_inicial, solucion)
    #? Mostrar resultado
    resultado = []
    nodo= nodo_solucion
    while nodo.get_padre()!=None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)




