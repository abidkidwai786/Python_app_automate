import requests
import json
import ssl
import sys
import os
path = os.getcwd()
sys.path.append(os.path.abspath(os.path.join(path, os.pardir)))
from time import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

from threading import Thread
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://manual-api.lambdatest.com/app/upload/realDevice"

payload='url=https%3A%2F%2Fprod-mobile-artefacts.lambdatest.com%2Fassets%2Fdocs%2Fproverbial_android.apk&name=android_proverbial'
headers = {
  'Authorization': 'Basic YWJpZGs6NVIzQnFzQkRrQW54Q3JtZXM1dVlMWnlQNHY5ODk0WXVRdG9rTkRxU1VkdUNnaGVrUkg=',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

y = json.loads(response.text)
aurl=y["app_url"]
print(aurl)

caps = [

    {
        "deviceName": "Galaxy S21",
        "platformName": "android",
        "platformVersion": "11",
        "app": aurl,
        # "infraTimeout": 100,
        "isRealMobile": True,
        # "tunnel": True,
        "deviceOrientation": "PORTRAIT",
        "visual": True,
        "console": True,
        "devicelog" : True,
        "build": "Python App Automation",
        # "devicelog": True,
        # "tunnel": True,
        #  "geoLocation": "BR",
    },
]

username = os.environ.get("LT_USERNAME")
accesskey = os.environ.get("LT_ACCESS_KEY")

def run_session(desired_cap):
    driver = webdriver.Remote(
        # hub.mobile-dev-1.dev.lambdatest.io/wd/hub",
        command_executor="https://"+username+":"+accesskey+"@beta-hub.lambdatest.com/wd/hub",
        desired_capabilities=desired_cap)

    try:
        colorElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/color")))
        colorElement.click()

        textElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/Text")))
        textElement.click()

        toastElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/toast")))
        toastElement.click()

        notification = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/notification")))
        notification.click()

        geolocation = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/geoLocation")))
        geolocation.click()

        home = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/Home")))
        home.click()

        speedTest = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/speedTest")))
        speedTest.click()

        home = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/Home")))
        home.click()

        browser = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/Browser")))
        browser.click()

        url = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/url")))
        url.send_keys("https://www.lambdatest.com")

        find = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/find")))
        find.click()

        driver.quit()
    except:
        driver.quit()


for cap in caps:
    Thread(target=run_session, args=(cap,)).start()