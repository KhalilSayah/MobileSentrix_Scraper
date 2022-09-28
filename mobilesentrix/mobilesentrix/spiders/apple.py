import scrapy

class applescraper (scrapy.Spider):
    name = "applescraper"
    start_urls = ['https://www.mobilesentrix.ca/']


    def parse(self, response):
        A_cat = ["'.aicon-iphone'","'.aicon-ipad'","'.aicon-watch'","'.aicon-ipod'","'.macbookmenuloginas.aicon-macbookpro'","'.macbookmenuloginas.aicon-macbookair'","'.mac-board-com aicon-ssds'"]

        

        iphone = response.css('.aicon-iphone')
        list_p1 = iphone.css('.submenu')
        
        
        ipad = response.css('.aicon-ipad')
        list_p2 = ipad.css('.submenu')

        watch = response.css('.aicon-watch')
        list_p3 = watch.css('.submenu')

        macbookpro = response.css('.macbookmenuloginas.aicon-macbookpro')
        list_p4 = macbookpro.css('.submenu')

        macbookair = response.css('.macbookmenuloginas.aicon-macbookair')
        list_p5 = macbookair.css('.submenu')

        ssds = response.css('.mac-board-com.aicon-ssds')
        list_p6 = ssds.css('.submenu')
        
        yield{
                
                'Iphone' : list_p1.css('a::attr(href)').getall(),
                'Ipad' : list_p2.css('a::attr(href)').getall(),
                'Watch' : list_p3.css('a::attr(href)').getall(),
                'macbookpro' : list_p4.css('a::attr(href)').getall(),
                'macbookair' : list_p5.css('a::attr(href)').getall(),
                'ssds' : list_p6.css('a::attr(href)').getall()

            }

            