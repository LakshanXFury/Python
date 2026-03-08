*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASEURL}=     https://jsonplaceholder.typicode.com
${ENDPOINT}=   /users

*** Test Cases ***
Get user API request
    Create Session  mysession   ${BASEURL}
    ${response}=      Get On Session     mysession    ${ENDPOINT}
#    Log To Console    ${response}

    ${statuscode}=      Convert To String   ${response.status_code}

    Should Be Equal    ${statuscode}    200
