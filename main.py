from selenium import webdriver # pip3 install selenium
# from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService # pip3 install webdriver_manager
from webdriver_manager.firefox import GeckoDriverManager
import time

# opts = FirefoxOptions()
# opts.add_argument("--headless")
browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# address = "https://www.boot.dev/lessons/acb5117d-0f34-40b3-81f0-b89828f0e443"
address = "google.com"

browser.get(address)