nameFile = input('Name File: ')
with open('file-npd-'+nameFile+'.csv', 'w') as file:
    with open('./files/npd-'+nameFile+'.csv', 'r') as arq:
        for line in arq:
            if not ',,' in line[-3:]:
                line = line[:-1]
            file.write(line)