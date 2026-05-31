*** Settings ***
# For data files, use Variables
Variables   test_data.py
Library    SeleniumLibrary

*** Test Cases ***
Login Test
    FOR    ${row}    IN    @{CREDENTIALS}
        Log To Console    ${row}[0] | ${row}[1] | ${row}[2]
#       Verify Login    ${row}[0]    ${row}[1]    ${row}[2]   ## We can use like this and do ddt
    END

*** Keywords ***
Verify Login
    [Arguments]    ${username}    ${password}    ${expected}
    Input Text     id:username    ${username}
    Input Text      id:password    ${password}
    Click Button    id:login
    Element Should Contain    id:message    ${expected}