from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class SeleniumUtils:
    def __init__(self):
        self.chrome_options = None
        self.chrome_driver_path = None
        self.url_target = None
        self.service = None
        self.driver = None
        self.keys = Keys()
    def set_url_target(self, url):
        self.url_target = url
    def set_chrome_options(self, stay_open: bool):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", stay_open)
    def set_chrome_driver_path(self, PATH):
        self.chrome_driver_path = PATH
    def set_service(self):
        self.service = Service(self.chrome_driver_path)
    def start_service(self):
        self.service.start()
    def set_driver(self):
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
    def access_url(self):
        self.driver.get(self.url_target)
    def wait_for_presence(self, element_type, timeout_time, element_name):
        try:
            wait = WebDriverWait(self.driver, timeout_time)
            if element_type == "id":
                wait.until(EC.presence_of_element_located((By.ID, element_name)))
            elif element_type == "class-name":
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, element_name)))
            elif element_type == "css-selector":
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element_name)))
            elif element_type == "name":
                wait.until(EC.presence_of_element_located((By.NAME, element_name)))
        except TimeoutException:
            print("Timed out waiting for login page to load")
            self.driver.quit()
    def get_element(self, element_type, element_name):
        if element_type == "id":
            element = self.driver.find_element(By.ID, element_name)
            return element
        elif element_type == "class-name":
            element = self.driver.find_element(By.CLASS_NAME, element_name)
            return element
        elif element_type == "css-selector":
            element = self.driver.find_element(By.CSS_SELECTOR, element_name)
            return element
        elif element_type == "name":
            element = self.driver.find_element(By.NAME, element_name)
            return element
    def send_text(self, target_element, text):
        target_element.send_keys(text)