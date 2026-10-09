def caminos(n, m):
    if n == 1 or m == 1:
        return 1
    return caminos(n - 1, m) + caminos(n, m - 1)

filas = int(input("Ingrese número de filas: "))
columnas = int(input("Ingrese número de columnas: "))
print("Número de caminos posibles:", caminos(filas, columnas))

