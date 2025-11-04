from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def check_titple_is(self, title):
        driver = self.driver
        page_title = driver.find_element(By.CSS_SELECTOR, "h2")
        assert page_title.text == title
