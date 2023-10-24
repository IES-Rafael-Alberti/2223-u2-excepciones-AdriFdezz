#Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje
#"La entrada no es correcta" y lanzará la excepción capturada.

def numero_entero(numero):
    if int(numero) != numero:
        raise ValueError("La entrada no es correcta")
    return numero

if __name__ == "__main__":
    try:
        entrada = float(input("introduce un numero: "))
        resultado = numero_entero(entrada)
        print("Numero introducido:", resultado)
    except ValueError as error:
        print(error)

