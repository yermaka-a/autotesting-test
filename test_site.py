import time
from selenium.webdriver.common.by import By

MAIN_PAGE = "https://demoblaze.com/"


def test_open_s6(driver):
    driver.get(MAIN_PAGE)
    galaxy_s6 = driver.find_element(
        By.XPATH,
        '//a[text()="Samsung galaxy s6"]',
    )
    galaxy_s6.click()
    title = driver.find_element(By.CSS_SELECTOR, "h2")
    assert title.text == "Samsung galaxy s6"


def test_two_monitors(driver):
    driver.get(MAIN_PAGE)
    monitor_link = driver.find_element(
        By.CSS_SELECTOR,
        """[onclick="byCat('monitor')"]""",
    )
    monitor_link.click()
    time.sleep(1)
    monitors = driver.find_elements(By.CSS_SELECTOR, ".card-block")
    assert len(monitors) == 2
