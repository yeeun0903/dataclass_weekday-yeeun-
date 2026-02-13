# 알라딘 사이트에서 "자기계발" 페이지 접속 후 책 20권 (제목 / 저자 / 출판사 / 가격 / 포인트 / URL) 크롤링
# Scrapy + Selenium 데이터 수집
# CSV 저장


import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class SeleniumTestSpider(scrapy.Spider):
    name = "selenium_test"
    allowed_domains = ["www.aladin.co.kr/shop/wbrowse.aspx?CID=38400"]
    start_urls = ["https://www.aladin.co.kr/shop/wbrowse.aspx?CID=38400"]

    def __init__(self):
        headlessoptions = webdriver.ChromeOptions()
        headlessoptions.add_argument("--headless=new")
        service = Service(r"./drivers/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=headlessoptions)

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(2)

        items = self.driver.find_element(By.CSS_SELECTOR, "div.ss_book_box")
        for i, item in enumerate(items, 1):
            title = item.find_element(By.CSS_SELECTOR, "a.bo3").get()
            author =



        yield item

    def closed(self, reason) :
        self.driver.quit()
