from scrapy import signals

import re

from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('window-size=1200x600')
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.ixigua.com/c/user/article/?user_id=67198009423&max_behot_time=0&max_repin_time=0&count=20&page_type=0')
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//pre[@style]"))
        )
    print(driver.page_source)