# Author Igor Galdino

import scrapy

class GovernotransparenteSpider(scrapy.Spider):
    name = 'governoTransparente'
    allowed_domains = ['http://www.governotransparente.com.br']
    def start_requests(self):
        urls = self.openLinks()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Faz a raspagem dos dados
    def parse(self, response):
        nome = response.css('h2.text-uppercase strong::text').extract_first()
        print('/*/*/*/*/*/*/*', nome)
        page = response.url.split("/")[-2]
        codCidade = response.url.split("/")[-3]
        #Arquivo com o nome da consulta e código da cidade
        file = open(page+'('+nome+').csv', 'w')
        head = response.css('table#datatable-buttons thead th::text').extract()
        # link que possui atributos diferente
        if page == 'consultarcontratoaditivo':
            head.remove('Número')
        else:
            head.remove('Documento')
            head.remove('Empenho')
        file.write(self.convertToString(head))
        for i in response.css('table#datatable-buttons tbody tr'):
            row = i.css('td::text').extract()
            row[2] = row[2].replace('\n', '')
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
        with open('links.txt', 'r') as file:
            for link in file:
                links.append(link)
        return links
