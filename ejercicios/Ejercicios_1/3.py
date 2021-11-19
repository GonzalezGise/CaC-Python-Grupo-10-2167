textoInput = str(input("Ingrese su texto: "))
indiceInput = int(input("Ingrese índice: "))
letterInput = str(input("Ingrese nueva letra: "))

def ChangeLetterOfString(string,index,newLetter):
    output = " "
    for i in string[0:index-1]:
        output += i
    output += newLetter
    for i in string[index+1:len(string)]:
        output += i
    print(output)
    return output

ChangeLetterOfString(textoInput,indiceInput,letterInput)

