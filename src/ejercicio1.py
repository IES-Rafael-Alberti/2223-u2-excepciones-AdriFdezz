#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
#(desde 1 hasta su edad).

def edad_cumplida(edad):
    if edad < 1:
        raise ValueError("La edad debe ser un numero positivo")
    else:
        anios_cumplidos = "Años que ha cumplido:\n"
        for anio in range(1, edad + 1):
            anios_cumplidos += str(anio) + " "
        return anios_cumplidos

if __name__ == "__main__":
    try:
        edad = int(input("Introduce tu edad: "))
        resultado = edad_cumplida(edad)
        print(resultado)
    except ValueError as error:
        print("Error:", error)
    except Exception as error:
        print("Ocurrio un error:", error)
