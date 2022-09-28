import scrapy

class productscraper (scrapy.Spider):
    name = "productscraper"
    start_urls = ['https://www.mobilesentrix.ca/replacement-parts/apple/macbook-parts/macbook-air/air-13-a2179']


    def parse(self, response):
        main = response.css('div.col-main')
        mainlist = main.css('div.category-products.main-list-category.deal-category')
        productlist = mainlist.css('.products-grid.product-listing.deal-category')
        
        for item in productlist.css('.item'):
            
            yield{
                'length' : len(productlist.css('.item')),
                'name' : item.css('span.product-name::text').get()
            }
