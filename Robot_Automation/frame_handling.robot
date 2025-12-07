*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url} =    https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame

*** Keywords ***
Consent form
    ${consent_present} =    Run Keyword And Return Status
    ...     Wait Until Element Is Visible    //p[text()='Consent']    5s
    Run Keyword If    ${consent_present}    Click Element    //p[text()='Consent']
    Run Keyword If    ${consent_present}    Log    Consent form clicked
    ...     ELSE    Log    Consent form not present, continuing test


*** Test Cases ***
Frame Handling in ROBOT
    open browser    ${url}    chrome
    maximize browser window
    Consent form
    scroll element into view    //span[text()='Miscellaneous']
    sleep    5s
    # Do the operation inside the frame and come out
    select frame    //div[@rel-title="iFrame"]//iframe
    click element    //span[text()='Trainings']//ancestor::div[5]/following-sibling::div//div[@id='portfolio_filter']
    sleep    5s
    click element    //div[text()='Automation']
    unselect frame
    ${status}  ${result} =      Run Keyword And Ignore Error    click element    //div[text()='Automation']
    Log To Console    Status: ${status}
    Log To Console    Result/Error: ${result}