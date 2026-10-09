def imprimir_patron(n, nivel=1):
    if nivel > n:
        return
    print("*" * nivel)
    imprimir_patron(n, nivel + 1)

n = int(input("Ingrese un número: "))
imprimir_patron(n)

