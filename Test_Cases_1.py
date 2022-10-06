import unittest
from _ast import Assert
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(executable_path="drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("http://www.musala.com/")
driver.find_element(By.ID, "wt-cli-accept-all-btn").click()
driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/section[2]/div[1]/div[1]/div[1]/a[1]/button[1]").click()
time.sleep(3)
with open('data.txt') as file:
 for i, line in enumerate(file):
  user = (line)
  sep = ","
  parts = user.split(sep)
  try:
   name = parts[0]
   email = parts[1]
   phone = parts[2]
   subject = parts[3]
   message = parts[4]
   gotdata = parts[5]
  except IndexError:
   gotdata = 'null'
  print(name)
  print(email)
  print(phone)
  print(subject)
  print(message)
  driver.find_element(By.ID,"cf-1").send_keys(name)
  driver.find_element(By.ID,"cf-2").send_keys(email)
  driver.find_element(By.ID,"cf-4").send_keys(subject)
  driver.find_element(By.ID,"cf-5").send_keys(message)
  time.sleep(5)
  validation_messages= driver.find_elements(By.XPATH, "/html[1]/body[1]/div[8]/div[1]/div[9]/div[1]/div[1]/div[1]/form[1]/p[1]/span[1]/span[1]")
  validation_count= len(validation_messages).numerator
  try:
   validation_count > 0
   for val_message in validation_messages:
    print(val_message.text)
  except:
   pass
  driver.find_element(By.XPATH, "/html[1]/body[1]/div[8]/div[1]/div[9]/div[1]/div[1]/div[1]/form[1]/div[3]/p[1]/input[1]").click()
  time.sleep(5)
  driver.find_element(By.ID, "cf-1").clear()
  driver.find_element(By.ID, "cf-2").clear()
  driver.find_element(By.ID, "cf-4").clear()
  driver.find_element(By.ID, "cf-5").clear()




