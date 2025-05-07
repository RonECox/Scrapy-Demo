import scrapy


class DriversSpider(scrapy.Spider):
    name = 'drivers'
    allowed_domains = ['googlechromelabs.github.io']
    start_urls = ['https://googlechromelabs.github.io/chrome-for-testing/']

    def parse(self, response):
        for section in response.xpath('//section[contains(@class, "status-ok")]'):
            channel = section.xpath('./@id').get()
            version = section.xpath('./p/code[1]/text()').get()
            revision = section.xpath('./p/code[2]/text()').get()

            for row in section.xpath('.//table//tr[contains(@class, "status-ok")]'):
                binary = row.xpath('.//th[1]/code/text()').get()
                platform = row.xpath('.//th[2]/code/text()').get()
                url = row.xpath('.//td[1]/code/text()').get()
                http_status = row.xpath('.//td[2]/code/text()').get()

                yield {
                    "channel": channel,
                    "version": version,
                    "revision": revision,
                    "binary": binary,
                    "platform": platform,
                    "url": url,
                    "http_status": http_status,
                }
