*** Settings ***
Library    SeleniumLibrary
Library    Collections


Test Teardown    Log To Console    === Test Finished ===

*** Variables ***
${URL}    https://example.com

*** Test Cases ***

1. Ignore Error Example
    ${status}    ${msg}=    Run Keyword And Ignore Error    Should Be Equal    1    2
    Log To Console    Status: ${status}, Message: ${msg}

2. Return Status Example
    ${result}=    Run Keyword And Return Status    Should Be Equal    5    10
    Run Keyword If    not ${result}    Log To Console    Comparison failed but test continues

3. Continue On Failure Example
    Run Keyword And Continue On Failure    Should Be Equal    Hello    Hi
    Log To Console    Still executing after failure

#4. Handle Error Example (Robot 6+)
#    ${status}    ${msg}=    Run Keyword And Handle Error    Fail    Something broke here
#    Log To Console    Status: ${status}, Message: ${msg}

5. Retry Example
    Wait Until Keyword Succeeds    15 sec    3 sec    Should Be Equal    1    2
    Log To Console    This will retry every 3 sec until timeout

6. Teardown Example
    Open Browser    ${URL}    chrome
    Fail    Forcing an error
    [Teardown]    Close Browser

7. Expect Error Example
    # The test fails and logs the Divison error.
    run keyword and expect error    *division error*    evaluate    10/0