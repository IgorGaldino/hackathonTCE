# Author Igor Galdino

import scrapy
import os
class TransparenciaFortalezaSpider(scrapy.Spider):
    name = 'transparenciaFortaleza'
    allowed_domains = ['https://transparencia.fortaleza.ce.gov.br']
    def start_requests(self):
        urls = self.openLinks()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Faz a raspagem dos dados
    def parse(self, response):
        nome = response.css('main h1::text').extract_first()
        year = response.url.split("=")[1].split("&")[0]
        # Cria pasta das bases por prefeituras
        os.system("mkdir -p 'PREFEITURA DE FORTALEZA'")
        #Arquivo com o nome da consulta
        file = open('./PREFEITURA DE FORTALEZA/' + nome +'(' + year + ').csv', 'w')
        head = response.css('table.table-striped thead th::text').extract()
        head = list(map(lambda text : text.lstrip().rstrip(), head))
        if(nome == 'Contrato'):
            head.remove('Nº Cont. Instit.')
        # link que possui atributos diferente
        file.write(self.convertToString(head))
        for i in response.css('table.table-striped tbody tr'):
            row = i.css('td::text').extract()
            # row[6] = row[6].rstrip()
            file.write(self.convertToString(row))
        file.close()

    #converte a lista para string
    def convertToString(self, row):
        line = ''
        for i in row:
            line += i + '|'
        line += '\n'
        return line

    #Abre arquivos com os links 
    def openLinks(self):
        links = []
        with open('./links/transparenciaFortaleza.txt', 'r') as file:
            for link in file:
                links.append(link)
        return links