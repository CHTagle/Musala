import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import HtmlTestRunner
from selenium.webdriver.support.select import Select
import time


class UnitestJobpage(unittest.TestCase):

    def setUp(self):
        # Preconditions:
        self.service = Service(executable_path="drivers/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.get("http://www.musala.com/")
        self.driver.implicitly_wait(time_to_wait=20)

    def test_career_page(self):
        self.driver.find_element(By.ID, "wt-cli-accept-all-btn").click()
        self.driver.find_element(By.XPATH, "//header/nav[2]/div[1]/div[1]/ul[1]/li[5]/a[1]").click()
        self.driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/a[1]/button[1]/span[1]").click()
        url_career_page = self.driver.current_url
        self.assertEqual(url_career_page, "http://www.facebook.com/MusalaSoft?fref=ts")
        selectLocation_dropDown = Select(self.driver.find_element(By.ID, "get_location"))
        selectLocation_dropDown.select_by_value("Sofia")
        sofia_jobs = self.driver.find_elements(By.CLASS_NAME, "card-jobsHot")

        # Imprimir todos el listado de trabajos en Sofia
        print("Sofia")
        for job in sofia_jobs:
            title = job.find_element(By.CLASS_NAME, "card-jobsHot__title").text
            print("Position:" + title)
            link = job.find_element(By.CLASS_NAME, "card-jobsHot__link").get_dom_attribute("href")
            print("More info:" + link)

        selectLocation_dropDown = Select(self.driver.find_element(By.ID, "get_location"))
        selectLocation_dropDown.select_by_value("Skopje")
        skopje_jobs = self.driver.find_elements(By.CLASS_NAME, "card-jobsHot")

        # Imprimir todos el listado de trabajos en Skopje

        print("Skopje")
        for job in skopje_jobs:
            title = job.find_element(By.CLASS_NAME, "card-jobsHot__title").text
            print("Position:" + title)
            link = job.find_element(By.CLASS_NAME, "card-jobsHot__link").get_dom_attribute("href")
            print("More info:" + link)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\ELITEBOOK\\PycharmProjects\\Musala_Test\\reports"))
