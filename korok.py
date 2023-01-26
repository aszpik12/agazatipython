def fel2():
    lista=[]
    index = 1

    while index <= 5:
        kor = int(input(str(index) + " " + "idős ember kora: "))
        index += 1
        lista.append(kor)

    print("II/A, B, C:")
    print("\t", end="")
    index = 0
    db = len(lista)-1
    while index < len(lista)-1:
        print(lista[index], end=" : ")
        index += 1
    print(lista[db])


    print("II/D, E:")
    print("\tElső idős ember korának helye a listában: {}".format(elso_idos(lista)))

def elso_idos(lista):
    elso = 0
    index = len(lista)
    while index > 0:
        if lista[index-1] > 70:
            elso = index-1
        index-=1
    return elso




