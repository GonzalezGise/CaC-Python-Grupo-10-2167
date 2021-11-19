userNum = int(input("Ingrese su número:"))
numA = ""
contador = 0

while contador < userNum:
    contador += 1
    numA = str(contador) * contador
    print (numA)