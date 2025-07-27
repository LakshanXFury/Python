*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${base_url} =    http://restapi.demoqa.com/customer

*** Test Cases ***
Put_CustomerRegistration
    create session    mysession    ${base_url}
    # To send data
    ${body}=    create dictionary    FirstName=Night    LastName=Fury    UserName=night_fury    Password=password    #Data
    ${header}=    create dictionary    Content-Type=application/json    #Type of data that is sent
    ${response}=    post request    mysession    /register    data=${body}    headers=${header}

    log to console    ${response.status_code}
    log to console    ${response.content}

    # Validations
    ${res_body} =    convert to string     ${response.content}
    should contain    ${res_body}    OPERATION_SUCCESS
