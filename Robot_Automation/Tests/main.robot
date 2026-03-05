*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${URL} =    https://www.saucedemo.com/
${BROWSER}=     headlesschrome

*** Keywords ***
Title Verification
    [Documentation]     Verifying the title of the webpage
    [Arguments]     ${TITLE}
    Title Should Be    ${TITLE}


*** Test Cases ***
Login to Sauce demo
    Open Browser    ${URL}      ${BROWSER}
    Title Verification   Swag Labs
    Wait Until Element Is Visible    id:user-name   5s
    Input Text    id:user-name    standard_user
    Input Text    //input[@name='password']    secret_sauce
    Click Element    id:login-button
    ${title}=   Get Title
    Should Be Equal    ${title}    Swag Labs