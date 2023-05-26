*** Settings ***
Library    SeleniumLibrary
Library    custom_keywords.py

Test Setup     Run Keywords
...    ${driver} Open Browser    https://www.demoblaze.com/    Chrome 
...    AND    Set Selenium Speed    0.5s
...    AND    Maximize Browser Window                  
Test Teardown    Close All Browsers

*** Variables ***
${driver}
${user_login}    gryundelb@gmail.com
${user_password}    Password1

*** Test Cases ***
Test Login
    [Tags]    screenshot
    Click Login Button
    Wait Until Element Is Visible    css=#loginusername
    Wait Until Element Is Visible    css=#loginpassword
    Log In
    Wait Until Element Is Visible    css=#logout2
    ${welcome_message}=    Get Text    css=#nameofuser
    Should Be Equal As Strings    ${welcome_message}    Welcome ${user_login}
    Capture Page Screenshot

Test Add Product To Cart
    [Tags]    screenshot
    Click Login Button
    Wait Until Element Is Visible    css=#loginusername
    Wait Until Element Is Visible    css=#loginpassword
    Log In
    Open Monitors Category
     ${product_info}=    Get Highest Price Monitor
    Click Add To Cart Button
    Click Cart Button
    Wait Until Element Is Visible    css=.success
    ${cart_product_info}=    Get Product Info
    Should Be Equal As Strings    ${product_info['name']}    ${cart_product_info['name']}
    Should Be Equal As Strings    ${product_info['price']}    ${cart_product_info['price']}
    Capture Page Screenshot

*** Keywords ***
Login
    Input Text    css=#loginusername    ${user_login}
    Input Text    css=#loginpassword    ${user_password}
    Click Button    //button[text()='Log in']

Click Login Button
    Click Element    css=#login2

Open Monitors Category
    Click Link    //a[text()='Monitors']

Click Add To Cart Button
    Click Link    //a[text()='Add to cart']
    Handle Alert    ACCEPT

Click Cart Button
    Click link    css=#cartur

Get Product Info
    ${name} =    Get Text    xpath=.//td[2]
    ${price} =    Get Text    xpath=.//td[3]
    [Return]    ${name}    ${price}
