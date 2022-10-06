import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import HtmlTestRunner
import time


class UnitestCompany(unittest.TestCase):

    def setUp(self):
        # Preconditions:
        self.service = Service(executable_path="drivers/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://www.musala.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=20)

    def test_company_page(self):
        self.driver.find_element(By.ID, "wt-cli-accept-all-btn").click()
        self.driver.find_element(By.XPATH, "//header/nav[2]/div[1]/div[1]/ul[1]/li[1]/a[1]").click()
        url_company_page = self.driver.current_url
        self.assertEqual(url_company_page, "http://www.musala.com/company/")
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/footer[1]/div[1]/div[1]/a[4]/span[1]").click()
        url_facebook_page = self.driver.current_url
        self.assertEqual(url_facebook_page, "http://www.facebook.com/MusalaSoft?fref=ts")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\ELITEBOOK\\PycharmProjects\\Musala_Test\\reports"))