import undetected_chromedriver as uc
from unittest import TestCase
from tempfile import TemporaryDirectory
from ChromeDriver import ChromeDriver


class Test_ChromeDriver(TestCase):
    def test_init(self):
        with TemporaryDirectory(ignore_cleanup_errors=True) as user_data_dir:
            chromedriver = ChromeDriver(user_data_dir)
            assert isinstance(chromedriver.driver, uc.Chrome)
            assert chromedriver.driver.user_data_dir == user_data_dir
