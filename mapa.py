import heapq

# Función para crear la matriz inicialmente llena de ceros
def crear_matriz(num_filas, num_columnas):
    matriz = []
    for i in range(num_filas):
        matriz.append(['0'] * num_columnas)  # Llena la matriz con '0' inicialmente
    return matriz

# Función para dibujar la matriz con diferentes símbolos para entrada, salida, obstáculos y camino
def dibujar_matriz(matriz):
    for fila in matriz:
        print(" ".join(fila))

# Función para agregar obstáculos en la matriz
def agregar_obstaculos(matriz):
    while True:
        fila_usuario = int(input('Elija una fila para agregar un obstáculo (o -1 para salir): '))
        if fila_usuario == -1:
            break
        columna_usuario = int(input('Elija una columna para agregar un obstáculo: '))
        
        if 0 <= fila_usuario < len(matriz) and 0 <= columna_usuario < len(matriz[0]):
            matriz[fila_usuario][columna_usuario] = '1'
        else:
            print('Coordenadas no son válidas')

# Función para establecer la entrada en la matriz
def establecer_entrada(matriz):
    while True:
        fila_entrada = int(input('Elija la fila para la entrada: '))
        columna_entrada = int(input('Elija la columna para la entrada: '))
        
        if 0 <= fila_entrada < len(matriz) and 0 <= columna_entrada < len(matriz[0]):
            matriz[fila_entrada][columna_entrada] = 'E'
            return (fila_entrada, columna_entrada)
        else:
            print('Coordenadas no son válidas')

# Función para establecer la salida en la matriz
def establecer_salida(matriz):
    while True:
        fila_salida = int(input('Elija la fila para la salida: '))
        columna_salida = int(input('Elija la columna para la salida: '))
        
        if 0 <= fila_salida < len(matriz) and 0 <= columna_salida < len(matriz[0]):
            matriz[fila_salida][columna_salida] = 'S'
            return (fila_salida, columna_salida)
        else:
            print('Coordenadas no son válidas')

# Función heurística para el cálculo de la distancia Manhattan
def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Algoritmo A* para encontrar el camino desde la entrada hasta la salida
def a_estrella(matriz, inicio, fin):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    vecinos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    costo_g = {inicio: 0}
    costo_f = {inicio: heuristica(inicio, fin)}
    lista_abierta = []
    heapq.heappush(lista_abierta, (costo_f[inicio], inicio))
    lista_cerrada = {}

    while lista_abierta:
        _, actual = heapq.heappop(lista_abierta)

        if actual == fin:
            # Reconstruir el camino desde la meta hasta el inicio
            camino = []
            while actual in lista_cerrada:
                camino.append(actual)
                actual = lista_cerrada[actual]
            camino.append(inicio)
            camino.reverse()  # Invertir el camino para que vaya desde inicio hasta fin
            return camino

        for dx, dy in vecinos:
            vecino = (actual[0] + dx, actual[1] + dy)
            if 0 <= vecino[0] < num_filas and 0 <= vecino[1] < num_columnas:
                if matriz[vecino[0]][vecino[1]] == '1':  # Considerar los obstáculos
                    continue
                tentative_costo_g = costo_g[actual] + 1
                if vecino not in costo_g or tentative_costo_g < costo_g[vecino]:
                    lista_cerrada[vecino] = actual
                    costo_g[vecino] = tentative_costo_g
                    costo_f[vecino] = tentative_costo_g + heuristica(vecino, fin)
                    heapq.heappush(lista_abierta, (costo_f[vecino], vecino))

    return None

# Función principal que organiza el flujo del programa
def main():
    # Crear la matriz
    num_filas = 6
    num_columnas = 6
    matriz = crear_matriz(num_filas, num_columnas)

    # Dibujar la matriz inicial
    print("Matriz inicial:")
    dibujar_matriz(matriz)

    # Llamar a la función de agregar obstáculos
    agregar_obstaculos(matriz)

    # Establecer la entrada en la matriz
    entrada = establecer_entrada(matriz)

    # Establecer la salida en la matriz
    salida = establecer_salida(matriz)

    # Dibujar la matriz con la entrada y la salida agregadas
    print("\nMatriz con entrada y salida:")
    dibujar_matriz(matriz)

    # Ejecutar el algoritmo A* para encontrar el camino
    camino = a_estrella(matriz, entrada, salida)

    # Marcar el camino en la matriz con *
    if camino:
        for paso in camino:
            if paso != entrada and paso != salida:
                matriz[paso[0]][paso[1]] = '*'
    else:
        print("No se encontró un camino desde la entrada hasta la salida.")

    # Dibujar la matriz con el camino encontrado
    print("\nMatriz con el camino encontrado:")
    dibujar_matriz(matriz)

# Llamar a la función principal si este archivo se ejecuta como el programa principal
if __name__ == "__main__":
    main()


