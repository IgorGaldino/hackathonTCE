nameFile = input('name File: ')
tam = 25
with open('./baseDados/' +nameFile+ '.csv', 'w') as file:
    with open('./baseDados/' +nameFile+ '.backup.csv', 'r') as arq:
        cont = 0
        for line in arq:
            lista = line.split('|')
            # lista = list(map(lambda text : text.lstrip().rstrip(), lista))
            if not (len(lista) <= tam):
                print(lista)
                lista[tam-1] = '\n' + lista[tam-1]
                cont += 1
            file.write('|'.join(lista))
