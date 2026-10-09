def flatten(lista):
    if not lista:
        return []
    primero, resto = lista[0], lista[1:]
    if isinstance(primero, list):
        return flatten(primero) + flatten(resto)
    else:
        return [primero] + flatten(resto)

# Aquí pedimos al usuario una lista en formato Python
entrada = eval(input("Ingrese una lista (ej: [1, [2, [3, 4], 5]]): "))
print("Lista plana:", flatten(entrada))

