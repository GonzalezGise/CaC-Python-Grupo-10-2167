def stringChanged():

    textoNew = []
    
    stringUser = str(input("Ingrese su texto a modificar: "))
    textoNew.append(stringUser)
    
    indiceString = int(input("ingrese el lugar del texto que quiere modificar: "))

    letraReemplazar = str(input("Ingrese letra nueva: "))

    print(stringUser)
    print(indiceString)
    print(letraReemplazar)

    if indiceString <= len(stringUser):
        stringUser[int(indiceString)] = stringUser.replace(letraReemplazar)
        print(stringUser)
    else:
        print("El índice proporcionado no esta en el string")


stringChanged()

