from unittest import TestCase
from unittest.mock import Mock
from selenium import webdriver
from subprocess import CompletedProcess
from ..ChromeDriver import ChromeDriver

class TestChromeDriver(TestCase):
    def setUp(self):
        self.chrome = Mock(str)
        self.port = 18888
        self.profile = Mock(str)
        self.chromedriver = ChromeDriver(self.chrome, self.port, self.profile)

    def test_initDriver(self):
        self.chromedriver._openChrome = Mock(None, side_effect=self.createProcess)
        self.chromedriver.initDriver()
        assert isinstance(self.chromedriver._process, CompletedProcess)
        assert isinstance(self.chromedriver.driver, webdriver.chrome.webdriver.WebDriver)
        assert ChromeDriver._isPortOpen(self.port) is False

    def test_closeChrome(self):
        self.chromedriver._killProcess = Mock(None)
        self.chromedriver.driver = webdriver.chrome.webdriver.WebDriver()
        self.chromedriver.closeChrome()

    def createProcess(self):
        self.chromedriver._process = Mock(CompletedProcess)

