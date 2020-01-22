links = response.xpath('//div[@class="main"]/div[@class="resultado"]/a/@href').extract()

head = response.xpath('//div[@class="main"]/div[@class="dados"]//div[@class="titulo"]/text()').extract()

body = response.xpath('//div[@class="main"]/div[@class="dados"]//div[@class="valor"]/text()').extract()
body2 = response.xpath('//div[@class="main"]/div[@class="dados"]//div[@class="valor"]/div/text()').extract()