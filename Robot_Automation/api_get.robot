*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${base_url}=    http://api.open-notify.org/iss-now.json
${relative_url}=    iss-now.json
*** Test Cases ***
Get Current ISS status
    Create Session    mysession    ${base_url}
    ${response}=    get request    mysession    ${relative_url}

    log to console    ${response.status_code}
    log to console    ${response.content}
    log to console    ${response.headers}

    # Validations
    ${status_code}=    convert to string    ${response.status_code}
    should be equal    ${status_code}    404

#    ${body}=    convert to string    ${response.content}
#    should contain    ${body}    success

    ${content_type_value}=    get from dictionary    ${response.headers}    Content-Type
    should be equal    ${content_type_value}    application/json; charset=UTF-8