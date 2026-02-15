# 알라딘 사이트에서 "자기계발" 페이지 접속 후 책 20권 (제목 / 저자 / 출판사 / 가격 / 포인트 / URL) 크롤링
# Scrapy + Selenium 데이터 수집
# CSV 저장
import scrapy
from aladin.items import AladinItem
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class SeleniumTestSpider(scrapy.Spider):
    name = "selenium_test"
    allowed_domains = ["www.aladin.co.kr"]
    start_urls = ["https://www.aladin.co.kr/shop/wbrowse.aspx?CID=336"]

    def __init__(self):
        headlessoptions = webdriver.ChromeOptions()
        headlessoptions.add_argument("--headless=new")
        service = Service(r"./drivers/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=headlessoptions)

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(2)

        items = self.driver.find_elements(By.CSS_SELECTOR, "ul.b-booklist > li")[:20]
        for i, item in enumerate(items, 1):
            try:
                title = item.find_element(By.CSS_SELECTOR, "div.b-text h4 a").text.strip()
                author = item.find_element(By.CSS_SELECTOR, "div.b-author").text.split("|")[0].strip()
                publisher = item.find_element(By.CSS_SELECTOR, "div.b-author").text.split("|")[1].strip()
                price = item.find_element(By.CSS_SELECTOR, "div.b-price strong").text.strip()
                point = item.find_element(By.CSS_SELECTOR, "div.b-price").text.split("/")[1].replace("원", "").strip()
                url = item.find_element(By.CSS_SELECTOR, "div.b-cover > a").get_attribute("href")
            except: 
                continue

            item = AladinItem()
            item["rank"] = i
            item["title"] = title
            item["author"] = author
            item["publisher"] = publisher
            item["price"] = price
            item["point"] = point
            item["url"] = url

            yield item

    def closed(self, reason) :
        self.driver.quit()
