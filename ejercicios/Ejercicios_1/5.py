test = [2,3,4,5,10,8]

def Score2doLugar(input):
    output = sorted(input, reverse=True)
    print("El subcampeon saco un", output[1])
    return output[1]

resultado = Score2doLugar(test)