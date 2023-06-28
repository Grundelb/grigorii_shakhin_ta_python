*** Settings ***
Library             SeleniumLibrary

*** Variables ***
${LOGIN_FORM_LOG_IN_USER_NAME} =    css=#loginusername
${LOGIN_FORM_LOG_IN_PASSWORD} =     css=#loginpassword
${HEADER_LOG_IN_LINK} =             css=#login2
${LOGIN_FORM_LOGIN_BUTTON} =        xpath=//button[text()='Log in']
${HEADER_LOG_OUT_BUTTON} =          css=#logout2
${HEADER_USER_NAME} =               css=#nameofuser
${HEADER_CART_ICON} =               css=#cartur

*** Keywords ***

Open Login Form
    Click Element    ${HEADER_LOG_IN_LINK}

Verify Login Form Opened
    Wait Until Element Is Visible    ${LOGIN_FORM_LOG_IN_USER_NAME}
    Wait Until Element Is Visible    ${LOGIN_FORM_LOG_IN_PASSWORD}

Fill In Login Field
    Input Text    ${LOGIN_FORM_LOG_IN_USER_NAME}    ${USER_LOGIN}

Fill In Password Field
    Input Text    ${LOGIN_FORM_LOG_IN_PASSWORD}    ${USER_PASSWORD}

Click On Login Button
    Click Button    ${LOGIN_FORM_LOGIN_BUTTON}

Verify User Name
    Wait Until Element Is Visible    ${HEADER_LOG_OUT_BUTTON}
    ${welcome_message}=    Get Text    ${HEADER_USER_NAME}
    Should Be Equal As Strings    ${welcome_message}    Welcome ${USER_LOGIN}

Navigate To The Cart
    Click link    ${HEADER_CART_ICON}
