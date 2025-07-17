*** Settings ***

Library    Custom.py

*** Test Cases ***
Add Numbers
    ${result}=     add    2    3
    should be equal as integers    ${result}    5
    log    ${result}