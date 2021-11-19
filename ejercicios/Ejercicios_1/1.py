myString = "Hola como estas"

def guionizador(input):
    output = input.replace(" ","-")
    print(output)
    return output

output = guionizador(myString)


