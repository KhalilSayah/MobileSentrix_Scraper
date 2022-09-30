# MobileSentrix_Scraper!
[MobileSentrix_logo](https://user-images.githubusercontent.com/29178160/193275448-3a3d9e11-23c9-453a-a37d-54b61779b57e.png)

MobileSentrix_Scraper is a command-line application written in Python that scrapes product data from MobileSentrix.ca. Use responsibly.

Install
-------
To install MobileSentrix_Scraper use git :
```bash
$ git clone https://github.com/KhalilSayah/MobileSentrix_Scraper
```

Setup
-------
install requirements :
```bash
$ pip install --no-cache-dir -r requirements.txt
$ cd ../mobilesentrix/mobilesentrix
```

Usage
-----
To scrap links of catégories use **catscraper spider**
```bash
$ scrapy crawl applescraper -O result.json
```
To scrap list of product on each categorie on result.json use **productscraper spider**
```bash
$ scrapy crawl productscraper -O product.json
```
To scrap details of each product on each categorie on product.json use **product_detail spider**
```bash
$ scrapy crawl product_detail -O product_details.json
```
Or, you can do all this on one commande line
```bash
$ python3 script.py
```

Info
-----
This scraper is develop by **Scrapy** : An open source and collaborative framework for extracting the data you need from websites
link : https://scrapy.org/

**Obey robots.txt rules** has been changed to False to bypass robot.txt

**Items containers** are used to store scraping items, useful to stock this data on a Sqli3 or MangoDB data base, see : https://www.youtube.com/watch?v=Ze0JRzdxVBU&t=327s&ab_channel=buildwithpython

**Items Piplines** are also used.

Comming soon
-----
1. Holding missing data
2. Holding differents localisation (ex : .com)
3. Docker image


License
-------
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.


