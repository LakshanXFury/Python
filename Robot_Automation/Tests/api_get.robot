*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASEURL}=     https://jsonplaceholder.typicode.com
${ENDPOINT}=   /users/1

*** Test Cases ***
Get user API request
    Create Session  mysession   ${BASEURL}
    ${response}=      Get On Session     mysession    ${ENDPOINT}
#    Log To Console    ${response}

    ${statuscode}=      Convert To String   ${response.status_code}

    Should Be Equal    ${statuscode}    200
    Status Should Be    200     ${response}
    Should Not Be Empty    ${response.json()['name']}
