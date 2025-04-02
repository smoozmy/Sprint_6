from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_visibility_of_element_located(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_element_to_be_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_url_to_be(self, url):
        return self.wait.until(EC.url_to_be(url))

    def send_keys_field(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)