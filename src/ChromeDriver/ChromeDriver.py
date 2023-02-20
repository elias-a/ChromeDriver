import os
import signal
import subprocess
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ChromeDriver:
    def __init__(self, path, port, profile):
        self._path = path
        self._port = port
        self._profile = profile
        self.driver = None
        self._process = None

    @staticmethod
    def _isPortOpen(port):
        completedProcess = subprocess.run(["lsof", f"-i:{port}"], 
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return completedProcess.returncode != 0

    def initDriver(self):
        if ChromeDriver._isPortOpen(self._port):
            self._openChrome()
        else:
            raise Exception(f"Port {self._port} is taken")

        options = Options()
        options.add_argument("--headless")
        options.add_argument(f"--remote-debugging-port={self._port}")
        self.driver = webdriver.Chrome(options=options)

    def _openChrome(self):
        self._process = subprocess.Popen([
            self._path,
            f"--remote-debugging-port={self._port}",
            f"--user-data-dir={self._profile}",
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, preexec_fn=os.setsid)

    def _killProcess(self):
        os.killpg(os.getpgid(self._process.pid), signal.SIGTERM)

    def closeChrome(self):
        self._killProcess()
        self.driver.quit()

