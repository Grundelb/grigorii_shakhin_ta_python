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
    pass