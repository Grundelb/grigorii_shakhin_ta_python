from module14.common.hw14 import DemoblizeHomePage

def test_login():
    test_page = DemoblizeHomePage()
    test_page.set_up()
    test_page.open_home_page()
    test_page.open_log_in_form()

    assert test_page.get_login().is_displayed()
    assert test_page.get_password().is_displayed()

    test_page.tear_down()