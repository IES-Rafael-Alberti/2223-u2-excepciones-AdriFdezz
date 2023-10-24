#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás 
#desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.

def cuenta_atras(numero):
    if numero < 0:
        raise ValueError("El numero debe ser positivo")
    cuenta_regresiva = list(range(numero, -1, -1))
    cuenta_regresiva_str = ', '.join(map(str, cuenta_regresiva))
    return cuenta_regresiva_str

if __name__ == "__main__":
    numero = -1
    while numero < 0:
        try:
            numero = int(input("Introduce un numero entero positivo: "))
            if numero < 0:
                raise ValueError("El numero debe ser positivo")
        except ValueError:
            print("Error: Debes introducir un numero entero valido")

    resultado = cuenta_atras(numero)
    print("Cuenta atras desde", numero, "hasta 0:", resultado)

