import scrapy

class productscraper (scrapy.Spider):
    name = "productscraper"
    start_urls = ['https://www.mobilesentrix.ca/replacement-parts/apple/iphone-parts/iphone-13-mini']


    def parse(self, response):
        main = response.css('div.col-main')
        mainlist = main.css('div.category-products.main-list-category.deal-category')
        productlist = mainlist.css('.products-grid.product-listing.deal-category')
        
        for item in productlist.css('.item'):
            
            yield{
                
                'name' : item.css('span.product-name::text').get(),
                'price' : item.css('span.price::text').get(),
                'link' : item.css('a::attr(href)').get()
                
            }
