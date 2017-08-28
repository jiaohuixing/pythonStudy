import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class RomanNumeralConverterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
    def tearDown(self):
        self.driver.close()
    def test_(self):
        print(123)
        driver = self.driver
        driver.get("http://www.baidu.com")
        #assert "Python" in driver.title
        elem = driver.find_element_by_id("kw")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


if __name__ =="__main__":
    unittest.main()
