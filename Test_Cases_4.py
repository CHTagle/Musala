from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import time

service = Service(executable_path="drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("http://www.musala.com/")
driver.find_element(By.ID,"wt-cli-accept-all-btn").click()
driver.find_element(By.XPATH,"//header/nav[2]/div[1]/div[1]/ul[1]/li[5]/a[1]").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/a[1]/button[1]/span[1]").click()
#Para tomar la url actual y comprobarla luego
current_url = driver.current_url
selectLocation_dropDown = Select(driver.find_element(By.ID, "get_location"))
selectLocation_dropDown.select_by_value("Sofia")
sofia_jobs = driver.find_elements(By.CLASS_NAME, "card-jobsHot")

#Imprimir todos el listado de trabajos en Sofia
print("Sofia")
for job in sofia_jobs:
    title = job.find_element(By.CLASS_NAME,"card-jobsHot__title").text
    print("Position:" + title)
    link = job.find_element(By.CLASS_NAME, "card-jobsHot__link").get_dom_attribute("href")
    print("More info:" + link)

selectLocation_dropDown = Select(driver.find_element(By.ID, "get_location"))
selectLocation_dropDown.select_by_value("Skopje")
skopje_jobs = driver.find_elements(By.CLASS_NAME, "card-jobsHot")

#Imprimir todos el listado de trabajos en Skopje

print("Skopje")
for job in skopje_jobs:
    title = job.find_element(By.CLASS_NAME,"card-jobsHot__title").text
    print("Position:" + title)
    link = job.find_element(By.CLASS_NAME, "card-jobsHot__link").get_dom_attribute("href")
    print("More info:" + link)
    print("************************************************************************")

