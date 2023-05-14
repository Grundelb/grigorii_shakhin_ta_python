from module14.common.hw14 import DemoblizeHomePage

def test_login():
    test_page = DemoblizeHomePage()
    test_page.set_up()
    test_page.open_home_page()
    test_page.open_log_in_form()

    assert test_page.get_login().is_displayed()
    assert test_page.get_password().is_displayed()

    test_page.log_in()

    assert test_page.get_logout_button().is_displayed()
    assert test_page.get_welcome_message().text == f'Welcome {test_page.user_login}'

    test_page.tear_down()

def test_add_monitor_with_highest_price():
    test_page = DemoblizeHomePage()
    test_page.set_up()
    test_page.open_home_page()
    test_page.open_log_in_form()
    test_page.log_in()
    test_page.open_monitors_category()
    
    assert test_page.get_highest_price_monitor() == test_page.get_highest_price_monitor_card_info()
    
    test_page.add_to_cart()
    
    assert test_page.highest_price_element[0] == test_page.open_cart()

    test_page.tear_down()