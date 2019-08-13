import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_search_in_python_org(cls):
        driver = cls.driver
        driver.get("http://www.python.org")
        cls.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_search_in_python_org2(cls):
        driver = cls.driver
        driver.get("http://google.com")
        cls.assertIn("Google", driver.title)
        elem = driver.find_element(By.CSS_SELECTOR, "input[name='q']")
        elem.send_keys("python")
        elem.send_keys(Keys.ENTER)
        elem = driver.find_element_by_css_selector("div#rso div.rc a")
        assert "https://www.python.org/" in elem.get_attribute("href")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
