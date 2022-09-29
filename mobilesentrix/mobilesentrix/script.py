import os 

os.system('scrapy crawl applescraper -O result.json;scrapy crawl productscraper -O product.json;scrapy crawl product_detail -O product_details.json;')