from module14.common.hw14 import DemoblizeHomePage

def test_login(driver):
    test_page = DemoblizeHomePage(driver)
    test_page.open_home_page()
    test_page.open_log_in_form()

    assert test_page.get_login().is_displayed(), 'Login field is not displayed'
    assert test_page.get_password().is_displayed(), 'Password field is not displayed'

    test_page.log_in()

    assert test_page.get_logout_button().is_displayed(), 'Logout button is not displayed'
    assert test_page.get_welcome_message().text == f'Welcome {test_page.user_login}'

def test_add_monitor_with_highest_price(driver, login):
    test_page = DemoblizeHomePage(driver)
    test_page.open_monitors_category()
    
    assert test_page.get_highest_price_monitor() == test_page.get_highest_price_monitor_card_info()
    
    test_page.add_to_cart()
    
    assert test_page.highest_price_element[0] == test_page.open_cart()
