from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import subprocess
import importlib.util

# Verify if the package is installed
package_name = "webdriver_manager"

if importlib.util.find_spec(package_name) is None:
    print(f"Package {package_name} not found. Installing...")
    subprocess.run(["pip", "install", "--upgrade", package_name], check=True)
else:
    print(f"Package {package_name} is already installed.")

from webdriver_manager.chrome import ChromeDriverManager

# Configurations to start the browser
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)