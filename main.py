from selenium import webdriver # pip3 install selenium
from selenium.webdriver.firefox.service import Service as FirefoxService # pip3 install webdriver_manager
from webdriver_manager.firefox import GeckoDriverManager
import time

address = "https://www.boot.dev"
# address = "google.com"

# export TMPDIR=$HOME/tmp geckodriver

# import tempfile
# tempfile.tempdir = '/home/user/my_tmp'


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get(address)