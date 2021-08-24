def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        id = input("¿Tienes identificación oficial? (s/n): ")
        if id == "s":
            print("Trámite de licencia concedido")
        else:
            if id != "s" and id != "n":
                print("Respuesta incorrecta")

            else:    
                print("No cumples requisitos") 
    else:
        if edad <= 0:
            print("Respuesta incorrecta")
        else:
            print("No cumples requisitos")


if __name__ == '__main__':
    main()
