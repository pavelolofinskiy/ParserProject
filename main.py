import time
from json import JSONDecoder
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


def get_data_with_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
    try:
        driver = webdriver.Firefox(
            executable_path="C:/Users/shapi/PycharmProjects/ParserProject/geckodriver.exe",
            options=options,
         )
        driver.get(url=url)
 

        date = driver.find_elements(By.XPATH, "//span[@class='date-posted']")
        for dates in date:
            print(dates.text)

        location = driver.find_elements(By.XPATH, "//div[@class='location']")
        for obj in location:
            locations = obj.find_element(By.TAG_NAME, 'span')
            print(locations.text)

        description = driver.find_elements(By.XPATH, "//div[@class='description']")
        for descriptions in description:
            print(descriptions.text)

        title = driver.find_elements(By.XPATH, "//a[contains(@class,'title')]")
        for titles in title:
            print(titles.text)

        price = driver.find_elements(By.XPATH, "//div[contains(@class,'price')]")
        for prices in price:
            print(prices.text)

        images = driver.find_elements(By.XPATH, '//img')
        for img in images:
            if "https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/" in img.get_attribute('src'):
                print(img.get_attribute('src'))



        time.sleep(5)

    except Exception as ex:
         print(ex)
    finally:
         driver.close()
         driver.quit()

get_data_with_selenium('https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273')





