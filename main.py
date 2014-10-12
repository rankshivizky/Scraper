import json
import requests
from scrapy import Spider, Item, Field


class Shoe(Item):
    title = Field()
    available_sizes = Field()


class ShoeReader(Spider):
    name, start_urls = 'shoeSpider', ['http://www.roadrunnersports.com/rrs/products/ASC1724/?cc=BLLM460']

    def parse(self, resp):
        product_id = resp.css('.prod_itemid::text')[0].extract().split('#')[1]
        resp = requests.post('http://www.roadrunnersports.com/rrs/product-detail/build-selections.jsp',
                             {'id': product_id})
        shoe_colors = json.loads(resp.text.split('$+$')[1].replace('\'', '"'))['Color']
        for color, details in shoe_colors.iteritems():
            print color, details