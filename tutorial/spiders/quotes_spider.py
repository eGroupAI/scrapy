import scrapy


class Mobile01Spider(scrapy.Spider):
    name = "mobile01"

    def start_requests(self):
        urls = [
            'https://www.mobile01.com/category.php?id=6',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'mobile01-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)