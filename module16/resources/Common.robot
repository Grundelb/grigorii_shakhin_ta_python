*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Begin Web Test
    Open Browser    about:blank    Chrome
    Set Selenium Speed    0.5s
    Maximize Browser Window
    SeleniumLibrary.set browser implicit wait    10s

End Web Test
    Close All Browsers
