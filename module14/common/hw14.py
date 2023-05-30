from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoblizeHomePage:

    base_url = 'https://www.demoblaze.com/'
    user_login = 'gryundelb@gmail.com'
    user_password = 'Password1'
    highest_price_element = []

    def __init__(self, driver) -> None:
        self.driver = driver

    def open_home_page(self):
        self.driver.get(self.base_url)

    def open_log_in_form(self):
        login_form = self.driver.find_element(By.CSS_SELECTOR, '#login2')
        login_form.click()
        login_form = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-content #logInModalLabel'))
            )

    def log_in(self):
        login = self.driver.find_element(By.CSS_SELECTOR, '#loginusername')
        password = self.driver.find_element(By.CSS_SELECTOR, '#loginpassword')
        login.send_keys(self.user_login)
        password.send_keys(self.user_password)
        login_button = self.driver.find_element(By.XPATH, '//button[text() ="Log in"]')
        login_button.click()

    def get_login(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#loginusername')

    def get_password(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#loginpassword')
    
    def get_logout_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#logout2'))
            )
        return self.driver.find_element(By.CSS_SELECTOR, '#logout2')
    
    def get_welcome_message(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#nameofuser'))
            )
        return self.driver.find_element(By.CSS_SELECTOR, '#nameofuser')
    
    def open_monitors_category(self):
        self.driver.refresh()
        monitors_category_locator = (By.XPATH, "//a[text()='Monitors']")
        monitors_category = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(monitors_category_locator)
            )
        monitors_category.click()

    def get_highest_price_monitor(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[text()='$400']"))
            )
        products = self.driver.find_elements(By.CSS_SELECTOR, '.card')
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
            self.highest_price_element.append((highest_price_product_name, highest_price_product_price[1:]))
            highest_price_product.find_element(By.XPATH, './/h4').click()
            WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h2.name'))
            )
            return {'name': highest_price_product_name, 'price' : highest_price_product_price}
        
    def get_highest_price_monitor_card_info(self):
        name = self.driver.find_element(By.CSS_SELECTOR, 'h2.name').text
        price = self.driver.find_element(By.CSS_SELECTOR, 'h3.price-container').text.split()[0]
        return {'name': name, 'price': price}


    def add_to_cart(self):
        self.driver.find_element(By.XPATH, '//a[text() = "Add to cart"]').click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
    
    def open_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '#cartur').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.success'))
            )
        product_card = self.driver.find_element(By.CSS_SELECTOR, '.success')
        return product_card.find_element(By.XPATH, './td[2]').text, product_card.find_element(By.XPATH, './td[3]').text

    