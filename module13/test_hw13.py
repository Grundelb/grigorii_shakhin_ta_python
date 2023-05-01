from selenium import webdriver
from selenium.webdriver.common.by import By

def get_page_url():
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.saucedemo.com/')

        login = driver.find_element(By.CSS_SELECTOR, '#user-name')
        login.send_keys('standard_user')
        password = driver.find_element(By.ID, 'password')
        password.send_keys('secret_sauce')
        login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')
        login_button.click()

        return driver.current_url

    finally:
        driver.quit()    

def test_page_url():
    assert get_page_url() == 'https://www.saucedemo.com/inventory.html'
