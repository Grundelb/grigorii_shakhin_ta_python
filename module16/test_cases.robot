*** Settings ***
Library    SeleniumLibrary
Suite Teardown    Close All Browsers

*** Variables ***
${user_login}    gryundelb@gmail.com
${user_password}    Password1

*** Test Cases ***
Test Login
    [Tags]    screenshot
    Open Browser    https://www.demoblaze.com/    Chrome
    Set Selenium Speed    0.5s
    Maximize Browser Window
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
    Open Browser    https://www.demoblaze.com/    Chrome
    Set Selenium Speed    0.5s
    Maximize Browser Window
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

Get Highest Price Monitor
    Wait Until Element Is Visible    xpath=//*[text()='$400']    timeout=10s
    ${products}    Get WebElements    css=.card
    ${highest_price}    Set Variable    -1
    ${highest_price_product}    Set Variable    None
    FOR    ${product}    IN    @{products}
        ${product}    Get Text    xpath=.//h5
        ${price}    Convert To Number    ${product[1:]}
        IF    ${price} > ${highest_price}
            ${highest_price}    Set Variable    ${price}
            ${highest_price_product}    Set Variable    ${product}
        END
    END
    IF    ${highest_price_product} is not ${None}
        ${highest_price_product_name}    Get Text    xpath=${highest_price_product}//h4
        ${highest_price_product_price}    Get Text    xpath=${highest_price_product}//h5
        Click Element    xpath=${highest_price_product}//h4
        Wait Until Element Is Visible    css=h2.name    timeout=10s
        ${result}    Create Dictionary    name=${highest_price_product_name}    price=${highest_price_product_price[1:]}
        [Return]    ${result}
    END

Click Add To Cart Button
    Click Button    //a[text()='Add to cart']
    Handle Alert    ACCEPT

Click Cart Button
    Click Button    css=#cartur

Get Product Info
    ${name} =    Get Text    css=h2.name
    ${price} =    Get Text    xpath=//div[@class='card h-100']//h5
    [Return]    ${name}    ${price}
