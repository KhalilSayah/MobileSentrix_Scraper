import scrapy

class product_detail (scrapy.Spider):
    name = "product_detail"
    start_urls = ['https://www.mobilesentrix.ca/oled-assembly-compatible-for-iphone-13-refurbished']


    def parse(self, response):
  
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

        yield{
                
                'NAME' : p_name,
                'SKU' : p_sku,
                'PRICE' : p_price,
                'TAGS' : p_tags,
                'DESCRIPTION' : p_desc,
                'IMAGE' : p_image,
                'OTHER IMAGES' : p_photos

            }