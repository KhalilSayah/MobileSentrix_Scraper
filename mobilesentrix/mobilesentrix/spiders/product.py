from tracemalloc import start
import scrapy
import json

#get urls links

dump_file_path = "Apple_start_urls.txt"
json_file_path = "result.json"

links = []
f = open(dump_file_path, "w")

with open(json_file_path, 'r') as j:
     data = json.loads(j.read())

keys = []
for key in data[0]:
    
    keys.append(key)
    for link in data[0][key]:
        links.append(link)
        
        


f.write(str(links))

class productscraper (scrapy.Spider):



    name = "productscraper"

    #with open(starts_urls_path, 'r') as f:
        #start_urls = f.read()

    start_urls = links
    


    def parse(self, response):
        i = 0
        main = response.css('div.col-main')
        mainlist = main.css('div.category-products.main-list-category.deal-category')
        productlist = mainlist.css('.products-grid.product-listing.deal-category')
        
        for item in productlist.css('.item'):
            i += 1
            yield{
                
                'name' : item.css('span.product-name::text').get(),
                'price' : item.css('span.price::text').get(),
                'link' : item.css('a::attr(href)').get()
                
  
            }
    #Stats 
    s = open("stats.txt", "w")
    s.write("Number of links crawled :" + str(len(start_urls))+"\n"+"Categories crawled :" + str(keys)) 


