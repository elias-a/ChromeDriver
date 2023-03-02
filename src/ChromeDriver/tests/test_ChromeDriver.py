import re
import tempfile
from unittest import TestCase
from unittest.mock import Mock
from selenium import webdriver
from ..ChromeDriver import ChromeDriver

class TestChromeDriver(TestCase):
    def setUp(self):
        with tempfile.TemporaryDirectory() as directory:
            self._directory = directory
            self.chromedriver = ChromeDriver(profile=directory)

    def test_initDriver(self):
        self.chromedriver.initDriver()
        assert isinstance(self.chromedriver.driver, webdriver.chrome.webdriver.WebDriver)
        assert self.chromedriver.driver.user_data_dir == self._directory
        
        version = self.chromedriver.driver.capabilities["browserVersion"]
        match = re.search("([0-9]+)", version)
        assert match is not None
        assert len(match.groups()) == 1
        assert isinstance(int(match.group(1)), int)

    def test_enterInput(self):
        pass

    def test_clickElement(self):
        pass

