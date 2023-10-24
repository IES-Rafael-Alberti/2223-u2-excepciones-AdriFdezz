#Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError 
#con el mensaje, "Incorrect Password!!"

def verificar_contrasenia(contraseña_ingresada):
    contraseña_correcta = "hola123"

    if contraseña_ingresada != contraseña_correcta:
        raise NameError("Incorrect Password!!")

if __name__ == "__main__":
    try:
        contraseña = input("Introduce la contraseña: ")
        verificar_contrasenia(contraseña)
        print("Contraseña correcta")
    except NameError as error:
        print(error)