with open('../spiders/links/servidoresOrgaosFortaleza.txt', 'w') as file:
    with open('orgao.txt', 'r') as arq:
        for orgao in arq:
            orgao = orgao.rstrip()
            links = []
            for month in range(1,13):
                links = ['https://transparencia.fortaleza.ce.gov.br/index.php/servidores/consultar?nome=&orgao='+orgao+'&mes='+str(month)+'&ano=2019&funcao=',
                'https://transparencia.fortaleza.ce.gov.br/index.php/servidores/consultar?nome=&orgao='+orgao+'&mes='+str(month)+'&ano=2018&funcao=',
                'https://transparencia.fortaleza.ce.gov.br/index.php/servidores/consultar?nome=&orgao='+orgao+'&mes='+str(month)+'&ano=2017&funcao=',
                'https://transparencia.fortaleza.ce.gov.br/index.php/servidores/consultar?nome=&orgao='+orgao+'&mes='+str(month)+'&ano=2016&funcao=',
                'https://transparencia.fortaleza.ce.gov.br/index.php/servidores/consultar?nome=&orgao='+orgao+'&mes='+str(month)+'&ano=2015&funcao=']
            for link in links:
                file.write(link+'\n')