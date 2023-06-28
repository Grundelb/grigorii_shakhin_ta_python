*** Settings ***
Library    SeleniumLibrary
Library     ../custom_keywords.py

*** Variables ***
${MONITORS_CATEGORY_LINK} =                 xpath=//a[text()='Monitors']
${ITEM_VIEW_ADD_ITEM_TO_THE_CART_LINK} =    xpath=//a[text()='Add to cart']

*** Keywords ***
Open Monitors Category
    Click Link    ${MONITORS_CATEGORY_LINK}
    ${expected_product_info} =    Get Highest Price Monitor
    [Return]    ${expected_product_info}

Add Monitor To The Cart
    Click Link    ${ITEM_VIEW_ADD_ITEM_TO_THE_CART_LINK}
    Handle Alert    ACCEPT
