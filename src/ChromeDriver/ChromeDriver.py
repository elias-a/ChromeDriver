import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChromeDriver:
    def __init__(self, user_data_dir, headless=False, timeout=10):
        self.timeout = timeout
        self.driver = self._init_driver(user_data_dir, headless)

    def __del__(self):
        self.driver.quit()

    def _init_driver(self, user_data_dir, headless):
        return uc.Chrome(user_data_dir=user_data_dir, headless=headless)

    def _add_options(self, opts):
        options = uc.ChromeOptions()
        [options.add_experimental_option(k, v) for k, v in opts.items()]
        return options

    def get(self, url):
        self.driver.get(url)

    def send_keys(self, xpath, text):
        is_loaded = EC.presence_of_element_located((By.XPATH, xpath))
        element = WebDriverWait(self.driver, self.timeout).until(is_loaded)
        element.send_keys(text)

    def click(self, xpath):
        is_loaded = EC.element_to_be_clickable((By.XPATH, xpath))
        element = WebDriverWait(self.driver, self.timeout).until(is_loaded)
        self.driver.execute_script("arguments[0].click();", element)
