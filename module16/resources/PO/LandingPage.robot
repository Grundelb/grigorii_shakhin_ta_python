*** Settings ***
Library             SeleniumLibrary

*** Keywords ***
Open Landing Page
    Go To   ${START_URL}

Verify Page Loaded
    Wait Until Page Contains    Log in
