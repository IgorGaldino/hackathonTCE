nameFile = input('Name File: ')
with open('npd-'+nameFile+'.csv', 'w') as file:
    with open('file-npd-'+nameFile+'.csv', 'r') as arq:
        for line in arq:
            lista = line.split(',')
            for i in range(len(lista)):
                if lista[i] == 'DESEMBOLSO' or lista[i] == 'ESCRITURAL':
                    lista[6] = '"' + lista[6] if lista[6][:1] != '"' else lista[6] #Adiciona " se não tiver
                    if lista[i-1][-1:] != '"':
                        lista[i-1] = lista[i-1] + '"'
                    elif lista[i-1][-1:] == '"' and lista[i-1][-2:] == '"' and i == 7:
                        lista[i-1] = lista[i-1] + '"'
                    break
            line = ",".join(lista)
            file.write(line)
