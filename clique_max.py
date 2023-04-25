from time import time
from random import choice

# Algoritmo Bron–Kerbosch sin pivote
def BronKerbosch1(Grafo, P, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from BronKerbosch1(Grafo, P=P.intersection(Grafo[v]), R=R.union([v]), X=X.intersection(Grafo[v]))
        X.add(v)


# Algoritmo Bron–Kerbosch con pivote
def BronKerbosch2(Grafo, P, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    try:
        u = choice(list(P.union(X)))
        S = P.difference(Grafo[u])
    # if union of P and X is empty
    except IndexError:
        S = P
    for v in S:
        yield from BronKerbosch2(Grafo, P=P.intersection(Grafo[v]), R=R.union([v]), X=X.intersection(Grafo[v]))
        P.remove(v)
        X.add(v)


def cargar_grafo(nombre_del_grafo, dirigido):
    n_aristas = 0
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
                    n_aristas += 1
                if not dirigido and not nodoA in Grafo[nodoB]:
                    Grafo[nodoB].append(nodoA)
                    n_aristas += 1
    # Ordenar el grafo solo favorece para los cliques de grafos dirigidos
    #tuplas_ordenadas = sorted(Grafo.items(), key=lambda x: int(x[0]))
    #Grafo_ordenado = {str(clave): valor for clave, valor in tuplas_ordenadas}
    return Grafo, n_aristas


def ordenar_listas_desc(lista_de_listas):
    return sorted(lista_de_listas, key=len, reverse=True)

#Sin pivote
def ejecutar_modelo1(nombre_archivo, dirigido):
    Grafo, n_aristas = cargar_grafo(nombre_archivo, dirigido)
    
    # Ejecución del algoritmo
    tiempo_inicio = time()
    cliques = ordenar_listas_desc(list(BronKerbosch1(Grafo, Grafo.keys()))) # P = {Nodos}
    tiempo_final = time()
    tiempo_en_ejecucion = tiempo_final - tiempo_inicio
    
    # Clasificación de cliques encontrados según su tamaño
    cantidades = {}
    for clique in cliques:
        tamano_clique = len(clique)
        if not tamano_clique in cantidades:
            cantidades[tamano_clique] = 1
        else:
            cantidades[tamano_clique] += 1
    cantidades = dict(sorted(cantidades.items()))
    
    # Mensajes
    tipo = "dirigido" if dirigido else "No dirigido" 
    info = f"Tipo de grafo: {tipo}"
    info += f"Nodos: {len(Grafo)}, Aristas: {n_aristas}\n"
    info += f"Clique maximo: {cliques[0]}\n"
    info += f"Cantidad de cliques en el grafo: {len(cliques)}"
    info += f"Cantidades de cliques: {cantidades}"
    info += f"Tiempo de ejecucion: {tiempo_en_ejecucion} segundos"

    # Resultados
    # print(f"Nodos: {len(Grafo)}, Aristas: {n_aristas}")
    # print(f"Clique maximo: {cliques[0]}")
    # print(f"Cantidad de cliques en el grafo: {len(cliques)}")
    # print(f"Cantidades de cliques: {cantidades}")
    # sprint(f"Tiempo de ejecucion: {tiempo_en_ejecucion} segundos")

    return Grafo, n_aristas, cliques, cantidades, tiempo_en_ejecucion, info


#Con pivote
def ejecutar_modelo2(nombre_archivo, dirigido):
    Grafo, n_aristas = cargar_grafo(nombre_archivo, dirigido)
    
    # Ejecución del algoritmo
    tiempo_inicio = time()
    cliques = ordenar_listas_desc(list(BronKerbosch2(Grafo, Grafo.keys()))) # P = {Nodos}
    tiempo_final = time()
    tiempo_en_ejecucion = tiempo_final - tiempo_inicio
    
    # Clasificación de cliques encontrados según su tamaño
    cantidades = {}
    for clique in cliques:
        tamano_clique = len(clique)
        if not tamano_clique in cantidades:
            cantidades[tamano_clique] = 1
        else:
            cantidades[tamano_clique] += 1
    cantidades = dict(sorted(cantidades.items()))
    
    # DETALLES
    tipo = "dirigido" if dirigido else "No dirigido" 
    info = f"Tipo de grafo: {tipo}"
    info += f"Nodos: {len(Grafo)}, Aristas: {n_aristas}\n"
    info += f"Clique maximo: {cliques[0]}\n"
    info += f"Cantidad de cliques en el grafo: {len(cliques)}"
    info += f"Cantidades de cliques: {cantidades}"
    info += f"Tiempo de ejecucion: {tiempo_en_ejecucion} segundos"
    
    return Grafo, n_aristas, cliques, cantidades, tiempo_en_ejecucion, info