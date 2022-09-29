import os 

os.system('scrapy crawl applescraper -O cat_link.json; scrapy crawl productscraper -O product.json; scrapy crawl product_detail -O Product_details.json')