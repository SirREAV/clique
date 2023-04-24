from time import time

# Fucionalidades
def cargar_grafo(nombre_del_grafo, dirigido):
    Grafo = {}
    with open(nombre_del_grafo, 'r') as archivo:
        for linea in archivo:
            if linea.startswith('e'):
                _, nodoA, nodoB = linea.split()
                if nodoA not in Grafo:
                    Grafo[nodoA] = []
                if nodoB not in Grafo:
                    Grafo[nodoB] = []
                if not nodoB in Grafo[nodoA]:
                    Grafo[nodoA].append(nodoB)
                if not dirigido and not nodoA in Grafo[nodoB]:
                    Grafo[nodoB].append(nodoA)
    return Grafo


def ordenar_listas_desc(lista_de_listas):
    return sorted(lista_de_listas, key=len, reverse=True)


def buscar_clique_maximo(Grafo, n_cliques, clique_encontrado_actual=[], nodos_restantes=[], nodos_omitidos=[]):
    if len(nodos_restantes) == 0 and len(nodos_omitidos) == 0:
        n_cliques.append(clique_encontrado_actual)
        return 1
    cliques_encontrados = 0
    for nodo in nodos_restantes:
        nuevo_posible_clique = clique_encontrado_actual + [nodo]
        nuevos_nodos_restantes = [
            N for N in nodos_restantes if N in Grafo[nodo]]
        nuevos_nodos_omitidos = [N for N in nodos_omitidos if N in Grafo[nodo]]
        cliques_encontrados += buscar_clique_maximo(
            Grafo, n_cliques, nuevo_posible_clique, nuevos_nodos_restantes, nuevos_nodos_omitidos)
        #  RECURSION
        # print("#", nuevo_posible_clique)
        nodos_restantes.remove(nodo)
        nodos_omitidos.append(nodo)
    return cliques_encontrados


def modelo_clique(nombre_archivo, dirigido):
    Grafo = cargar_grafo(nombre_archivo, dirigido)
    Cliques_totales = []
    tiempo_inicio = time()
    Num_cliques = buscar_clique_maximo(Grafo=Grafo, n_cliques=Cliques_totales, nodos_restantes=list(Grafo.keys()))
    tiempo_final = time()

    Cliques_totales = ordenar_listas_desc(Cliques_totales)
    Clique_maximo = Cliques_totales[0]
    print(f"Nodos del clique máximo: {Clique_maximo}")
    print(f"Cantidad de cliques en el grafo: {Num_cliques}")
    print(f"Tiempo de ejecucion: {tiempo_final - tiempo_inicio}")


modelo_clique("Examples/le450_5a.col", True)
# Cliques_totales = []
# tiempo_inicio= time()
# Num_cliques = buscar_clique_maximo(Grafo=chat, n_cliques=Cliques_totales, nodos_restantes=list(chat.keys()))
# tiempo_final= time()

# Cliques_totales = ordenar_listas_desc(Cliques_totales)
# Clique_maximo = Cliques_totales[0]
# print(f"Nodos del clique máximo: {Clique_maximo}")
# print(f"Cantidad de cliques en el grafo: {Num_cliques}")
# print(f"Tiempo de ejecucion: {tiempo_final - tiempo_inicio}")


# Ejemplos

chat = {
    0: [1, 3, 4, 5, 6, 7],
    1: [0, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    2: [1, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    3: [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11],
    4: [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11],
    5: [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11],
    6: [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12],
    7: [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12],
    8: [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12],
    9: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12],
    10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12],
    11: [2, 3, 4, 5, 6, 7, 8, 9, 10, 12],
    12: [6, 7, 8, 9, 10, 11]
}


Grafo_Ejemplo1 = {
    "A": ["B", "K", "H", "M", "G", "J"],
    "B": ["A", "C", "E"],
    "C": ["B", "D", "H"],
    "D": ["C", "E", "F", "L"],
    "E": ["B", "D", "F", "L"],
    "F": ["E", "L", "D"],
    "J": ["M", "G", "K", "A", "H"],
    "H": ["C", "A", "K", "G", "M", "J"],
    "K": ["A", "H", "J", "M", "G"],
    "M": ["J", "H", "A", "K", "G"],
    "G": ["M", "K", "H", "J", "A"],
    "L": ["E", "F", "D"]
}

Grafo_Ejemplo2 = {
    "1": ["2", "5"],
    "2": ["1", "3", "5"],
    "3": ["2", "4"],
    "4": ["3", "6", "5"],
    "5": ["1", "2", "4"],
    "6": ["4"]
}
