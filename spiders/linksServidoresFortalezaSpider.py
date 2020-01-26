# Author Igor Galdino

import scrapy
import os

class LinksServidoresFortalezaSpider(scrapy.Spider):
    name = 'linksServidoresFortalezaSpider'
    allowed_domains = ['https://transparencia.fortaleza.ce.gov.br']
    def start_requests(self):
        os.system('rm -f ./links/servidoresFortaleza.txt')
        urls = self.openLinks()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Faz a raspagem dos dados
    def parse(self, response):
        links = response.xpath('//div[@class="main"]/div[@class="resultado"]/a/@href').extract()
        with open('./links/servidoresFortaleza.txt', 'a') as file:
            for params in links:
                file.write('https://transparencia.fortaleza.ce.gov.br/index.php/servidores/'+ params + '\n')

    #Abre arquivos com os links 
    def openLinks(self):
        links = []
        with open('./links/servidoresOrgaosFortaleza.txt', 'r') as file:
            for link in file:
                links.append(link)
        return links