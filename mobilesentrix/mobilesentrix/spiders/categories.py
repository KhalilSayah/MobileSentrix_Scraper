import scrapy

class catcraper (scrapy.Spider):
    name = "catscraper"
    start_urls = ['https://www.mobilesentrix.ca/']


    def parse(self, response):
        
        
#Apple categories

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
        
        

#Samsung categories

        S_series = response.css('.aicon-sseries')
        list_p1ss = S_series.css('.submenu')
        
        
        Note_series = response.css('.aicon-noteseries')
        list_p2ns = Note_series.css('.submenu')

        J_series = response.css('.aicon-jseries')
        list_p3js = J_series.css('.submenu')

        A_series = response.css('.aicon-aseries')
        list_p4as = A_series.css('.submenu')

        S_others = response.css('.aicon-sothers')
        list_p5so = S_others.css('.submenu')

        
        


    #Motorola categories

        motog = response.css('.aicon-motog')
        list_p1mg = motog.css('.submenu')
        
        
        motoe = response.css('.aicon-motoe')
        list_p2me = motoe.css('.submenu')

        motoone = response.css('.aicon-motoone')
        list_p3mo = motoone.css('.submenu')

        motoedge = response.css('.aicon-motoedge')
        list_p4me = motoedge.css('.submenu')

        motoz = response.css('.aicon-motoz')
        list_p5mz = motoz.css('.submenu')

        motoothers = response.css('.aicon-motoothers')
        list_p6mo = motoothers.css('.submenu')
        
        


    #LG categories

        lgg = response.css('.aicon-lgg')
        list_p1lgg = lgg.css('.submenu')
        
        
        lgk = response.css('.aicon-lgk')
        list_p2lgk = lgk.css('.submenu')

        lgstylo = response.css('.aicon-lgstylo')
        list_p3lgs = lgstylo.css('.submenu')

        lgv = response.css('.aicon-lgv')
        list_p4lgv = lgv.css('.submenu')

        lgq = response.css('.aicon-lgq')
        list_p5lgq = lgq.css('.submenu')

        lgo = response.css('.aicon-lgothers')
        list_p6lgo = lgo.css('.submenu')
        
        

    #Game Console
        micro = response.css('.aicon-gmicro')
        list_p1micro = micro.css('.submenu')
        
        
        sony = response.css('.aicon-sony')
        list_p2sony = sony.css('.submenu')

        nitendo = response.css('.aicon-nintendo')
        list_p3nitendo = nitendo.css('.submenu')

        bcomp = response.css('.aicon-bcomponent')
        list_p4bcomp = bcomp.css('.submenu')

        
        
       


    #Refurbished categories

        riphone = response.css('.aicon-riphone')
        list_p1r = riphone.css('.submenu')
        
        
        ripad = response.css('.aicon-ripad')
        list_p2r = ripad.css('.submenu')

        rwatch = response.css('.aicon-riwatch')
        list_p3r = rwatch.css('.submenu')

        rgalaxy = response.css('.aicon-rgalaxy')
        list_p4r = rgalaxy.css('.submenu')

        rothers = response.css('.aicon-rothers')
        list_p5r = rothers.css('.submenu')

        
     #Board Components categories   

        biphone = response.css('.aicon-biphone')
        list_p1b = biphone.css('.submenu')
        
        
        bipad = response.css('.aicon-bipad')
        list_p2b = bipad.css('.submenu')

        bgalaxy = response.css('.sam_boardcomp.aicon-bsamsung')
        list_p3b = bgalaxy.css('.submenu')

        bothers = response.css('.aicon-bothers')
        list_p4b = bothers.css('.submenu')

        

        
        yield{
                'Iphone' : list_p1.css('a::attr(href)').getall(),
                'Ipad' : list_p2.css('a::attr(href)').getall(),
                'Watch' : list_p3.css('a::attr(href)').getall(),
                'macbookpro' : list_p4.css('a::attr(href)').getall(),
                'macbookair' : list_p5.css('a::attr(href)').getall(),
                'ssds' : list_p6.css('a::attr(href)').getall(),

                'S_series' : list_p1ss.css('a::attr(href)').getall(),
                'Note_series' : list_p2ns.css('a::attr(href)').getall(),
                'J_series' : list_p3js.css('a::attr(href)').getall(),
                'A_series' : list_p4as.css('a::attr(href)').getall(),
                'S_others' : list_p5so.css('a::attr(href)').getall(),

                'MotoG' : list_p1mg.css('a::attr(href)').getall(),
                'MotoE' : list_p2me.css('a::attr(href)').getall(),
                'MotoONE' : list_p3mo.css('a::attr(href)').getall(),
                'MotoEDGE' : list_p4me.css('a::attr(href)').getall(),
                'MotoZ' : list_p5mz.css('a::attr(href)').getall(),
                'Moto_others' : list_p6mo.css('a::attr(href)').getall(),

                'LG G' : list_p1lgg.css('a::attr(href)').getall(),
                'LG K' : list_p2lgk.css('a::attr(href)').getall(),
                'LG Stylo' : list_p3lgs.css('a::attr(href)').getall(),
                'LG V' : list_p4lgv.css('a::attr(href)').getall(),
                'LG Q' : list_p5lgq.css('a::attr(href)').getall(),
                'LG Others' : list_p6lgo.css('a::attr(href)').getall(),

                'Microsoft' : list_p1micro.css('a::attr(href)').getall(),
                'Sony' : list_p2sony.css('a::attr(href)').getall(),
                'Nitendo and Oculus' : list_p3nitendo.css('a::attr(href)').getall(),
                'Boards Componenets' : list_p4bcomp.css('a::attr(href)').getall(),

                'Ref Iphone' : list_p1r.css('a::attr(href)').getall(),
                'Ref Ipad' : list_p2r.css('a::attr(href)').getall(),
                'Ref Watch and Galaxy Note' : list_p3r.css('a::attr(href)').getall(),
                'Ref Galaxy' : list_p4r.css('a::attr(href)').getall(),
                'Ref Others' : list_p5r.css('a::attr(href)').getall(),

                'Board Iphone' : list_p1b.css('a::attr(href)').getall(),
                'Board Ipad' : list_p2b.css('a::attr(href)').getall(),
                'Board Samsung' : list_p3b.css('a::attr(href)').getall(),
                'Board Others' : list_p4b.css('a::attr(href)').getall()

            }