def multiplicacion_rusa(a, b):
    if b == 0:
        return 0
    return a + multiplicacion_rusa(a, b - 1)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
print("Resultado:", multiplicacion_rusa(a, b))

