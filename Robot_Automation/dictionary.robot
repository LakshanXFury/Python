*** Settings ***
Library     SeleniumLibrary
Library    Collections

*** Keywords ***

*** Test Cases ***
Single Dictionary in Robot
    ${dict}=    Create Dictionary   name=John   age=25
    Set To Dictionary     ${dict}   city    Bengaluru
    Log    ${dict}

Adding multiple key-value pairs
    ${my_dict}=     Create Dictionary
    Set To Dictionary    ${my_dict}
    ...    firstName    John
    ...    lastName     Smith
    ...    age          25
    ...    country      India
    Log    ${my_dict}