from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.BuiltIn import RobotNotRunningError
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@keyword('Get Highest Price Monitor')
def get_highest_price_monitor():
    highest_price_element = []
    try:
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        driver = seleniumlib.driver
    except RobotNotRunningError:
        raise AssertionError("No running Robot Framework instance found.")

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card'))
    )
    products = driver.find_elements(By.CSS_SELECTOR, '.card')
    highest_price = -1
    highest_price_product = None
    for product in products:
        price = float(product.find_element(By.XPATH, './/h5').text[1:])
        if price > highest_price:
            highest_price = price
            highest_price_product = product
    if highest_price_product is not None:
        highest_price_product_name = highest_price_product.find_element(By.XPATH, './/h4').text
        highest_price_product_price = highest_price_product.find_element(By.XPATH, './/h5').text
        highest_price_product.find_element(By.XPATH, './/h4').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h2.name'))
        )
        return {'name': highest_price_product_name, 'price': highest_price_product_price[1:]}
