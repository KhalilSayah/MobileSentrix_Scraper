import scrapy
import json

from ..items import MobilesentrixItem

#Get links of product list
json_file_path = "product.json"

links = []


with open(json_file_path, 'r') as j:
     data = json.loads(j.read())

for i in range(len(data)):
    links.append(data[i]["link"])


class product_detail (scrapy.Spider):
    name = "product_detail"
    #start_urls = links

    start_urls = ['https://www.mobilesentrix.ca/power-ic-chip-for-notebooks-macbooks-cd3210a0-qfn-20pin']

    def parse(self, response):

        items = MobilesentrixItem()
  
        name = response.css('div.product-name')
        p_name = name.css('h1::text').get()


        p_price = price = response.css('span.price::text')[1].get()


        p_desc = response.css('div.std').get()


        sku = str(response.css('span.label_size::text').get())
        p_sku = sku[2:]


        tag = response.css('ul.product-tags.ms-wraptgs')
        p_tags = tag.css('a::text').getall()


        bar = response.css('div.MagicToolboxSelectorsContainer')
        p_photos = bar.css('a::attr(href)').getall()

        p_image = response.css('img.no-sirv-lazy-load::attr(src)').extract()

        items["NAME"]= p_name
        items["SKU"] = p_sku
        items["PRICE"] = p_price
        items["TAGS"] = p_tags
        items["DESCRIPTION"] = p_desc
        items["IMAGE"] = p_image
        items["OTHER_IMAGES"] = p_photos

        yield items


        #yield{
                
                #'NAME' : p_name,
                #'SKU' : p_sku,
                #'PRICE' : p_price,
                #'TAGS' : p_tags,
                #'DESCRIPTION' : p_desc,
                #'IMAGE' : p_image,
                #OTHER IMAGES' : p_photos

            #}