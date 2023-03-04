import os
import re
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChromeDriver:
    def __init__(self, profile = None, chromeVersion = None, options = {}):
        self._profile = profile
        self._chromeVersion = chromeVersion if chromeVersion is not None else self._getSystemChromeVersion()
        self._options = options if options is not None else {}
        self.driver = None

    def _getSystemChromeVersion(self):
        chromePath = "/usr/bin/google-chrome"
        version = os.popen(f"{chromePath} --version").read()
        match = re.search("Google Chrome ([0-9]+)", version)

        if match is None or len(match.groups()) < 1:
            raise Exception(f"Cannot get Chrome version from: {version}.")

        try:
            return int(match.group(1))
        except ValueError:
            raise Exception(f"Cannot convert major version to type \"int\": {match.group(1)}.")

    def initDriver(self):
        self.driver = uc.Chrome(
            user_data_dir=self._profile,
            version_main=self._chromeVersion,
            options=self._addOptions())

    def _addOptions(self):
        options = uc.ChromeOptions()
        [options.add_experimental_option(k, v) for k, v in self._options.items()]

        return options

    def enterInput(self, xPath, text, timeout = 7):
        isLoaded = EC.presence_of_element_located((By.XPATH, xPath))
        element = WebDriverWait(self.driver, timeout).until(isLoaded)
        element.send_keys(text)

    def clickElement(self, xPath, timeout = 7):
        isLoaded = EC.element_to_be_clickable((By.XPATH, xPath))
        element = WebDriverWait(self.driver, timeout).until(isLoaded)
        self.driver.execute_script("arguments[0].click();", element)

