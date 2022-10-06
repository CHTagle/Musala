import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import HtmlTestRunner
import time


class UnitestContactUs(unittest.TestCase):

    def setUp(self):
        # Preconditions:
        self.service = Service(executable_path="drivers/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://www.musala.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=20)

    def test_contactUS_page(self):
        self.driver.find_element(By.ID, "wt-cli-accept-all-btn").click()
        self.driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/main[1]/section[2]/div[1]/div[1]/div[1]/a[1]/button[1]").click()
        self.driver.find_element(By.ID, "cf-1").send_keys("Celia")
        self.driver.find_element(By.ID, "cf-2").send_keys("email")
        self.driver.find_element(By.ID, "cf-4").send_keys("subject")
        self.driver.find_element(By.ID, "cf-5").send_keys("message")
        time.sleep(5)
        self.assertTrue(self.driver.find_elements(By.XPATH,
                                                  "/html[1]/body[1]/div[8]/div[1]/div[9]/div[1]/div[1]/div[1]/form[1]/p[2]/span[1]/span[1]"), msg="The validation message does not display as expected")
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\ELITEBOOK\\PycharmProjects\\Musala_Test\\reports"))
