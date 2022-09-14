import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_data_with_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
    try:
        driver = webdriver.Firefox(
            executable_path="C:/Users/shapi/PycharmProjects/ParserProject/geckodriver.exe",
            options=options,
         )
        driver.get(url=url)
        element = driver.find_elements(By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[3]/main/div[2]')
        for elements in element:
            print(elements.text)

        time.sleep(5)

    except Exception as ex:
         print(ex)
    finally:
         driver.close()
         driver.quit()


get_data_with_selenium('https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273')





