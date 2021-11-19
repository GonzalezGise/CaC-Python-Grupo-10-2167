test = "Test InpUT"

def Swaperino(strInput):
    output = ""
    for i in strInput:
        if(i.isupper()):
            #output.append(i.lower())
            output+= i.lower()
        else:
            #output.append(i.upper())
            output+= i.upper()             
    print(output)

Swaperino(test)
