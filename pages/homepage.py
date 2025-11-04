from selenium.webdriver.common.by import By


MAIN_PAGE = "https://demoblaze.com/"


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        driver = self.driver
        driver.get(MAIN_PAGE)

    def click_galaxy_s6(self):
        driver = self.driver
        galaxy_s6 = driver.find_element(
            By.XPATH,
            '//a[text()="Samsung galaxy s6"]',
        )
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = self.driver.find_element(
            By.CSS_SELECTOR,
            """[onclick="byCat('monitor')"]""",
        )

        monitor_link.click()

    def check_products_count(self, count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, ".card-block")
        assert len(monitors) == count
