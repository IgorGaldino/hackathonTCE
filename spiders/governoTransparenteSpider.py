# Author Igor Galdino

import scrapy
import os

class GovernotransparenteSpider(scrapy.Spider):
    name = 'governoTransparente'
    allowed_domains = ['http://www.governotransparente.com.br']
    pageTemp = ''
    anoTemp = ''
    def start_requests(self):
        urls = self.openLinks()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Faz a raspagem dos dados
    def parse(self, response):
        nome = response.css('h2.text-uppercase strong::text').extract_first()
        page = response.url.split("/")[-2]
        ano = response.url.split("&")[2][-4:]
        city = nome[24:][:-5]
        # Cria pasta das bases por prefeituras
        os.system("mkdir -p baseDados")
        #Arquivo com o nome da consulta e código da cidade
        file = open('./baseDados/'+page+'('+ano+').csv', 'a')
        if self.pageTemp != page or self.anoTemp != ano:
            # print('$'*30, self.pageTemp != page and self.anoTemp != ano)
            self.pageTemp = page
            self.anoTemp = ano
            head = response.css('table#datatable-buttons thead th::text').extract()
            # link que possui atributos diferente
            if page == 'consultarcontratoaditivo':
                head.remove('Número')
            else:   
                head.remove('Documento')
                head.remove('Empenho')
            file.write(self.convertToString(head, 'cidade', 'ano'))
        for tr in response.css('table#datatable-buttons tbody tr'):
            row = []
            for i in tr.css('td'):
                item = i.css('::text').extract()
                if item == []:
                    row.append('***')
                else:
                    row.append(item[0])
            file.write(self.convertToString(row, city, ano))
        # for i in response.css('table#datatable-buttons tbody tr'):
        #     row = i.css('td::text').extract()
            # row[2] = row[2].replace('\n', '')
            # file.write(self.convertToString(row, city, ano))
        file.close()

    #converte a lista para string
    def convertToString(self, row, city, year):
        line = city + '|' + year + '|'
        for i in row:
            line += i.replace('\n', '') + '|'
        line += '\n'
        return line
    
    #Abre arquivos com os links 
    def openLinks(self):
        links = []
        with open('./links/governoTransparente.txt', 'r') as file:
            for link in file:
                links.append(link)
        return links
