import scrapy

from pep_parse.constants import URL, ALLOWED_DOMAIN
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [ALLOWED_DOMAIN]
    start_urls = [URL]

    def parse(self, response):
        peps = response.css('a.pep.reference.internal::attr(href)').getall()
        yield from response.follow_all(peps, callback=self.parse_pep)

    def parse_pep(self, response):
        name_num = response.css(
            'h1.page-title::text').get().split(' – ')
        pep_num = name_num[0][4:]
        pep_name = name_num[1]
        data = {
            'number': int(pep_num),
            'name': pep_name,
            'status': response.css(
                'dt:contains("Status")+dd ::text').get()
        }
        yield PepParseItem(data)
