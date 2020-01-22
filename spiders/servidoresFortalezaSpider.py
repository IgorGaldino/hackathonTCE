# Author Igor Galdino

import scrapy
import os

class LinksServidoresFortalezaSpider(scrapy.Spider):
    name = 'linksServidoresFortalezaSpider.py'
    allowed_domains = ['https://transparencia.fortaleza.ce.gov.br']
    count = 1
    def start_requests(self):
        os.system('rm -f ./baseDados/servidoresFortaleza.csv')
        urls = self.openLinks()
        for url in urls:
            print('#'*30, self.count)
            self.count += 1
            yield scrapy.Request(url=url, callback=self.parse)

    # Faz a raspagem dos dados
    def parse(self, response):
        year = response.url.split('=')[-1:][0]
        month = response.url.split('=')[-2:][0][:2]
        body1 = response.xpath('//div[@class="main"]/div[@class="dados"]//div[@class="valor"]/text()').extract()
        body2 = response.xpath('//div[@class="main"]/div[@class="dados"]//div[@class="valor"]/div/text()').extract()
        body = body1 + body2
        with open('./baseDados/servidoresFortaleza.csv', 'a') as file:
            file.write(self.convertToString(str(body), year, month))

    #converte a lista para string
    def convertToString(self, row, year, month):
        rem = "[]'"
        for i in rem:
            row = row.replace(i,'')
        row = year + '|' + month + '|' + row.replace(', ', '|')
        row += '\n'
        return row

    #Abre arquivos com os links 
    def openLinks(self):
        links = []
        with open('./links/servidoresFortaleza.txt', 'r') as file:
            for link in file:
                links.append(link)
        return links