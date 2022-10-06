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
driver.find_element(By.ID, "wt-cli-accept-all-btn").click()
driver.find_element(By.XPATH,"//header/nav[2]/div[1]/div[1]/ul[1]/li[5]/a[1]").click()
driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/a[1]/button[1]/span[1]").click()
current_url = driver.current_url #Para tomar la url actual y comprobarla luego
selectLocation_dropDown = Select(driver.find_element(By.ID, "get_location"))
selectLocation_dropDown.select_by_value("Anywhere")
driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/section[1]/div[2]/article[12]/div[1]/a[1]").click()
#Apply
applybtn = driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/section[1]/article[1]/div[1]/div[2]/div[2]/a[1]/input[1]")
applybtn.click()

driver.find_element(By.NAME, "your-name").send_keys("")
driver.find_element(By.NAME, "your-email").send_keys("Celia Indira")
driver.find_element(By.NAME, "mobile-number").send_keys("Celia Indira")
driver.find_element(By.ID, "uploadtextfield").send_keys("\\Users\\ELITEBOOK\\Desktop\\Celia Indira Hidalgo Tagle - Resume.pdf")
driver.find_element(By.NAME, 'linkedin').send_keys("Celia Indira")
driver.find_element(By.NAME, "your-message").send_keys("Celia Indira")
consent = driver.find_element(By.NAME, "adConsentChx")
consent.click()
selected = consent.is_selected()
print("Selected:" + selected)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[8]/div[1]/div[9]/div[1]/div[1]/div[1]/form[1]/div[4]/p[1]/input[1]").click()