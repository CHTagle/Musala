import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import HtmlTestRunner
from selenium.webdriver.support.select import Select
import time


class UnitestCareer(unittest.TestCase):

    def setUp(self):
        # Preconditions:
        self.service = Service(executable_path="drivers/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.get("http://www.musala.com/")
        self.driver.implicitly_wait(time_to_wait=20)

#Navigate to Careers menu (from the top) and check that the correct page loads
    def test_career_page(self):
        self.driver.find_element(By.ID, "wt-cli-accept-all-btn").click()
        self.driver.find_element(By.XPATH, "//header/nav[2]/div[1]/div[1]/ul[1]/li[5]/a[1]").click()
        self.driver.find_element(By.XPATH,
                            "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/a[1]/button[1]/span[1]").click()
        url_career_page = self.driver.current_url
        self.assertEqual(url_career_page, "http://www.musala.com/careers/join-us/")
        title_career_page = self.driver.title
        self.assertEqual(title_career_page, "CAREERS")

#Click ‘Check our open positions’ button and Verify that  ‘Join Us’ page is opened (can verify that URL is correct: http://www.musala.com/careers/join-us/
    def test_joinus_page(self):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/a[1]/button[1]/span[1]").click()
        url_facebook_page = self.driver.current_url
        self.assertEqual(url_facebook_page, "http://www.musala.com/careers/join-us")
        selectLocation_dropDown = Select(self.driver.find_element(By.ID, "get_location"))
        selectLocation_dropDown.select_by_value("Anywhere")

    def test_job_page(self):
        applybtn = self.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/section[1]/article[1]/div[1]/div[2]/div[2]/a[1]/input[1]")
        applybtn.click()

    def test_validate_job_page(self):
        self.assertTrue()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
