*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url} =    https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame

*** Keywords ***
Consent form
    wait until element is visible    //p[text()='Consent']    5s
    run keyword and continue on failure    click element    //p[text()='Consent']


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
    unselect frame
    click element    //div[text()='Automation']




