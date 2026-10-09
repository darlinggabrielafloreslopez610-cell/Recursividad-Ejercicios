def contar_vocales(cadena):
    if cadena == "":
        return 0
    primera = cadena[0].lower()
    if primera in "aeiou":
        return 1 + contar_vocales(cadena[1:])
    else:
        return contar_vocales(cadena[1:])

texto = input("Ingrese un texto: ")
print("Cantidad de vocales:", contar_vocales(texto))


