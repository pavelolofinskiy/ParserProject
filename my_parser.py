from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get('https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273')

bed_list = []
get_beds = driver.find_elements(By.XPATH, "//span[@class='bedrooms']")
for beds in get_beds:
    bed_list.append(beds.text)

date_list = []
get_date = driver.find_elements(By.XPATH, "//span[@class='date-posted']")
for dates in get_date:
    date_list.append(dates.text)

location_list = []
get_location = driver.find_elements(By.XPATH, "//div[@class='location']")
for obj in get_location:
    locations = obj.find_element(By.TAG_NAME, 'span')
    location_list.append(locations.text)

description_list = []
get_description = driver.find_elements(By.XPATH, "//div[@class='description']")
for descriptions in get_description:
    description_list.append(descriptions.text)

title_list = []
get_title = driver.find_elements(By.XPATH, "//a[contains(@class,'title')]")
for titles in get_title:
    title_list.append(titles.text)

price_list = []
get_price = driver.find_elements(By.XPATH, "//div[contains(@class,'price')]")
for prices in get_price:
    price_list.append(prices.text)

source_list = []
get_image_src = driver.find_elements(By.XPATH, '//img')
for img in get_image_src:
    if "https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/" in img.get_attribute('src'):
           source_list.append(img.get_attribute('src'))



time.sleep(5)
driver.close()
driver.quit()







