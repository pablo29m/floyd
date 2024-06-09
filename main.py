INF = float('inf')

def floyd_warshall(grafo):
    V = len(grafo)
    dist = [[0]*V for _ in range(V)]

    for i in range(V):
        for j in range(V):
            dist[i][j] = grafo[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    grafo = [
        [0, 4, 8, INF, INF],
        [4, 0, 1, 2, INF],
        [8, INF, 0, 4, 2],
        [INF, 2, 4, 0, 7],
        [INF, INF, 2, 7, 0]
    ]

    print("Matriz de inicio:")
    imprimir_matriz(grafo)

    resultado = floyd_warshall(grafo)

    print("\nMatriz resultante:")
    imprimir_matriz(resultado)

main(
)