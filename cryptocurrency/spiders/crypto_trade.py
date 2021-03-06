import scrapy
from selenium import webdriver
from scrapy.selector import Selector


class CryptoTradeSpider(scrapy.Spider):
    name = 'crypto_trade'
    #allowed_domains = ['https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/']
    allowed_domains = ["*"]
    start_urls = ['https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/']

    def __init__(self):
        driver = webdriver.Chrome(executable_path='/Users/preface_ehsan/Desktop/Project/linkedin/linkedin/chromedriver')
        driver.set_window_size(1920, 1080)
        driver.get('https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/')

        rur_tab = driver.find_element_by_xpath('//*[@id="marketOverviewContainer"]/section/div/article/div/div[1]/div[5]')
        rur_tab.click()
        self.html = driver.page_source

       # driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS')]"):
            yield {
                'currency pair' : currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h)' : currency.xpath(".//div[2]/span/text()").get()
            }