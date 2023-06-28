*** Settings ***
Library               SeleniumLibrary

*** Variables ***
${CART_FIRST_ITEM_NAME} =     xpath=.//td[2]
${CART_FIRST_ITEM_PRICE} =    xpath=.//td[3]
${CART_SUCCESS_MESSAGE} =     css=.success

*** Keywords ***
Get Product Info
    ${name} =     Get Text    ${CART_FIRST_ITEM_NAME}
    ${price} =    Get Text    ${CART_FIRST_ITEM_PRICE}
    [Return]        ${name}    ${price}

Assert Product Name And Product Price
    [Arguments]    ${expected_product_info}
    Wait Until Element Is Visible    ${CART_SUCCESS_MESSAGE}
    ${name}    ${price}    Get Product Info
    Should Be Equal As Strings    ${expected_product_info['name']}    ${name}
    Should Be Equal As Strings    ${expected_product_info['price']}    ${price}
