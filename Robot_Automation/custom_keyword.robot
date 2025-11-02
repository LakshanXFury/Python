*** Settings ***

Library    Custom.py


*** Variables ***
${FIRST}    John
${LAST}     Doew


*** Test Cases ***
Add Numbers
    ${result}=     add    2    3
    should be equal as integers    ${result}    5
    log    ${result}

Test Used Name
    Used Name    ${FIRST}

Test Full Name
    ${name}=    Full Name    ${FIRST}    ${LAST}
    Log    Full name is: ${name}