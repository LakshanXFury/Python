*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn

*** Variables ***

@{items}    alpha    beta    gamma
*** Test Cases ***

Run A Keyword For Each Item
    Run keyword i    Log    @{items}

