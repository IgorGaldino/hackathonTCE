method = 'contratados'
with open('./baseDados/municipio-'+method+'V2.csv', 'w') as file:
    with open('./baseDados/municipio-'+method+'.csv', 'r') as arq:
        for line in arq:
            file.write(line.replace('|', ';'))