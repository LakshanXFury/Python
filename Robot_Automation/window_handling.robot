*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}=    https://vinothqaacademy.com/multiple-windows/

${expected_title}=    Demo Site – WebTable – Vinoth Tech Solution

*** Test Cases ***
Window Handling in Robot
    open browser    ${URL}    chrome
    maximize browser window
    wait until element is visible    //button[text()='New Browser Window']    10s

    click element    //button[text()='New Browser Window']
    ${handels} =    get window handles
    log    The unqiue ID of the Windows are: ${handels}    # Now it will return 2 open window ID as list

    # To switch to new window and close it
    switch window    ${handels}[1]
    ${title} =    get title
    ${status}    ${msg}=    run keyword and ignore error    should be equal    ${title}    ${expected_title}
    Log    Status: ${status}, Message: ${msg}
    close window
    sleep    5s
    # Switch to the first window and do some no operation
    switch window    ${handels}[0]
    click element    //button[text()='New Browser Tab']
    sleep    5s
    close browser



