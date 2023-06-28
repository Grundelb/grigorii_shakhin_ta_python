*** Settings ***
Resource         ../resources/Demoblaze.robot
Resource         ../resources/Common.robot
Test Setup       Common.Begin Web Test
Test Teardown    Common.End Web Test
#run: robot -d results tests/TestDemoblaze.robot

*** Variables ***
${START_URL} =    https://www.demoblaze.com/
${USER_LOGIN} =                     gryundelb@gmail.com
${USER_PASSWORD} =                  Password1

*** Test Cases ***
User Should Be Able To Login
    [Tags]    first
    Demoblaze.Log In

User Should Be Able To Add Monitor To Cart
    [Tags]    second
    Demoblaze.Log In
    ${expected_product_info} =    Demoblaze.Add Highest Price Monitor To The Cart
    Demoblaze.Verify Product Name And Product Price    ${expected_product_info}
