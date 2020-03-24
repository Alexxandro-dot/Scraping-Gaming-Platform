# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import Steam20Item

from scrapy.selector import Selector

class SteamSpider(scrapy.Spider):
    name = 'steam'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/?l=german&filter=topsellers/']
    
    def parse(self, response):
       
        games=response.xpath("//div[@id='search_resultsRows']/a")
        for game in games:
            loader= ItemLoader(item= Steam20Item(), selector=game, response=response)
            loader.add_xpath("game_name", ".//div/div[@class='col search_name ellipsis']/span/text()")
            loader.add_xpath("release_date", ".//div/div[@class='col search_released responsive_secondrow']/text()")
            loader.add_xpath("original_price", ".//div[contains(@class, 'search_price_discount_combined')]")
            loader.add_xpath("discount_rate", ".//div[contains(@class, 'search_discount')]/span/text()")
            loader.add_xpath("discounted_price", "(.//div[contains(@class, 'search_price discounted')]/text())[2]")
            loader.add_xpath("game_url", ".//@href")
            loader.add_xpath('img_url', ".//div/img/@src")
            loader.add_xpath("platforms", ".//span[contains(@class, 'platform_img')or @class='vr_supported']/@class")
            loader.add_xpath("reviews_summary", ".//span[contains(@class, 'search_review_summary')]/@data-tooltip-html")
            yield loader.load_item()
