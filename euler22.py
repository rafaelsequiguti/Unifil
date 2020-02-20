def euler22():
    file = open("names.txt", 'r')

    text = file.read()
    text = text.replace("\"","")
    #print(text)
    names = text.split(",")
    

    letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    somaLetras = 0

    names.sort()

    #print(names)

    for x in range(0,len(names)):  #escolher o nome
        atual = names[x]
        soma = 0
        for i in range(0,len(atual)):  #somar as letras do nome
            letra = ""
            for y in range(0,len(letter)):
                if atual[i] == letter[y]:
                    letra = letter[y]
                    soma += y + 1
        index = names.index(atual) +1
        #print(index)
        soma *= index
        somaLetras += soma
    print(somaLetras)
    print(len(names))
        
euler22()


