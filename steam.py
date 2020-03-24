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
        #steam_item=Steam20Item()
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
            
           
            

            #steam_item['game_url']= game.xpath(".//@href").get()
            #steam_item['img_url']= game.xpath(".//div/img/@src").get()
            #steam_item['game_name']=game.xpath(".//div/div[@class='col search_name ellipsis']/span/text()").get()
            #steam_item['release_date']=game.xpath(".//div/div[@class='col search_released responsive_secondrow']/text()").get()
           # steam_item['platforms']=self.get_platforms(game.xpath(".//span[contains(@class, 'platform_img')or @class='vr_supported']/@class").getall())
            #steam_item['reviews_summary']=self.remove_html(game.xpath(".//span[contains(@class, 'search_review_summary')]/@data-tooltip-html").get())
            # steam_item['original_price']=game.xpath("").get()
            #steam_item['original_price']=self.get_original_price(game.xpath(".//div[contains(@class, 'search_price_discount_combined')]"))
            #steam_item['discount_rate']=self.clean_discount_rate(game.xpath(".//div[contains(@class, 'search_discount')]/span/text()").get())
            #steam_item['discounted_price']=self.clean_discounted_price(game.xpath("(.//div[contains(@class, 'search_price discounted')]/text())[2]").get())
            yield loader.load_item()