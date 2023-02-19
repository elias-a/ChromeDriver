import sys
import os
import signal
import pathlib
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ChromeDriver:
    def __init__(self, chromedriver, port, chrome, profile):
        self._chromedriver = chromedriver
        self._port = port
        self._chrome = chrome
        self._profile = profile
        self.driver = None
        self._process = None

    @staticmethod
    def _isPortOpen(port):
        completedProcess = subprocess.run(["lsof", f"-i:{port}"], 
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return completedProcess.returncode != 0

    def initDriver(self):
        options = Options()
        options.headless = True
        options.add_experimental_option("debuggerAddress", f"127.0.0.1:{self._port}")

        if ChromeDriver._isPortOpen(self._port):
            self._openChrome()
        else:
            print(f"Port {self._port} is taken")
            sys.exit(1)

        self.driver = webdriver.Chrome(self._chromedriver, options=options)

    def _openChrome(self):
        self._process = subprocess.Popen([
            f"{pathlib.Path(__file__).parent.resolve()}/start_chrome.sh",
            self._chrome,
            str(self._port),
            self._profile,
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, preexec_fn=os.setsid)

    def closeChrome(self):
        os.killpg(os.getpgid(self._process.pid), signal.SIGTERM)
        self.driver.quit()

