
# #! Vuelos com busqueda con profundidad iterativa
# from arbol import Nodo 

# def DFS_prof_iter(nodo, solucion):
#     for limite in range(0,100):
#         visitados=[]
#         sol = buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite)
#         if sol != None: 
#             return sol
# def buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite):
#         if limite >0 : #* 
#             visitados.append(nodo)
#         if nodo.get_datos()== solucion:
#             return nodo
#         else: #! Expandir nodos hijo (Ciudades con conección)
#             dato_nodo= nodo.get_datos()
#             lista_hijos=[]
#             for un_hijo in conexiones[dato_nodo]:
#                 hijo = Nodo(un_hijo)
#                 if not hijo.en_lista(visitados):
#                     lista_hijos.append(hijo)

#             nodo.set_hijos(lista_hijos)

#             for nodo_hijo in nodo.get_hijos():
#                 if nodo_hijo.get_datos() in visitados:
#                     #!Llamada recursiva 
#                     sol = buscar_solucion_DFS_Rec(nodo_hijo, solucion, visitados, limite-1)
#                     if sol != None:
#                         return sol
                    
#         return None

# if __name__ == "__main__":
#     conexiones= {
#         'jiloyork':['Celaya','CDMX', 'Queretaro'],
#         'Sonora':['Zacatecas','Sinaloa' ],
#         'Guanajuato': ['AguasCalientes' ],
#         'Oaxaca':['Queretaro'],
#         'Sinaloa':['Celaya', 'Sonora','jiloyork'],
#         'CDMX':['Queretaro', 'Sonora'],
#         #'Queretaro':{'Monterrey'},
#         'Celaya':['jiloyork', 'Sinaloa'],
#         'Zacatecas':['Sonora', 'Monterrey', 'Queretaro'],
#         'Monterrey':['Zacatecas','Sinaloa'],
#         'Tamaulipas':['Queretaro'],
#         'Queretaro':['Tamaulipas', 'Zacatecas', 'Sinaloa', 'jiloyork', 'Oaxaca']

#     }
#     estado_inicial = ['jiloyork']
#     solucion = ['Oaxaca']
#     nodo_inicial = Nodo(estado_inicial, solucion)
#     nodo = DFS_prof_iter(nodo_inicial, solucion)
#     #!Mostrar resultado
#     if nodo != None:
#         resultado = []
#         while nodo.get_padre() != None:
#             resultado.append(nodo.get_datos())
#             nodo = nodo.get_padre()
#             resultado.append(estado_inicial)
#             resultado.reverse()
#             print(resultado)
            
#     else :
#         print ("Solucion no encontrada")
#! Vuelos con búsqueda con profundidad iterativa
from arbol import Nodo 

def DFS_prof_iter(nodo, solucion):
    for limite in range(0, 100):
        visitados = []
        sol = buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite)
        if sol is not None: 
            return sol
    return None


def buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite):
    
    if limite == 0:#*Caso base límite alcanzado
        if nodo.get_datos() == solucion:
            return nodo
        return None
    visitados.append(nodo)
    if nodo.get_datos() == solucion:
        return nodo
    dato_nodo = nodo.get_datos()
    lista_hijos = []
    for un_hijo in conexiones[dato_nodo]:
        hijo = Nodo(un_hijo)
        hijo.set_padre(nodo)  # *importante para reconstruir ruta

        if not hijo.en_lista(visitados):
            lista_hijos.append(hijo)

    nodo.set_hijos(lista_hijos)

    for nodo_hijo in nodo.get_hijos():
        sol = buscar_solucion_DFS_Rec(nodo_hijo, solucion, visitados, limite - 1)
        if sol is not None:
            return sol

    return None


if __name__ == "__main__":
    conexiones = {
        'jiloyork':['Celaya','CDMX', 'Queretaro'],
        'Sonora':['Zacatecas','Sinaloa'],
        'Guanajuato':['AguasCalientes'],
        'Oaxaca':['Queretaro'],
        'Sinaloa':['Celaya', 'Sonora','jiloyork'],
        'CDMX':['Queretaro', 'Sonora'],
        'Celaya':['jiloyork', 'Sinaloa'],
        'Zacatecas':['Sonora', 'Monterrey', 'Queretaro'],
        'Monterrey':['Zacatecas','Sinaloa'],
        'Tamaulipas':['Queretaro'],
        'Queretaro':['Tamaulipas', 'Zacatecas', 'Sinaloa', 'jiloyork', 'Oaxaca']
    }

    
    estado_inicial = 'jiloyork' #*usar strings, no listas
    solucion = 'Oaxaca' # *usar strings, no listas

    nodo_inicial = Nodo(estado_inicial)
    nodo = DFS_prof_iter(nodo_inicial, solucion)

    # Mostrar resultado
    if nodo is not None:
        resultado = []
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()

        resultado.reverse()
        print("Ruta encontrada:", resultado)
    else:
        print("Solución no encontrada")