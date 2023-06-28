*** Settings ***
Library    SeleniumLibrary
Resource    PO/LandingPage.robot
Resource    PO/HeaderSection.robot
Resource    PO/MonitorsPage.robot
Resource    PO/CartPage.robot

*** Keywords ***
Log In
    LandingPage.Open Landing Page
    LandingPage.Verify Page Loaded
    HeaderSection.Open Login Form
    HeaderSection.Verify Login Form Opened
    HeaderSection.Fill In Login Field
    HeaderSection.Fill In Password Field
    HeaderSection.Click On Login Button
    HeaderSection.Verify User Name

Add Highest Price Monitor To The Cart
    ${expected_product_info} =  MonitorsPage.Open Monitors Category
    MonitorsPage.Add Monitor To The Cart
    HeaderSection.Navigate To The Cart
    [Return]    ${expected_product_info}

Verify Product Name And Product Price
    [Arguments]    ${expected_product_info}
    CartPage.Assert Product Name And Product Price  ${expected_product_info}
