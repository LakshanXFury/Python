*** Settings ***
Library     RequestsLibrary

*** Test Cases ***
Get ISS info
    # If you're testing an API with multiple endpoints, use GET On Session. If you just need one quick request, GET is simpler.

    Create Session    mysession    http://api.open-notify.org  #Base URL
    ${response}=    GET On Session      mysession       /iss-now.json       #Endpoint

    Log To Console      ${response}
    Log To Console      ${response.json()}
    
    Log To Console    ${response.json()}[message]

    Should Be Equal As Strings    ${response.json()}[message]    success