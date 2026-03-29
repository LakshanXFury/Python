*** Settings ***
Library     RequestsLibrary

*** Variables ***
${url} =    https://jsonplaceholder.typicode.com

*** Keywords ***
Check API status
    [Arguments]     ${endpoint}     ${status_code}
    Create Session    api_session    ${url}
    # expected_status=any, tells to accept all the status code
    ${response}=     GET On Session     api_session     ${endpoint}     expected_status=any
    Log    ${response.status_code}
    Should Be Equal As Strings    ${response.status_code}    ${status_code}

*** Test Cases ***
Verify Status Code
    [Template]     Check API status
    /posts/1        200
    /posts/999      404
    /users/1        200
