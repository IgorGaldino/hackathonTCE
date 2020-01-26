# Author Igor Galdino

import scrapy
import os

class GetMunicipioSpider(scrapy.Spider):
    name = 'getMunicipio'
    allowed_domains = ['https://api.tce.ce.gov.br']
    method = 'notas_pagamentos'

    def start_requests(self):
        os.system('rm -f ./baseDados/municipio-'+self.method+'.csv')
        codes = self.getCodes()
        for code in codes:
            # for year in range(2010, 2020):
            url = 'https://api.tce.ce.gov.br/index.php/sim/1_0/'+self.method+'?codigo_municipio='+code+'&exercicio_orcamento='+str(2019)+'00'
            # url = "https://api.tce.ce.gov.br/index.php/sim/1_0/agentes_publicos?codigo_municipio="+code+"&exercicio_orcamento="+str(year)+"00"
            yield scrapy.Request(url=url, callback=self.parse)

    # Faz a raspagem dos dados
    def parse(self, response):
        body = []
        head = response.xpath('//table[@class="ok"]//tr/th/text()').extract()
        for i in response.xpath('//table[@class="ok"]//tr/td'):
            body.append(i.xpath('text()').extract_first())
        with open('./baseDados/municipio-'+self.method+'.csv', 'a') as file:
            file.write(self.convertToString(body, len(head)))

    #converte a lista para string
    def convertToString(self, row, tam):
        data = ''
        cont = 0
        for item in row:
            if item == None:
                item = '-'
            if cont == tam:
                data += '\n'
                cont = 0
            data += item + '|'
            cont += 1
        return data

    #Abre arquivos com os links 
    def getCodes(self):
        codes = []
        with open('./baseDados/municipios.csv', 'r') as file:
            for line in file:
                codes.append(line.split('"')[1])
        return codes