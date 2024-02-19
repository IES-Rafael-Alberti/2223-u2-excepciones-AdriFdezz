#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
#todos los números impares desde 1 hasta ese número separados por comas.

def numeros_impares(numero):
    if numero < 1:
        raise ValueError("El numero debe ser positivo")
    
    impares = [str(impar) for impar in range(1, numero + 1) if impar % 2 != 0]
    resultado = ", ".join(impares)
    
    if resultado:
        return resultado
    else:
        return "No hay numeros impares en el rango"

if __name__ == "__main__":
    try:
        numero = int(input("Introduce un numero entero positivo: "))
        resultado = numeros_impares(numero)
        print("Numeros impares desde 1 hasta", numero, "son:", resultado)
    except ValueError as error:
        print("Error:", error)
    except Exception as error:
        print("Ocurrio un error:", error)
