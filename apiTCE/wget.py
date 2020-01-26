import os

method = 'contratos'
codes = []
with open('./baseDados/municipios.csv', 'r') as file:
    for line in file:
        codes.append(line.split('"')[1])
for code in codes:
    os.system('wget https://api.tce.ce.gov.br/index.php/sim/1_0/'+method+'.csv?codigo_municipio='+code+'&data_contrato=20150101_20191231 -O '+ method+'-'+code+'.csv')
