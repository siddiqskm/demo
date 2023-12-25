from pathlib import Path

import scrapy


class ColesSpider(scrapy.Spider):
    name = "coles"

    def start_requests(self):
        urls = [
            "https://www.coles.com.au/browse/meat-seafood",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("Response: %s", response.body)
        for product in response.css("section[data-testid='product-tile']"):
            yield {
                "price": product.css("span.price__value::text").get(),
                "name": product.css("h2[class='LinesEllipsis  product__title']::text").get(),
            }
