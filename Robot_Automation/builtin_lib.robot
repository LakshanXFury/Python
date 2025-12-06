*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn

*** Variables ***

@{items}    alpha    beta    gamma
${Variable_1} =    PROD

*** Test Cases ***

Run A Keyword IF
    Run keyword if    "${Variable_1}"=="PROD"    Log    The Run keyword if passed >

Run A Keyword IF NOT
    Run keyword unless    "${Variable_1}"=="NOT-PROD"    Log    The Run keyword if Failed >
