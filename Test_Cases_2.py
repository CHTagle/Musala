from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("http://www.musala.com/")
driver.find_element(By.ID, "wt-cli-accept-all-btn").click()
driver.find_element(By.XPATH,"//header/nav[2]/div[1]/div[1]/ul[1]/li[1]/a[1]").click()
current_url = driver.current_url
print(current_url)
driver.find_element(By.XPATH, "/html[1]/body[1]/footer[1]/div[1]/div[1]/a[4]/span[1]").click()
